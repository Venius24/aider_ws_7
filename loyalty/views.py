from django.shortcuts import render
from .models import LoyaltyTransaction

def loyalty_list(request):
    transactions = LoyaltyTransaction.objects.all()
    return render(request, 'loyalty/loyalty_list.html', {'transactions': transactions})
