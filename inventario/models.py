from django.db import models

# Create your models here.
class Categoria(models.Model):
    category_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_name
    
    class META:
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
class Productos(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    imagen = models.ImageField(upload_to='img_inventario',null=True,blank=True)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True,default=1)
    
    origin = [
        ("NAC","Nacional"),
        ("IMP","Importado"),
    ]
    
    origen = models.CharField(max_length=30,choices=origin,default="NAC")

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
