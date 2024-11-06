from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Collec
from .forms import CollecForm

# Create your views here.

def about(request):
    return render(request,"./about.html")

def collection_detail(request, id):
    #Récupérer l'objet collec correspondant à l'ID ou renvoyer une erreur 404 si non trouvé 
    collection= get_object_or_404(Collec, id=id)
    return render(request,'./collection_detail.html', {'collection':collection})

def collection_list(request):
    collections = Collec.objects.all()
    return render(request, './collection_list.html', {'collections':collections})

def add_collection(request):
    if request.method == 'POST':
        form=CollecForm(request.POST)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.save() #la date de création sera automatiquement remplie
            return redirect('collection_list') #Redirige vers la liste des collections 
        else: 
            return render(request, './add_collection.html',{'form':form}) #affiche le formulaire avec de erreurs 
    else: 
        form=CollecForm()
        return render(request,'./add_collection.html', {'form': form})

def delete_collection(request, id):
    collection = get_object_or_404(Collec, id=id)
    if request.method == 'POST': 
        collection.delete()
        return redirect('collection_list')#Redirige vers la liste des collections après suppression 
    return render(request, './delete_collection.html', {'collection': collection})

def edit_collection(request, id):
    collection = get_object_or_404(Collec, id=id)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collection_list') #Redirige vers la liste des collections après modification
    else:
        form= CollecForm(instance=collection)
    return render(request, './edit_collection.html', {'form': form,'collection':collection})

def home(request):
    return render(request, './home.html')