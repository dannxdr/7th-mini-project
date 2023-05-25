from django.shortcuts import render, redirect

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse



# Create your views here.
def index(request):
    return render(request, 'blog/post_form.html', context={"active" : "blog"})


class PostList(ListView):
    model = Post
    ordering = '-pk'  #포스트 목록이 최신 글부터 나열
    #paginate_by = 5


class PostDetail(DetailView):
    model = Post

class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content', 'head_image', 'file_upload']
    
    def form_valid(self, form):  #포스트를 로그인한 방문자만 작성할 수 있음
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate,self).form_valid(form)
        else:
            return redirect('/blog/')
        
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title','content', 'head_image', 'file_upload'] 
    template_name = 'blog/post_update_form.html'
    


