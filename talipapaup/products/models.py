from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=300)
    primaryCategory = models.BooleanField(default = False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f"/products/{self.title}/"
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'
        ordering = ['title',]
        
class Stall(models.Model):
    name_of_stall = models.CharField(max_length = 300)
    address = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name_of_stall
    
class Product(models.Model):
    measurements = (
        ('kgs', 'kgs'),
        ('pcs', 'pcs'),
    )
    mainimage = models.ImageField(upload_to = 'products/', blank = True)
    name = models.CharField(unique = True, max_length = 300)
    product_id = models.AutoField(primary_key = True)
    stall_address = models.ForeignKey(Stall, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    preview_text = models.TextField(max_length = 300, verbose_name = 'Preview Text')
    detail_text = models.TextField(max_length = 300, verbose_name = 'Detail Text')
    price = models.IntegerField()
    measurement = models.CharField(max_length = 100, choices=measurements)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"{self.product_id}/"
    
    def get_absolute_detail(self):
        return f"products/list/{self.product_id}/"
    
    class Meta :
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name',]
        


    
    