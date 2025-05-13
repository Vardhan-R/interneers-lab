# urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.routers import DefaultRouter
from inventory import views

# router = DefaultRouter()
# router.register("", views.ProductViewSet)

def create_product_form(request):
    return render(request, "create_prod.html")

def hello_name(request):
    """
    A simple view that returns 'Hello, {name}' in JSON format.
    Uses a query parameter named 'name'.
    """
    # Get 'name' from the query string, default to 'World' if missing
    name = request.GET.get("name", "World")
    return JsonResponse({"message": f"Hello, {name}!"})

def hello_world(request):
    return HttpResponse("Testing by Vardhan.")
    # return HttpResponse("Hello, world! This is our interneers-lab Django server.")

def redirect_to_home(request):
    return redirect("/home")

def show_home(request):
    return render(None, "home.html")

def show_products(request):
    return render(request, "show_prods.html")

def update_product_form(request):
    return render(request, "update_prods.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("hello/", hello_world),
    path("hello/", hello_name),
    # Example usage: /hello/?name=Bob
    # returns {"message": "Hello, Bob!"}
    # path("", include(router.urls)),
    path("", redirect_to_home),
    path("home/", show_home),
    # path("show_products/", show_products),
    # path("show_products/", include(router.urls)),
    path("show_products/", views.ProductList.as_view()),
    path("create_product/", create_product_form),
    path("cp/", views.ProductCreate.as_view()),
    path("search_product/", views.ProductDetail.as_view()),
    path("delete_product/", views.ProductDelete.as_view()),
    path("update_product/", update_product_form),
    path("up/", views.ProductUpdate.as_view()),
]
