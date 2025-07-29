from django.shortcuts import render
from .models import InstaPost
from .forms import PostingInsta,Register,CommentForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseForbidden

# Create your views here.

def index(request):
    posts = InstaPost.objects.all().order_by('-uploaded_at')
    comment_form = CommentForm()

    return render(request, 'index.html', {
        'posts': posts,
        'comment_form': comment_form
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostingInsta(request.POST, request.FILES)  
        if form.is_valid():
            fpost = form.save(commit=False)
            fpost.user = request.user
            fpost.save()
            return redirect('home_page')
    else:
        form = PostingInsta()

    return render(request, "posting.html", {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(InstaPost, id=post_id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('home_page')  

    return render(request, 'confirm_delete.html', {'post': post})

def register(request):
    form = Register()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
@login_required  
def toggle_like(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to like posts.")
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = InstaPost.objects.get(id=post_id)

        liked_posts = request.session.get('liked_posts', [])

        if post_id in liked_posts:
            post.likes -= 1
            liked_posts.remove(post_id)
            liked = False
        else:
            post.likes += 1
            liked_posts.append(post_id)
            liked = True

        post.save()
        request.session['liked_posts'] = liked_posts

        return JsonResponse({'likes': post.likes, 'liked': liked})
    
@login_required
def view_comments(request, post_id):
    post = InstaPost.objects.get(id=post_id)
    comments = post.comments.all()
    form = CommentForm()

    return render(request, 'comments.html', {
        'post': post,
        'comments': comments,
        'comment_form': form
    })
    
@csrf_exempt
@login_required
def post_comment(request, post_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to comment.")
    
    if request.method == 'POST':
        post = InstaPost.objects.get(id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('view_comments', post_id=post.id)
        
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = Register()
        
    return render(request, 'registration/login.html', {'form':form})   

def logout(request):
    if request.method == 'POST':
        return render(request, 'registration/logout.html')