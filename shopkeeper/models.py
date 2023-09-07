from colorfield.fields import ColorField
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
class Color(models.Model):
    name=models.CharField(max_length=200)
    hex_color=ColorField(blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
class mainCat(models.Model):
    name=models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True )
    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args, **kwargs)
class subCat(models.Model):
    main_cat=models.ForeignKey(mainCat, on_delete= models.CASCADE)
    name=models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True )
    def __str__(self):
        return str(self.main_cat.name ) +" / " + str(self.name )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args, **kwargs)
class categorys(models.Model):
    main_cat=models.ForeignKey(mainCat, on_delete= models.CASCADE)
    sub_cat=models.ForeignKey(subCat, on_delete= models.CASCADE)
    name=models.CharField(max_length=200)
    slug = models.CharField(max_length=200, null=True, blank=True )
    def __str__(self):
        return str(self.main_cat.name ) +" / " +str(self.sub_cat.name ) +" / " + str(self.name )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super().save(*args, **kwargs)
class Image(models.Model):
    image=CloudinaryField('image')
class Review(models.Model):
    customer=models.ForeignKey(User, on_delete= models.CASCADE)
    rate=models.IntegerField(blank=True, null=True)
    title = models.CharField( max_length=200,blank=True, null=True)
    content = models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return str(self.title) 
class pruduct(models.Model):

    category=models.ForeignKey(categorys, on_delete= models.CASCADE)
    title=models.CharField(max_length=200)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2 ,blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,)
    discount = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True)
    slug = models.SlugField()
    image=models.ManyToManyField(Image, blank=True)
    description = models.TextField(blank=True)
    colors=models.ManyToManyField(Color, blank=True)

    size = models.CharField(max_length=200,blank=True, null=True)
    size2 = models.CharField( max_length=200,blank=True, null=True)
    size3 = models.CharField( max_length=200,blank=True, null=True)
    size4 = models.CharField( max_length=200,blank=True, null=True)
    product_date=models.DateTimeField(auto_now_add=True, )
    views=models.IntegerField(default=0)
    out_of_stock = models.BooleanField(default=False)
    riviews= models.ManyToManyField(
        Review, related_name="riviews",blank=True)
    def __str__(self):
        return str(self.title)
   
   
    def get_sizes(self):
        sizes=[]
        
        if self.size != None:
            sizes.append(self.size)     
        if self.size2 != None:
            sizes.append(self.size2)     
        if self.size3 != None:
            sizes.append(self.size3)     
        if self.size4 != None:
            sizes.append(self.size4)  
        return sizes   
    def chanegePrice(self):
        if self.discount and self.discount != None:
            self.oldprice=self.price
            self.price= self.price - (self.price * 20 /100)
            self.save()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(str(self.category.name)+ "_"+ self.title +str(self.id))
        
            
        return super().save(*args, **kwargs)
     

    
class TodoList(models.Model):
    todo = models.CharField( max_length=200,blank=True, null=True)
    todo_date=models.DateTimeField()
    def __str__(self):
        return str(self.todo)

    def is_today(self):
        e=False
        month=datetime.now().month
        year=datetime.now().year
        daye=datetime.now().day
        if self.todo_date.year == year and self.todo_date.month == month and self.todo_date.day== daye:
            e=True
        return e
    
    
  
class Profile(models.Model):
    facebook=models.URLField(max_length=200, null=True, blank=True)
    tiktok=models.URLField(max_length=200, null=True, blank=True)
    instagram=models.URLField(max_length=200, null=True, blank=True)
    address=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.IntegerField( null=True, blank=True)
    def __str__(self):
        return str(self.email)
