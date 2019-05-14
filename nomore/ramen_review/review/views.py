from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm, UserForm  
# UserForm, 
from .models import Post, Comment, Ramen, Topping, Extra, MyUser
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',  {'posts': posts})

# 회원가입


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['password_check']
            if password1 != password2:
                error = '똑같은 비밀번호를 입력해주세요'
                form = UserForm()
                return render(request, 'registration/signup.html', {'form': form, 'error': error})
            new_user = MyUser.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
        else:
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['password_check']
            if password1 != password2:
                error = '똑같은 비밀번호를 입력해주세요'
                form = UserForm()
                return render(request, 'registration/signup.html', {'form': form, 'error': error})
            error = form.errors
            form = UserForm()
            return render(request, 'registration/signup.html', {'form': form, 'error': error})
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form})

# new 부분

@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.user = request.user.get_username()
        # radio 값 입력
        post.men = request.POST['men']
        post.soup = request.POST['soup']
        post.hoke = request.POST['hoke']
        post.topping = request.POST['topping']
        post.extra = request.POST['extra']
        post.save()
        return redirect('detail', post.pk)
    else:
        ramens = Ramen.objects.all()
        toppings = Topping.objects.all()
        extras = Extra.objects.all()
        form = PostForm()
        return render(request, 'new.html', {'ramens': ramens, 'toppings': toppings, 'extras': extras, 'form': form})

# 디테일
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect('detail', post.pk)
    else:
        form = CommentForm()

        return render(request, 'detail.html', {'post': post, 'form': form})

# 디테일에 댓글 삭제
@login_required
def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    comment.delete()
    return redirect('detail', post_pk)

# 디테일 글 수정
@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('detail', post_pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})

# 디테일 글 삭제
@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

# 더보기 --> 전체 게시판


def review_list(request):
    posts = Post.objects.all()
    return render(request, 'review_list.html',  {'posts': posts})