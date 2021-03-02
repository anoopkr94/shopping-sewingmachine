from django.utils.safestring import mark_safe
from shopping.models import category, cartitem
from django import template

register = template.Library()


@register.simple_tag
def categories():
    items = category.objects.all()
    items_li = ""
    for i in items:
        items_li += """<a href="/products/{}">{}</a>""".format(i.slug, i.name)
    return mark_safe(items_li)


@register.filter
def cart_items(user):
    items = cartitem.objects.filter(user=user)
    li = ""
    total=0

    for i in items:

        li += """<tr>
                    <td><img src="{}" width="200" height="250" alt=""></td>
                    <td><h5>{}</h5></td>
                    <td >{} X {}</td>
                    
                    </tr>""".format(i.item.image.url,i.item.name,i.item.price,i.quantity)

        total += i.item.price * i.quantity
    li +="""<tr style="color:red">
    <td colspan="3" >Total = {}</td>""".format(total)
    return mark_safe(li)


@register.filter
def cart_items_count(user):
    items = cartitem.objects.filter(user=user)
    count = 0
    for i in items:
        count+=i.quantity
    return mark_safe(count)

