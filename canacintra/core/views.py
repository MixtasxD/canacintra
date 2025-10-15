from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Publicacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import PublicacionForm

# Create your views here. 
def index(request): 
    return render(request, 'core/index.html')

def identidad(request): 
    return render(request, 'core/identidad.html')
    
def contactanos(request): 
    return render(request, 'core/contactanos.html')

def noticia(request): 
    return render(request, 'core/noticia.html')

def categoria(request): 
    return render(request, 'core/categoria.html')

def perfil(request): 
    return render(request, 'core/perfil.html')

# Blog dinámico básico
def posts(request):
    qs = Publicacion.objects.select_related('fk_categoria', 'fk_user').order_by('-created')
    paginator = Paginator(qs, 9)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'core/posts.html', { 'page_obj': page_obj })

def post_detail(request, pk: int):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'core/post_detail.html', { 'post': post })


# CRUD Publicacion
class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'core/publicacion_form.html'
    success_url = reverse_lazy('core:posts')

    def form_valid(self, form):
        # Asignar usuario creador si aplica
        obj = form.save(commit=False)
        if self.request.user.is_authenticated:
            obj.fk_user = self.request.user
        obj.save()
        return super().form_valid(form)


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'core/publicacion_form.html'
    success_url = reverse_lazy('core:posts')


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = 'core/publicacion_confirm_delete.html'
    success_url = reverse_lazy('core:posts')
