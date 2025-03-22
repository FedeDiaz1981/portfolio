from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/')
    enlace = models.URLField(max_length=200, blank=True, null=True)  # Si deseas agregar enlaces a tus proyectos

    def __str__(self):
        return self.titulo

class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    imagen = models.ImageField(upload_to='testimonios/', blank=True, null=True)  # Opcional
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.ocupacion}"

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Crecimiento(models.Model):
    año = models.IntegerField(unique=True)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.año}: {self.valor}"

class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    excerpt = models.TextField()  # Breve descripción del artículo
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo