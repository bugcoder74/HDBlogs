# No need to define repeteadly the same context again and again
# That's why we created a context_preprocessor
# Don't forget to configure in settings.py



from .models import Category

## STEP-1

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories = categories) # Now this context dictionary will be available throughout the website once configured in the settings

## STEP-2 - Go in Settings.py to configure - inside templates - inside context_preprocessors.functionName - provide path of this file