from django.shortcuts import render, get_object_or_404
from .models import Wishlist
from datetime import datetime
from .forms import ProductForm



# Create your views here.


def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {"title": "wishlist i about project"})


def list_page(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST)
        instance_product = form.save()
        wishlist.product.add(instance_product)
        wishlist.save()
    else:
         form = ProductForm()
    return render(
        request,
        "wish_list.html",
        {
            "wishlist": wishlist,
            "is_owner_list": wishlist.owner == request.user
        }
    )



