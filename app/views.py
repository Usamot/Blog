from django.shortcuts import render, redirect
from app.models import Blog
from .forms import Blog3Form, UserSignupForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def RegisterUser(request):

    form = UserSignupForm

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('LoginPageUrl') 

    return render(request, 'register.html', {'form': form})


def LoginUser(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HomePageurl')  # Redirect to the home page or any other page after login
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    # return render(request, 'login.html')

def LogOutUser(request):
    logout(request)
    return redirect('/') 


def LandingPage(request):
    user = request.user

    print('\n\n\===============================')
    print(user)
    print('===============================\n\n')

    blogs=Blog.objects.all()

    context ={
        "allblog" : blogs
    }
    return render(request,'landingPage.html', context)


def AddPage(request):

    form = Blog3Form()

    if request.method == 'POST':
        form = Blog3Form(request.POST)
        if form.is_valid:
           form.save()
           return redirect('HomePageurl')



    context ={
        'myform': form
    }

    return render(request, 'addPage.html', context)

def ViewMorePage(request,pk):

    blog =Blog.objects.get(id=pk)

    print('\n\n')
    print(blog)
    print('\n\n')

    context ={
        'myBlog' : blog
    }


    return render(request,'viewMorePage.html', context)



def EditMorePage(request, pk):
    blog =Blog.objects.get(id=pk)


    form = Blog3Form(instance=blog)

    if request.method == 'POST':
        print('\n\n')
        print('method == post')
        print(request.POST)
        print('\n\n')
        form = Blog3Form(request.POST, instance=blog)
            
        if form.is_valid():
            form.save()
            return redirect('ViewMorePageurl',blog.id)



    context ={
            'myform': form,
            'myBlog' : blog
        }

        
    return render(request, 'editPage.html', context)


def DeleteSinglePage(request, pk):
    blog =Blog.objects.get(id=pk)

    blog.delete()
    return redirect('HomePageurl')

# def FilterPage(request):

#     return render(request,'filterPage.html')
