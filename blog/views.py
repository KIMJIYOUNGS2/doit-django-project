# from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    ordering = '-pk'  # Post 레코드 중 pk값이 작은 순서대로 보여주기 = 최신글부터 나오게

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

# def index(request):
# posts = Post.objects.all().order_by('-pk') # 최신글이 제일 위로 나오게 하기

# return render(
# request,
# 'blog/index.html',
# {
# 'posts': posts,
# }
# )


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
# # render 함수를 통해 템플릿 폴더에서 blog 폴더의 index.html 파일을 찾아서 방문자에게 보내줌
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )
