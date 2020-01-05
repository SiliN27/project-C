from django.shortcuts import render
from user_profile.forms import ProductForm, ReviewForm
from user_profile.models import Product, productReview
from profile_page.models import Farmer
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from user_profile.models import productReview
# Create your views here.


def user_profile(request):
    template_name = 'user_profile/product.html'
    form = ProductForm()

    form2 = ReviewForm()
    if request.method == "POST":
        form2 = ReviewForm(request.POST)
        if form2.is_valid():
            title = form2.cleaned_data['review_title']
            message = form2.cleaned_data['review_message']
            id = request.POST['prodId']
            print(id)
            saving = productReview(review_title=title, review_message=message, review_product=id)
            saving.save()

    search = {"Vegetable": ["Mais", "Peach", "Brocolli", "Carrot", "Tomato"],
              "Fruit": ["Banana", "Kiwi","Apple","Strawberry"]}
    context = {'product': Product.objects.all(), 'review': productReview.objects.all(), "data": search,'navigation':'products', 'form': form, 'reviewform':form2}
    return render(request, template_name, context)


def category_products(request):
    category = request.GET.get("category")
    if category == "Vegetable":
        category = ["Mais", "Peach", "Brocolli",
                    "Carrot", "Tomato"]
        result = Product.objects.filter(product_name__in=category)

    elif category == "Fruit":
        category = ["Banana", "Kiwi", "Apple","Strawberry",]
        result = Product.objects.filter(product_name__in=category)
        pass

    else:
        result = Product.objects.filter(product_name__istartswith=category)

    # if len(result) == 0:
    #     available = f"There are no {category} products available"
    # "available":available

    return render(request, 'user_profile/product.html', {"result": result})


def search_product(request):
    template = 'user_profile/product.html'
    query_product = request.GET.get("query")
    if query_product:
        result = Product.objects.filter(product_name__startswith=query_product)
        # if len(result) < 1:
        #     empty = True
        # else:
        #     empty = False
        # "empty:empty"
    return render(request, template, {"result": result})


def add_product(request):
    form = ProductForm()
    template_name = 'user_profile/add_product.html'
    return render(request, template_name, {'form': form})


def delete_product(request, id):
    template_name = "farmer_page/my_products.html"
    product = Product.objects.get(pk=id)
    product.delete()
    # product.delete(pk=id)
    products = Product.objects.filter(product_user=request.user)

    return render(request, template_name, {"product": products})


def post_product(request):
    form = ProductForm()
    template_name = 'user_profile/add_product.html'
    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(form.errors)
        if form.is_valid():
            name = form.cleaned_data['product_name'].capitalize()
            description = form.cleaned_data['product_description']
            price = form.cleaned_data['product_price']
            image = request.FILES['product_picture']
            user = request.user
            print(user)
            product = Product(product_name=name, product_description=description,
                              product_price=price, product_user=user, product_picture=image)
            product.save()
            return render(request, 'user_profile/product.html', {'product': Product.objects.all()})
        else:
            form = ProductForm()
    return render(request, template_name, {'form':form})

def review_product(request):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['review_title']
            message = form.cleaned_data['review_message']


    return render(request, 'user_profile/product.html', {'reviews':reviews, 'reviewform':form})      
