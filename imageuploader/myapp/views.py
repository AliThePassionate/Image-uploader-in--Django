from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        # Fetch all images after saving the form
        img = Image.objects.all()
        return render(request, 'myapp/home.html', {'form': form, 'img': img, 'success': True})
    else:
        form = ImageForm()  # Create an empty form for GET request
        img = Image.objects.all()  # Fetch all images to display

    return render(request, 'myapp/home.html', {'form': form, 'img': img})
