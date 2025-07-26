from django.shortcuts import render
from .models import InstaPost
from .forms import PostingInsta
from django.shortcuts import get_object_or_404,redirect

# Create your views here.

def index(request):
    posts = InstaPost.objects.all().order_by('-uploaded_at')
    return render(request,'layout.html',{"posts" : posts})

# def create_post(request):
#     if request.method == 'POST':
#         form = PostingInsta(request.POST)
#         if form.is_valid():
#             fpost = form.save(commit=False)
#             fpost.user = request.user
#             fpost.save()
#     else:
#         form = PostingInsta()
        
#     return render(request, "posting.html" , {'form' : form})

# def delete_post(request, post_id):
#     post = get_object_or_404(InstaPost, id=post_id, user=request.user)

#     if request.method == 'POST':
#         post.delete()
#         return redirect('index')  

#     return render(request, 'confirm_delete.html', {'post': post})