from django.shortcuts import render
from django.db.models import Q, F
#from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

# Create your views here.
# view function takes the request and gives a response, (request handler)

def say_hello(request):

    # Finding the products that have been ordered by comparing the order_id with
    # the product ID and sorting 
    query_set = Product.objects.filter(
        id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')


    # .values returns dictionary objects {.., .., ..}
    # values_list gives us tuple objects
    #query_set = Product.objects.values('id', 'title', 'collection__title')

    #slicing and limiting results, displays product 5,6,7,8,9
    #query_set = Product.objects.all()[5:10]

    # sorting by unit price ascending and title descending
    #query_set = Product.objects.order_by('unit_price','-title')

    # search for specific field in class
    # query_set = Product.objects.filter(collection__id__range=(1, 3))

    # string - query_set = Product.objects.filter(title__icontains='coffee')


    # Products: inventory < 10 OR price < 20
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    # comparing two fields with F objects
    #query_set = Product.objects.filter(inventory=F('unit_price'))
    
    
    
    #try:
     #   product = Product.objects.get(pk=0)
   # except ObjectDoesNotExist:
   #     pass

#return none if the query set is empty
 #  product = Product.objects.filter(pk=0).first()

# provides boolean value if object exists or not        
#   product = Product.object.filter(pk=0).exists()

    return render(request, 'hello.html', {'name': 'Carson', 'products': list(query_set)})