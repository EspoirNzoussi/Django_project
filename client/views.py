from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required


@login_required(login_url='acces')
def list_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_totol=commande.count()
    myFilter = CommandeFiltre(request.GET, queryset=commande)
    commande=myFilter.qs
    context={'client':client, 'commande':commande,'commande_totol':commande_totol,'myFilter':myFilter}
    return render(request,'client/list_client.html',context)
