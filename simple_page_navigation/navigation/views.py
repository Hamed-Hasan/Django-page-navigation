from django.shortcuts import render
from datetime import datetime
# Create your views here.

def about(request):
    # Data to be passed to the template
    context = {
        'page_title': 'About Page',
        'content': 'This is the about page content.',
         'current_date': datetime.now(),
    }
    return render(request, 'navigation/about.html', context)

def contact(request):
    return render(request, 'navigation/contact.html')