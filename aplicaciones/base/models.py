from django.db import models
from ckeditor.fields import RichTextField

class ModeloBase(models.Model):
  id = models.AutoField(primary_key=True)
  estado=models.BooleanField('Estado', default=True)
  fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)
  fecha_modificacion= models.DateField('Fecha de modificacion', auto_now=True, auto_now_add=False)
  fecha_eliminacion = models.DateField('Fecha de eliminacion', auto_now=True, auto_now_add=False)
  
  class Meta:
    abstract=True
    
class Categoria(ModeloBase):
  nombre=models.CharField('Nombre de la categoria',max_length=100, unique=True)
  imagen_referencial=models.ImageField('Imagen referencial', upload_to='categorias/')
  
  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    
  def __str__(self):
    return self.nombre
  
class Autor(ModeloBase):
  nombre=models.CharField('Nombres',max_length=100)
  apellido=models.CharField('Apellidos',max_length=120)
  email=models.EmailField('Correo electronico', max_length=200)
  descripcion=models.TextField('Descripcion')
  web=models.URLField('Sitio web', null=True,blank=True)
  facebook=models.URLField('Facebook', null=True,blank=True)
  instagram=models.URLField('Instagram', null=True,blank=True)
  twiter=models.URLField('Twiter', null=True,blank=True)
  
  class Meta:
    verbose_name = 'Autor'
    verbose_name_plural = 'Autores'
    
  def __str__(self):
    return '{0}, {1}'.format(self.apellido, self.nombre)
  
class Post(ModeloBase):
  class PostObject(models.Manager):
    def get_queryset(self) :
      return super().get_queryset() .filter(publicado=True)
    
  options=(
    ('borrador', 'Borrador'), ('publicado', 'Publicado')
  )
      
      
  titulo = models.CharField('Titulo del post', max_length=150, unique=True)
  slug = models.SlugField('Slug', max_length=250,null=False, unique=True)
  descripcion=models.TextField('Descripcion')
  autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  contenido=RichTextField
  imagen_referencial=models.ImageField('Imagen Referencial', upload_to='imagenes/', max_length=255)
  publicado=models.BooleanField('Publicado / No Publicado',default=False)
  publish = models.CharField(max_length=10, choices=options, default='borrador')
  fecha_publicacion=models.DateField('Fecha de publicacion')
  objects = models.Manager() #Manager por default
  postobject = PostObject() #Manager personalizado
  
  class Meta:
    ordering = ('-fecha_creacion',)
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
    
  def __str__(self):
    return self.titulo
  
class Web(ModeloBase):
  nosotros=models.TextField('Nosotros')
  telefono=models.CharField('Telefono', max_length=15)
  email=models.EmailField('Correo electronico',max_length=200)

  class Meta: 
    verbose_name = 'Web'
    verbose_name_plural = 'Webs'
    
  def __str__(self):
    return self.nosotros
  
class RedesSociales(ModeloBase):
  facebook=models.URLField('Facebook', null=True,blank=True)
  instagram=models.URLField('Instagram', null=True,blank=True)
  twiter=models.URLField('Twiter', null=True,blank=True)
  
  class Meta: 
    verbose_name = 'Red Social'
    verbose_name_plural = 'Redes Sociales'
    
    def __str__(self):
      return self.facebook
  
class Contacto(ModeloBase):
    nombre=models.CharField('Nombres',max_length=100)
    apellido=models.CharField('Apellidos',max_length=120)
    email=models.EmailField('Correo electronico', max_length=200)
    asunto=models.CharField('Asunto', max_length=200)
    mensaje=models.TextField('Mensaje')
    
    class Meta: 
      verbose_name = 'Contacto'
      verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return self.asunto
    
class Suscriptor(ModeloBase):
  email=models.EmailField('Correo electrinico', max_length=200)
  
  class Meta: 
    verbose_name = 'Suscriptor'
    verbose_name_plural = 'Suscriptores'
    
    def __str__(self):
      return self.email