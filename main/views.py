from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the form data
            pass
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
    
