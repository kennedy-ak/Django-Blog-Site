from django.shortcuts import render ,get_object_or_404


from .models import Post
# Create your views here.


def starting_page(request):
    lastest_post = Post.objects.all().order_by("-date")[:3]
     
    
    return render(request, "blog/index.html",{
        "posts":lastest_post
    })
    #return HttpResponse("<h1>This is the starting page</h1>")

def all_post(request):
    all_posts = Post.objects.all().order_by("-date")
    #return HttpResponse("<h1>This is the starting page</h1>1111")
    return render(request,"blog/all_post.html",{
        "all_posts":all_posts
    })

def single_post_page(request, slug):
    identified_post =get_object_or_404(Post,slug = slug)
    return render(request, "blog/post-detail.html ",{
        "post":identified_post,
        "post_tags":identified_post.tag.all()
    })