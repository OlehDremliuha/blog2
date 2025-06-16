from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Post, Comment, Profile
import datetime

currentUserId = None

def getIndex(request):

    posts = Post.objects.all()

    return render(request, "index.html", {"posts": posts})



def getLogin(request):

    global currentUserId

    if request.method == "POST":
        
        userName = request.POST['name']
        userPassword = request.POST['password']

        user = authenticate(request, username=userName, password=userPassword)

        if user is not None:
            currentUserId=user.id
            login(request, user)
            return redirect('/')
        else:

            return render(request, "login.html", {"error": "Невірні данні для входу"})
    else:

        return render(request, "login.html")


def getLogup(request):

    global currentUserId

    if request.method == "POST":
        
        if request.POST['password'] == request.POST['password2']:
        
            userName = request.POST['name']
            userMail = request.POST['email']
            userPassword = request.POST['password']

            user = User.objects.create_user(userName, userMail, userPassword)

            user.save()

            profile = Profile(userId=user)
            profile.save()

            user = authenticate(request, username=userName, password=userPassword)

            currentUserId=user.id
            
            login(request, user)
            return redirect('/')
        else:

            return render(request, "login.html", {"error": "Невірні данні для входу"})
        
    else:

        return render(request, "logup.html")



@login_required
def getLogout(request):
    global currentUserId
    logout(request)
    currentUserId = None
    return redirect('login')














@login_required
def createPost(request):
    global currentUserId

    if request.method == "POST":
            

            Title = request.POST['title']
            Text = request.POST['text']
            Image = request.FILES['image']
            user=User.objects.get(id=currentUserId)

            post = Post(userId=user, title=Title, text=Text, image=Image)

            post.save()

            return redirect('/')
        
    else:

        return render(request, 'createPostForm.html')
    

@login_required
def addComment(request):
    global currentUserId

    if request.method == "POST":

        postId = request.POST['postId']
        post = Post.objects.get(id=postId)
        user = User.objects.get(id=currentUserId)
        comentText = request.POST['comentText']
        comentDate = datetime.datetime.now()

    comment = Comment(postId=post, userId=user, text=comentText, date=comentDate)
    comment.save()

    return redirect('article', post.id)
    



def postView(request, pk):

    post = Post.objects.filter(id=pk).first
    comments = Comment.objects.all().filter(postId=pk).order_by("-date")

    return render(request, "post.html", {"post": post, "comments": comments})





def getProfile(request, id):
    user = User.objects.get(id=id)
    userProfile = Profile.objects.get(userId=user)
    posts = Post.objects.filter(userId=user)

    return render(request, "profile.html", {"userProfile": userProfile, "posts": posts})



def editProfile(request, id):
    user = User.objects.get(id=id)
    userProfile = Profile.objects.get(userId=user)

    if request.method == "POST":

        if 'userName' in request.POST.keys():
            
            user.username = request.POST['userName']
            user.save()

            return redirect(request.path)


        elif 'userMail' in request.POST.keys():
            
            user.email = request.POST['userMail']
            user.save()

            return redirect(request.path)

        elif 'password' in request.POST.keys() and 'passwordValid' in request.POST.keys():

            if request.POST['password'] == request.POST['passwordValid']:
                user.set_password(request.POST['password'])
                user.save()
                return redirect(request.path)
            else:
                error = "Passwords must match"
                return render(request, "edit.html", {"userProfile": userProfile, "error": error})
    else:

        return render(request, "edit.html", {"userProfile": userProfile})
    


def changeAvatar(request, id):

        user = User.objects.get(id=id)
        profile = Profile.objects.get(userId=user)

        profile.avatar = request.FILES['avatar']
        profile.save()

        return redirect('profile', id)


def changeBio(request, id):

        user = User.objects.get(id=id)
        profile = Profile.objects.get(userId=user)

        profile.bio = request.POST['bio']
        profile.save()

        return redirect('profile', id)



def deletePost(request, id):

    post = Post.objects.get(id=id)

    post.delete()

    return redirect('main')