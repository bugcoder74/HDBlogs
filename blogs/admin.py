from django.contrib import admin
from .models import Category,Blog


class BlogAdmin(admin.ModelAdmin):   # Since we are auto generating slug for the Bolg Model - so the class name must be BlogAdmin
    prepopulated_fields = {'slug':('title',)} # This line will auto type slug as we type the title
    list_display = ('title', 'category', 'author', 'status', 'is_featured') # Makes the admin panel of Model Blog look like table
    search_fields = ('id', 'title', 'category__category_name', 'status') # Adds a search bar in admin panel where we can search Blog table by rows specified as arguments 
    #                                       ^
    # Since category was a foreign key - so writing just category in serach bar gives error, so we want cateogry jiska foreign key h uska category_name se search kiya ja sake, so write category__category name 

    list_editable = ('is_featured',) # Means is_featured can be edited by direct checking at table - need not go inside edit option to edit

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin) # BlogAdmin passed since we want slug to be auto filled as we fill the title

