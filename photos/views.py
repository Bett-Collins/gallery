from django.shortcuts import render
from .models import Category,Image,Location
# Create your views here.
#................

def welcome(request):
    return render(request, 'welcome.html')

def gallery(request):
    category = request.GET.get('category')
    if category==None:
        photos=Image.objects.all()
    else:
        photos=Image.objects.filter(category__category_name=category)
    categories= Category.objects.all()
    context= {'categories':categories, 'photos':photos}
    
    return render(request,'gallery.html',context)

def viewPhoto(request,pk=int):
    photo=Image.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})

def about(request):
    
    return render(request,'about.html')