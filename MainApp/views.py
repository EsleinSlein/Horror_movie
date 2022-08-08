from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import MovieForm
from .models import Movies



class MoviesList(ListView):
    model = Movies
    queryset = Movies.objects.all()
    ordering = ['-film_ratings']
    extra_context = {'title': 'Список фильмов'}
    paginate_by = 30



class AddMovie(CreateView):
    form_class = MovieForm
    template_name = 'MainApp/add_movie.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Добавить фильм'}


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'MainApp/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'MainApp/login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
