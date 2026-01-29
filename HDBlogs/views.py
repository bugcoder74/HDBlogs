from django.http import HttpResponse
from django.shortcuts import render, redirect

from blogs.models import Category, Blog
from .forms import RegistrationForm

from django.contrib.auth.forms import AuthenticationForm # Provided by the django
from django.contrib import messages, auth

def home(request):
    #return HttpResponse("<H2> Welcome, this is the Home Page</H2>")

    #Fetching Data to be displayed from database
    # categories = Category.objects.all() # Will fetch all the Categories - no need since did in context_processors
    #print(categories) e.g.   <QuerySet [<Category: Sports>, <Category: Politics>, <Category: Science>, <Category: Health>, <Category: Business>, <Category: Technology>]>
    
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at') # Pick all those entries where is_featured = True
    normal_posts = Blog.objects.filter(is_featured=False, status='Published')

    context = {
        # 'categories' : categories, since we already did it in context processors so no need
        'featured' : featured_posts,
        'posts' : normal_posts,
    }
    
    return render(request, 'home.html', context)



def register(request): # Same method handling both POST method by register from sunmit button and GET for /register url
    print(request)
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        print("The form is ", form)
        if form.is_valid(): # Data Validation
            form.save()
            #messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            print("=======Errors===========",form.errors)
            context = {
                'form' : form,
                'message' : "There was some error - please fill the form again"
            }
            #messages.error(request, "There was an error registering, please fix the problems below..")
            return render(request, 'register.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,

        }
        return render(request, 'register.html', context)

def login(request):
    if (request.method=="POST"):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("Password",password)

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
        else:
            context={
                'form' : form,
                'message' : "Invalid Credentials, Can't Sign In.."
            }
            return render(request, 'login.html', context)
    else:
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')