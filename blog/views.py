from django.shortcuts import render ,get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView, DetailView



class StartPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
# def starting_page(request):
#     lastest_post = Post.objects.all().order_by("-date")[:3]

    
#     return render(request, "blog/index.html",{
#         "posts":lastest_post
#     })

# def all_post(request):
#     all_posts = Post.objects.all().order_by("-date")

#     return render(request,"blog/all_post.html",{
#         "all_posts":all_posts
#     })

class AllPostView(ListView):
    template_name = "blog/all_post.html"
    model = Post
    ordering = ["-date"]
    context_object_name ="all_posts"
    
    
class SinglePostView(DetailView):
    template_name ="blog/post-detail.html"
    model = Post
    
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tag.all()
        context["comment_form"] = CommentForm()
        return context
    
    

# def single_post_page(request, slug):
#     identified_post =get_object_or_404(Post,slug = slug)
#     return render(request, "blog/post-detail.html ",{
#         "post":identified_post,
#         "post_tags":identified_post.tag.all()
#     })
