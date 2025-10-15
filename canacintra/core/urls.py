from django.urls import path
from . import views

app_name = "core"

urlpatterns = [ 
    path("", views.index, name="index"), 
    path("identidad", views.identidad, name="identidad"),
    path("noticia", views.noticia, name="noticia"),
    path("contactanos", views.contactanos, name="contactanos"),
    path("categoria", views.categoria, name="categoria"),
    path("perfil", views.perfil, name="perfil"),
    # Blog dinámico
    path("posts", views.posts, name="posts"),
    path("posts/<int:pk>", views.post_detail, name="post_detail"),
    # CRUD Publicacion
    path("posts/create", views.PublicacionCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/edit", views.PublicacionUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete", views.PublicacionDeleteView.as_view(), name="post_delete"),

]