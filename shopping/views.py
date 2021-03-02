from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import item, category, order_item, cartitem, service_register
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView


def home_view(request):
    product = item.objects.all()
    return render(request, 'index.html', {'product': product});


def about(request):
    return render(request, 'about.html');


def contact(request):
    return render(request, 'contact.html');

def register_service(request):
    if request.method =="POST":
        datas=service_register(
        name = request.POST['name'],
        email = request.POST['email'],
        phone = request.POST['phone'],
        landmark = request.POST['landmark'],
        address = request.POST['address'],
        machine_name = request.POST['machine_name'],
        machine_model = request.POST['machine_model'],
        machine_Complaint = request.POST['machine_Complaint'])
        datas.save()

    return render(request,'register_service.html')

def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['username']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email, first_name=name)
                user.save()
                return redirect("shopping:login")

    return render(request, 'register.html');


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'index.html')
        else:
            messages.info(request,'invalid username or password')
    return render(request, 'login.html');



def logout(request):
    auth.logout(request)
    return redirect('/')

#all product view
class productview(ListView):
    model = item
    template_name = "product.html"

# category based view
class catcegoryview(ListView):
    def get(self, *args, **kwargs):
        cat = category.objects.filter(slug=self.kwargs['slug'])
        for c in cat:
            name=c.id
        items=item.objects.filter(category=name)
        context = {
            'object_list': items,
        }

        return render(self.request,"product.html", context)

# product details
class product_detailview(DetailView):
    model = item
    template_name = "productdet.html"


@login_required(login_url='shopping:login')
def addtocart(request,slug):
    products = get_object_or_404(item, slug=slug)
    orderitem, created = cartitem.objects.get_or_create(item=products,user=request.user)

    if cartitem.objects.filter(item__slug=products.slug, user=request.user).exists():
        orderitem.quantity +=1
        orderitem.save()
    else:

        cart=cartitem.objects.create(user=request.user)
        cart.item.add(orderitem)
    messages.info(request, 'cart item ADD')

    return redirect("shopping:cart")


def deletecartitem(request,slug):
    products = get_object_or_404(item, slug=slug)
    cartitem.objects.filter(item=products, user=request.user).delete()

    messages.info(request, 'cart item deleted')
    return redirect('shopping:cart')

def remove_cartitem_qty(request,slug):
    products = get_object_or_404(item, slug=slug)
    orderitem = cartitem.objects.get(item=products, user=request.user)

    if cartitem.objects.filter(item__slug=products.slug, user=request.user).exists():
        orderitem.quantity -= 1
        orderitem.save()
        if orderitem.quantity==0:
            cartitem.objects.filter(item=products, user=request.user).delete()

    messages.info(request, 'cart item deleted')
    return redirect('shopping:cart')


class cartview(View):
    def get(self, *args, **kwargs):
        items=cartitem.objects.filter(user=self.request.user)

        return render(self.request,"shopping-cart.html",{'items':items})

