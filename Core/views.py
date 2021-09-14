from django.shortcuts import render
from Product.models import Product, category

# Create your views here.


def Home(request):

    # Get Last Products Fore Show In New Products Part
    LastProductCount = Product.objects.all().count()
    if LastProductCount > 10:
        LastProduct = Product.objects.order_by('-Date')[:10]
    else:
        LastProduct = Product.objects.order_by('-Date')[:LastProductCount]

    # Get Top Categories For Showing On Top
    TopCategories = category.objects.filter(AddToTop = True)

    # Get All Categories For Show In Search Box And ... 
    AllCategories = category.objects.all()

    # Get Categories That Should Be Displayed In The Category List
    DisplayCategories = category.objects.filter(AddToListCategory = True)

    var = {
        '10LastProductList':LastProduct,
        'TopCategories':TopCategories,
        'AllCategories':AllCategories,
        'DisplayCategories':DisplayCategories,
    }
    return render(request,'Core/index.html',var)