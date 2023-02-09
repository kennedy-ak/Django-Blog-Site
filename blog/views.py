from django.shortcuts import render ,get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    
    
class SinglePostView(View):
    # template_name ="blog/post-detail.html"
    # model = Post
    
    def get(self,request, slug):
        post = Post.objects.get(slug = slug)
        context ={
            "post":post,
            "post_tag":post.tag.all(),
            "comment_form": CommentForm,
            "comments":post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():

            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("single_post",args=[slug]))

        context ={
            "post":post,
            "post_tag":post.tag.all(),
            "comment_form": CommentForm,
            "comments":post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)        
        
    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tag.all()
    #     context["comment_form"] = CommentForm()
    #     return context
    
    

# def single_post_page(request, slug):
#     identified_post =get_object_or_404(Post,slug = slug)
#     return render(request, "blog/post-detail.html ",{
#         "post":identified_post,
#         "post_tags":identified_post.tag.all()
#     })


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_post")
        
        context = {}
        if stored_posts is None or len(stored_posts) ==0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in = stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
            
            
        return render(request, "blog/stored-post.html", context)
        
        
        
    def post(self,request):
        stored_posts = request.session.get("stored_post")
        
        if stored_posts is None:
            stored_posts = []
            
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
            
        return HttpResponseRedirect("/")
            
    
    