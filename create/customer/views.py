from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm, LoginForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Profile,Location, Order
from django.contrib.auth.models import User
from django.http import JsonResponse

try:
    import folium
    FOLIUM_AVAILABLE = True
except ImportError:
    FOLIUM_AVAILABLE = False


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'customer/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'customer/login.html', {'form': form})

def dashboard(request):
    return render (request,'customer/dashboard.html')



@login_required
def profile_view(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("profile")  # Redirect to avoid duplicate form submission
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, "customer/profile.html", {"form": form})


@login_required
def Tracking(request):
    if request.method == 'POST':
        if 'item' in request.POST:
            item = request.POST['item']
            Order.objects.create(customer=request.user, item=item)
        elif 'latitude' in request.POST and 'longitude' in request.POST:
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            Location.objects.update_or_create(customer=request.user, defaults={'latitude': latitude, 'longitude': longitude})
            return JsonResponse({'status': 'Location updated'})
    
    customer = request.user
    location = Location.objects.filter(customer=customer).last()
    
    map_html = ""
    if location:
        # Generate map with folium
        m = folium.Map(location=[location.latitude, location.longitude], zoom_start=15)
        folium.Marker([location.latitude, location.longitude], popup=f"{customer.username}'s Location").add_to(m)
        map_html = m._repr_html_()
    
    return render(request, 'customer/Request.html', {'customer': customer, 'location': location, 'map_html': map_html})


def index(request):
    return render(request,'restaurant/index.html')

def about(request):
    return render(request,'restaurant/about.html')

def contact(request):
    return render(request,'restaurant/contact.html')

def product(request):
    return render(request,'restaurant/product.html')

def about2(request):
    return render(request,'restaurant2/about.html')

def book(request):
    return render(request,'restaurant2/book.html')

def index2(request):
    return render(request,'restaurant2/index.html')

def menu(request):
    return render(request,'restaurant2/menu.html')

def about3(request):
    return render(request,'restaurant3/About.html')

def blog3(request):
    return render(request,'restaurant3/blog.html')

def contact3(request):
    return render(request,'restaurant3/contact.html')

def index3 (request):
    return render(request,'restaurant3/index.html')

def service3(request):
    return render(request,'restaurant3/services.html')

def testimonial3(request):
    return render(request,'restaurant3/testimonial.html')