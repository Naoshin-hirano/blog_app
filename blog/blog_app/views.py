from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import PostAddForm

# Create your views here.
def add(request):
    if request.method == "POST":
        #リクエストがPOSTなら、formの中身とユーザーを更新してレスポンス
        form = PostAddForm(request.POST, request.FILES)#FILESは画像などのファイルデータ
        if form.is_valid():
            #保存する前にどのuserの投稿か判断
            post = form.save(commit=False)#仮登録
            post.user = request.user
            #記事の内容とuserの判別に成功したら保存
            post.save()
            return redirect('blog_app:index')
    else:
        #リクエストがPOST以外なら,特になにも更新せずにレスポンスに返す
        form = PostAddForm()
    return render(request, 'blog_app/add.html', {'form': form})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_app/detail.html', {'post': post})

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/index.html', {'posts': posts})