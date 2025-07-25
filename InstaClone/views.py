from django.shortcuts import render
from .models import InstaPost
from .forms import PostingInsta
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    posts = InstaPost.objects.all().order_by('-uploaded_at')
    return render(request,'index.html',{"posts" : posts})

def create_post(request):
    if request.method == 'POST':
        form = PostingInsta(request.POST)
        if form.is_valid():
            fpost = form.save(commit=False)
            fpost.user = request.user
            fpost.save()
    else:
        form = PostingInsta()
        
    return render(request, "posting.html" , {'form' : form})

def del_post(request, post_id):
    delpost = get_object_or_404(InstaPost , pk=post_id ,user= request.user)