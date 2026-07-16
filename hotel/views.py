from django.shortcuts import render, HttpResponse, redirect
from .models import register as RegisterModel

# Create your views here.

def index(request):
    from admin_app.models import GalleryImage, News, HeroImage
    gallery_images = GalleryImage.objects.all()
    news_items = News.objects.all().order_by('-date')
    hero_image = HeroImage.objects.order_by('-id').first()
    return render(request, 'index.html', {
        'gallery_images': gallery_images,
        'news_items': news_items,
        'hero_image': hero_image
    })

def login_view(request):
    if request.method == "POST":
        usermail = request.POST.get("usermail")
        userpassword = request.POST.get("userpassword")
        if usermail == 'admin@gmail.com' and userpassword == 'admin':
            request.session['email'] = usermail
            request.session['name'] = 'admin'
            return redirect('admin_dashboard')
        else:
            error_message = "Only admin can log in."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('index')

def register(request):
    import datetime
    today = datetime.date.today().isoformat()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        date = request.POST.get('date', '').strip()
        time = request.POST.get('time', '').strip()
        people = request.POST.get('people', '').strip()
        message = request.POST.get('message', '').strip()
        errors = {}
        if not name:
            errors['name'] = 'Name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not phone:
            errors['phone'] = 'Phone number is required.'
        elif not phone.isdigit() or len(phone) != 10:
            errors['phone'] = 'Phone number must be exactly 10 digits.'
        if not date:
            errors['date'] = 'Date is required.'
        if not time:
            errors['time'] = 'Time is required.'
        if not people:
            errors['people'] = 'Number of people is required.'
        else:
            try:
                if int(people) < 1:
                    errors['people'] = 'At least 1 person is required.'
            except ValueError:
                errors['people'] = 'Number of people must be a number.'
        if not message:
            errors['message'] = 'Special requests field is required.'

        if errors:
            return render(request, 'register.html', {
                'errors': errors,
                'name': name,
                'email': email,
                'phone': phone,
                'date': date,
                'time': time,
                'people': people,
                'message': message,
                'today': today
            })

        RegisterModel.objects.create(name=name, email=email, phone=phone, date=date, 
        time=time, people=people, message=message)
        success_message = 'Your reservation has been submitted successfully!'
        return render(request, 'register.html', {'success_message': success_message})
    return render(request, 'register.html')

