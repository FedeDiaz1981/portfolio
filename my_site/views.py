from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from rest_framework import generics
from .models import Proyecto, Testimonio, Articulo, Crecimiento, BlogPost
from .serializers import BlogPostSerializer


def home(request):
    crecimiento_data = Crecimiento.objects.all().order_by("año")
    
    # Convertir los datos en listas para JavaScript
    años = [dato.año for dato in crecimiento_data]
    valores = [dato.valor for dato in crecimiento_data]

    return render(request, 'my_site/home.html', {
        "años": años,
        "valores": valores
    })

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí puedes agregar la lógica para enviar el mensaje, guardar en la base de datos, etc.
            # Por ahora, solo mostramos un mensaje de éxito.
            render(request, 'contacto.html', {'form': form, 'success': True})
            return redirect('/')
            
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form, 'success': False})

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def testimonios(request):
    testimonios = Testimonio.objects.all()
    return render(request, 'testimonios.html', {'testimonios': testimonios})

def certificaciones(request):
    return render(request, 'certificaciones.html')

def blog(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'my_site/blog.html', {'articulos': articulos})

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all().order_by('-fecha_publicacion')
    serializer_class = BlogPostSerializer

def blog_detail(request, blog_id):
    articulo = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog_detail.html', {'articulo': articulo})

def blog_list(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, "about.html")