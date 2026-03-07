from django.shortcuts import render,redirect
from.models import blog,comment
from django.shortcuts import get_object_or_404
from .forms import commentform 

def blog_list(request):
    posts = blog.objects.all()
    carousel = blog.objects.all().order_by("-id")[:4]
    return render(request,'list.html',{'posts':posts,"carousel":carousel})

def blog_detail(request,pk):
    posts = get_object_or_404(blog,pk=pk)
    comments = posts.comments.all
    
    if request .method == "POST":
        form = commentform(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.posts = posts
            comment.save()
            
            return redirect("detail",pk=pk)
    else:
        form = commentform()
              
    return render(request,"detail.html",{"posts":posts, "form":form ,'comments':comments}) 

def post_like(request,pk):
    post = get_object_or_404(blog,pk=pk)
    post.likes += 1
    post.save()
    return redirect("detail",pk=pk)


def search (request):    
    query = request.GET.get('q','')
    results = blog.objects.filter(title__icontains=query)
    
    return render (request,'search.html',{'query':query, 'results':results})
    
