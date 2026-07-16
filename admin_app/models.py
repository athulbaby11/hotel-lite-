
from django.db import models
# MainCategory model
class MainCategory(models.Model):
    heading = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='maincategory_images/', blank=True, null=True)
    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Main Category"
        verbose_name_plural = "1. Main Categories"

# Category model
class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    image_main = models.BooleanField(default=False, verbose_name='Image Main')

    def __str__(self):
        return f"{self.main_category.heading} - {self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "2. Categories"

# MenuItem model
class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.category.name})"

# Gallery image model
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.caption or str(self.image)

# Hero image model
class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.headline

# News model
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
from django.db import models
