from django.views.decorators.http import require_POST
# Toggle main image for category
@require_POST
def category_toggle_main(request, pk):
    category = get_object_or_404(Category, id=pk)
    # Set all other categories' image_main to False if this is being set to True
    if not category.image_main:
        Category.objects.filter(main_category=category.main_category).update(image_main=False)
        category.image_main = True
    else:
        category.image_main = False
    category.save()
    return redirect('category_list')
# --- MenuItem CRUD ---
# def menuitem_list(request):
#     menuitems = MenuItem.objects.select_related('category', 'category__main_category').all()
#     return render(request, 'menuitem_list.html', {'menuitems': menuitems})

# def menuitem_add(request):
#     categories = Category.objects.select_related('main_category').all()
#     if request.method == 'POST':
#         category_id = request.POST.get('category')
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         if category_id and name and price:
#             category = get_object_or_404(Category, id=category_id)
#             MenuItem.objects.create(category=category, name=name, price=price, description=description)
#             return redirect('menuitem_list')
#     return render(request, 'menuitem_add.html', {'categories': categories})

# def menuitem_edit(request, pk):
#     obj = get_object_or_404(MenuItem, id=pk)
#     categories = Category.objects.select_related('main_category').all()
#     if request.method == 'POST':
#         category_id = request.POST.get('category')
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         if category_id and name and price:
#             obj.category = get_object_or_404(Category, id=category_id)
#             obj.name = name
#             obj.price = price
#             obj.description = description
#             obj.save()
#             return redirect('menuitem_list')
#     return render(request, 'menuitem_edit.html', {'menuitem': obj, 'categories': categories})

# def menuitem_delete(request, pk):
#     obj = get_object_or_404(MenuItem, id=pk)
#     obj.delete()
#     return redirect('menuitem_list')
# --- Category CRUD ---
def category_list(request):
    categories = Category.objects.select_related('main_category').all()
    return render(request, 'category_list.html', {'categories': categories})

def category_add(request):
    maincategories = MainCategory.objects.all()
    if request.method == 'POST':
        main_category_id = request.POST.get('main_category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        if main_category_id and name:
            main_category = get_object_or_404(MainCategory, id=main_category_id)
            category = Category(
                main_category=main_category,
                name=name,
                price=price if price else None,
                description=description if description else None,
                image=image if image else None
            )
            category.save()
            return redirect('category_list')
    return render(request, 'category_add.html', {'maincategories': maincategories})

def category_edit(request, pk):
    obj = get_object_or_404(Category, id=pk)
    maincategories = MainCategory.objects.all()
    if request.method == 'POST':
        main_category_id = request.POST.get('main_category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        if main_category_id and name:
            obj.main_category = get_object_or_404(MainCategory, id=main_category_id)
            obj.name = name
            obj.price = price if price else None
            obj.description = description if description else None
            if image:
                obj.image = image
            obj.save()
            return redirect('category_list')
    return render(request, 'category_edit.html', {'category': obj, 'maincategories': maincategories})

def category_delete(request, pk):
    obj = get_object_or_404(Category, id=pk)
    obj.delete()
    return redirect('category_list')
from django.shortcuts import render, HttpResponse, get_object_or_404
from hotel.models import register as RegisterModel
from .models import GalleryImage, HeroImage, News, MainCategory, Category, MenuItem
# --- MainCategory CRUD ---
from django.shortcuts import redirect

def maincategory_list(request):
    maincategories = MainCategory.objects.all()
    return render(request, 'maincategory_list.html', {'maincategories': maincategories})

def maincategory_add(request):
    error = None
    if request.method == 'POST':
        heading = request.POST.get('heading')
        image = request.FILES.get('image')
        if heading:
            if MainCategory.objects.filter(heading=heading).exists():
                error = 'This main category already exists.'
            else:
                MainCategory.objects.create(heading=heading, image=image if image else None)
                return redirect('maincategory_list')
    return render(request, 'maincategory_add.html', {'error': error})

def maincategory_edit(request, pk):
    obj = get_object_or_404(MainCategory, id=pk)
    if request.method == 'POST':
        heading = request.POST.get('heading')
        if heading:
            obj.heading = heading
            obj.save()
            return redirect('maincategory_list')
    return render(request, 'maincategory_edit.html', {'maincategory': obj})

def maincategory_delete(request, pk):
    obj = get_object_or_404(MainCategory, id=pk)
    obj.delete()
    return redirect('maincategory_list')

# Create your views here.

def menu_page(request):
    from .models import MainCategory, GalleryImage
    maincategories = MainCategory.objects.prefetch_related('categories').all()
    gallery_images = GalleryImage.objects.all()
    return render(request, 'menu_page.html', {'maincategories': maincategories, 'gallery_images': gallery_images})

# Book table view for admin_app
def book_table(request):
    reservations = RegisterModel.objects.all()
    return render(request, 'book_table.html', {'reservations': reservations})

def delete_reservation(request, reservation_id):
    RegisterModel.objects.filter(id=reservation_id).delete()
    return render(request, 'book_table.html', {'reservations': RegisterModel.objects.all()})
 
def admin_dashboard(request):
    reservation_count = RegisterModel.objects.count()
    return render(request, 'admin_dashboard.html', {'reservation_count': reservation_count})

def load_admin_app(request):
    return HttpResponse("Admin App Loaded")

def admin_news_list(request):
    news_items = News.objects.all()
    return render(request, 'admin_news_list.html', {'news_items': news_items})

def admin_news_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            News.objects.create(title=title, content=content)
            return render(request, 'admin_news_add.html', {'success': True})
    return render(request, 'admin_news_add.html')

def admin_news_edit(request, pk):
    news_obj = get_object_or_404(News, id=pk)
    if request.method == 'POST':
        news_obj.title = request.POST.get('title')
        news_obj.content = request.POST.get('content')
        news_obj.save()
        return render(request, 'admin_news_edit.html', {'news': news_obj, 'success': True})
    return render(request, 'admin_news_edit.html', {'news': news_obj})

def admin_news_delete(request, pk):
    news_obj = get_object_or_404(News, id=pk)
    news_obj.delete()
    return render(request, 'admin_news_list.html', {'news_items': News.objects.all(), 'deleted': True})
def admin_hero_list(request):
    images = HeroImage.objects.all()
    return render(request, 'admin_hero_list.html', {'images': images})

def admin_hero_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # Use fixed values for headline and subheadline
            HeroImage.objects.create(
                image=image,
                headline='BOLD TASTE OF KERALA',
                subheadline='Now in Hounslow'
            )
            return render(request, 'admin_hero_add.html', {'success': True})
    return render(request, 'admin_hero_add.html')

def admin_hero_edit(request, pk):
    image_obj = get_object_or_404(HeroImage, id=pk)
    if request.method == 'POST':
        if 'image' in request.FILES:
            image_obj.image = request.FILES['image']
        image_obj.title = request.POST.get('title')
        image_obj.subtitle = request.POST.get('subtitle')
        image_obj.save()
        return render(request, 'admin_hero_edit.html', {'image': image_obj, 'success': True})
    return render(request, 'admin_hero_edit.html', {'image': image_obj})

def admin_hero_delete(request, pk):
    image_obj = get_object_or_404(HeroImage, id=pk)
    image_obj.delete()
    return render(request, 'admin_hero_list.html', {'images': HeroImage.objects.all(), 'deleted': True})
def admin_gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'admin_gallery_list.html', {'images': images})

def admin_gallery_add(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        description = request.POST.get('description')
        if image:
            GalleryImage.objects.create(image=image, caption=caption, description=description)
            return render(request, 'admin_gallery_add.html', {'success': True})
    return render(request, 'admin_gallery_add.html')

def admin_gallery_edit(request, pk):
    image_obj = get_object_or_404(GalleryImage, id=pk)
    if request.method == 'POST':
        if 'image' in request.FILES:
            image_obj.image = request.FILES['image']
        image_obj.caption = request.POST.get('caption')
        image_obj.description = request.POST.get('description')
        image_obj.save()
        return render(request, 'admin_gallery_edit.html', {'image': image_obj, 'success': True})
    return render(request, 'admin_gallery_edit.html', {'image': image_obj})

def admin_gallery_delete(request, pk):
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    try:
        image_obj = GalleryImage.objects.get(id=pk)
        image_obj.delete()
        return HttpResponseRedirect(reverse('admin_gallery_list') + '?deleted=1')
    except GalleryImage.DoesNotExist:
        return HttpResponseRedirect(reverse('admin_gallery_list') + '?notfound=1')
