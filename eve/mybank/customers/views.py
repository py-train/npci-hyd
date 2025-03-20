from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Customer 

import json

cust_data = [
    {
        'name': 'abcd',
        'id': 12,
        'sex': 'M'
    },
    {
        'name': 'pqrs',
        'id': 22,
        'sex': 'F'
    },
    {
        'name': 'xyzz',
        'id': 41,
        'sex': 'F'
    }
]


# Create your views here.
def list_customers(request, cust_id=None):
    if request.method == 'GET':
        if cust_id==None:
            # qs = Customer.objects.all().values()
            # rdata = list(qs)
            qs = Customer.objects.all()
        else:
            pass
            # qs = Customer.objects.filter(id=cust_id).values()
            # qs = Customer.objects.filter(id=cust_id).values()
            # rdata = list(qs)

        # return JsonResponse(rdata, safe=False)
        return render(request, 'customers.html', {'cust_data': qs})
    elif request.method == 'POST':
        # print(request.POST)
        # data = request.POST.get('data', {})
        # cust_data.append(data)
        customer = json.loads(request.body)
        Customer(**customer).save()
        return HttpResponse('')

disbursals = [
    ('abcd', 123),
    ('pqrs', 444),
    ('xyz', 999)
]

recoveries = [
    ('abcd', 10),
    ('pqrs', 44),
    ('xyz', 111)
]


def loans(request):
    return render(request, 
    'loans.html', 
    {'disbursals': disbursals, 'recoveries': recoveries})
