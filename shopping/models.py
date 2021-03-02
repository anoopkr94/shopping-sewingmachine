from django.db import models
from django.conf import settings
from django.shortcuts import reverse


class category(models.Model):
    name=models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
# category view url
    def get_absolute_url(self):
        return reverse("shopping:productcat",kwargs={'slug':self.slug})



class item(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_no = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image=models.ImageField()
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
# product detail view url
    def get_absolutep_url(self):
        return reverse("shopping:productsdet",kwargs={'slug':self.slug})

    def get_addtocart_url(self):
        return reverse("shopping:addtocart",kwargs={'slug':self.slug})

    def get_deletecartitem_url(self):
        return reverse("shopping:deletecartitem",kwargs={'slug':self.slug})

    def get_remove_cartitem_qty_url(self):
        return reverse("shopping:remove_cartitem_qty",kwargs={'slug':self.slug})



class order_item(models.Model):
    item=models.ForeignKey(item,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(order_item)
    start_date=models.DateTimeField(auto_now_add=True)
    order_date=models.DateTimeField()
    orderd=models.BooleanField(default=False)


    def __str__(self):
        return self.user.user

class cartitem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_total_item_price(self):
        return self.quantity * self.item.price


class service_register(models.Model):
    status = (("Registerd", "Registerd"),("Inspectig", "Inspectig"),("Compleated","Compleated"))


    name = models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    landmark=models.CharField(max_length=50)
    address=models.TextField()
    machine_name=models.CharField(max_length=30)
    machine_model=models.CharField(max_length=20)
    machine_Complaint=models.CharField(max_length=50)
    status=models.CharField(max_length=20,choices=status,default="Registerd")

