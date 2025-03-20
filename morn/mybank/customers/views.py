from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from customers.models import Customer
from .models import Customer

cust_data = [
    {
        'name': 'abcd',
        'acnum': 1234,
        'balance': 11.22,
    },
    {
        'name': 'pqrs',
        'acnum': 1111,
        'balance': 222.33,
    },
    {
        'name': 'wxyz',
        'acnum': 3333,
        'balance': 4444.55,
    }
]


# Create your views here.
def list_customers(request):
    # return HttpResponse('Hello world!')
    if request.method == 'GET':
        # return JsonResponse(cust_data, safe=False)
        cust_data = list(Customer.objects.all().values())
        return render(request, 'customers.html', {'cust_data': cust_data})
    elif request.method == 'POST':
        print(request.POST)
        return HttpResponse('')


def list_customer(request, id):
    # return HttpResponse('Hello world!')
    # return JsonResponse(cust_data[id], safe=False)
    # customer_data = cust_data[id]
    customer_data = Customer.objects.filter(acnum=id).values().get()
    customer_data['id'] = id
    return render(request, 
        'customer.html', 
        # {'id': id, 'name': customer_data['name'], 'acnum': customer_data['acnum'], 'balance': customer_data['balance']})
        # {'data': customer_data})
        customer_data)

        # {'data': {
        #    'name': 'wxyz',
        #    'acnum': 3333,
        #    'balance': 4444.55,
        # }
