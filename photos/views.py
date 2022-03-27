from django.shortcuts import render,redirect
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

def addPhoto(request):
    categories= Category.objects.all()

    if request.method == 'POST':
        data=request.POST
        image=request.FILES.get('image')

        if data['category']!='none':
            category=Category.objects.get(id=data['category'])

        elif data['category_new']!='':
            category, created=Category.objects.get_or_create(name=data['category_new'])
        else:
            category=None

        photo = Image.objects.create(
            category=category,
            description=data['description'],
            image=image
        )
        return redirect('gallery')