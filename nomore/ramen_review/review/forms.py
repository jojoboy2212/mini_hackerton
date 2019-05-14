from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comment, Post, MyUser


# 로그인아웃
class UserForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'password_check', 'age', 'name']
        labels = {
            'username' : '아이디',
            'password' : '비밀번호',
            'email' : '이메일 주소',
            'password_check' : '비밀번호 확인',
            'name' : '이름',
            'age' : '나이',
        }

        widgets={
            'username' : forms.Textarea(attrs={'class':'username_form', 'rows' : '1'}),
            'password' : forms.PasswordInput(attrs={'class':'password_form', 'rows' : '1'}),
            'email' : forms.Textarea(attrs={'class':'email_form', 'rows' : '1'}),
            'password_check' : forms.PasswordInput(),
        }
# class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
#     email = forms.EmailField(required=True) # 이메일 필드 추가
    
#     class Meta:
#         model = User
#         fields = ("username", "password", "email")
#         labels = {
#             'username' : '아이디',
#             'password' : '비밀번호',
#             'email' : '이메일 주소',
#         }
#         widgets={
#             'username' : forms.Textarea(attrs={'class':'username_form', 'rows' : '1'}),
#             'password' : forms.PasswordInput(attrs={'class':'password_form', 'rows' : '1'}),
#             'email' : forms.Textarea(attrs={'class':'email_form', 'rows' : '1'}),
#         }
#     def save(self, commit=True): # 저장하는 부분 오버라이딩
#         user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'age', 'password_check')
#         labels={
#             'username' : '아이디',
#             'password' : '비밀번호',
#             'password_check' : '비밀번호 확인',
#             'age' : '나이',
            
#         }
#         widgets = {
#             'username' : forms.Textarea(attrs={'class':'username_form', 'rows' : '1'}),
#             'password' : forms.PasswordInput(attrs={'class':'password_form', 'rows' : '1'})
           
#         }



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'img', 'content')
        labels ={
            'title' : '',
            'img' : '사진',
            'content' : '',
        }

        widgets={
            'title' : forms.Textarea(attrs={'class':'title_form', 'rows' : '1'}),
            'content' : forms.Textarea(attrs={'class':'content_form', 'rows' : '10'}),
            
        }

# Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('score', 'addcontent', )  # --> comment 뷰 detail에 추가해야함

        labels = {
            'score' : '점수',
            'addcontent' : '댓글'
        }

        widgets={
            'addcontent' : forms.Textarea(attrs={'class':'title_form', 'rows' : '1', 'default' : '댓글을 입력해주세요..'}),
        }

