from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreerUtilisateur
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# ate your views here.
@login_required(login_url='acces')
def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Votre compte a été créer avec succès ' + user)
            return redirect('acces')
    context={'form':form}
    return render(request,'compte/Inscription.html',context)

def accesPage(request):
    context = {}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            return redirect('accueil')
        else:
            messages.info(request,"il y aune erreur le nom d'utilisateur et/ou le Mot de passe ")
    return render(request, 'compte/acces.html', context)

def logoutUser(request):
    logout(request)
    return redirect('acces')