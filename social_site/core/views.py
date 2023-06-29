from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.models import Sezione, Discussione, Post
from .models import Logo


# Create your views here.

# def homepage(request):
#     return render (request, 'core/homepage.html')

class HomeView (ListView):
    queryset=Sezione.objects.all()
    template_name="core/homepage.html"
    context_object_name= "lista_sezioni"


class UserList (LoginRequiredMixin, ListView):
     model = User
     template_name="core/users.html"


def user_profile_view(request, username):
    user=get_object_or_404(User, username=username)
    discussioni_utente=Discussione.objects.filter(autore_discussione=user).order_by("-pk")
    context={"user":user,"discussioni_utente":discussioni_utente }
    return render (request, "core/user_profile.html", context)

def cerca(request):
    if "q" in request.GET:
        querystring=request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/cerca/")
        discussioni= Discussione.objects.filter(titolo__icontains = querystring)
        posts= Post.objects.filter(contenuto__icontains = querystring)
        users= User.objects.filter(username__icontains = querystring)
        context={"discussioni":discussioni, "posts":posts, "users":users}
        return render (request, "core/cerca.html", context)
    else:
        return render (request, "core/cerca.html")
    

def visualizza_logo (request):
    
   logo= Logo.objects.all()
   context={"logo":logo}
   return render (request, "core/homepage", context)