from django.shortcuts import render

from post.models import Post

def main_page(request):
    post_list = Post.objects.order_by('-created_date')

    return render(request, 'main.html', {'post_list': post_list})


def detail_page(request, pk):
    post = Post.objects.get(id=pk)
    post.view_cnt += 1
    post.save()
    return render(request, 'detail.html', {'post': post})
