from django.shortcuts import render
from django.db.models import Q, F, Value, Func
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
#from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from tags.models import tagged_item
from store.models import Product, OrderItem, Order, Customer

# Create your views here.
# view function takes the request and gives a response, (request handler)

def say_hello(request):

    tagged_item.objects.get_tags_for(Product, 1)

    #queryset = Customer.objects.annotate(
        #CONCAT
        #full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    #)

    #queryset = Customer.objects.annotate(
        #CONCAT
        #full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    #)

    #aggregating objects
    #result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))

    #query_set = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

     # prefetch_related when other end of relationsip has many instances
     # combined to load all product with promotions and collection
    #query_set = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # select_related when other end of relationsip has only 1 instance
    #query_set = Product.objects.select_related('collection').all()
    
    #query_set = Product.objects.only('id', 'title', 'unit_price')

    # Finding the products that have been ordered by comparing the order_id with
    # the product ID and sorting 
    #query_set = Product.objects.filter(
     #   id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')


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

    return render(request, 'hello.html', {'name': 'Carson'})