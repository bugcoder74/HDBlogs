from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Category, Blog

def posts_by_category(request, category_id):
    # category)id comes from the url, e.g. url .../category/6 => category_id=6
    # Fetching the posts of a particular id
    posts = Blog.objects.filter(status='Published', category=category_id)
    #category = Category.objects.get(pk=category_id) # pk == primary key, get => get one value, all => get all
    #Above line will raise error when category not exist - like category/1000 - so better write above line as
    #category = get_object_or_404(Category, pk=category_id) # Now no error - just a 404 page

    # We want to redirect to home page instead so using this method

    try:
        category = Category.objects.get(pk=category_id)
    except:
        # Redirecting to the Home Page
        return redirect('home')

    context = {
        'posts' : posts,
        'category' : category,
    }
    return render(request, 'post_by_category.html', context)
