
from django.contrib import admin
from django.contrib.admin import AdminSite


# Kerala Street Admin Branding
class CustomAdminSite(AdminSite):
	site_header = "Kerala Street Administration"
	site_title = "Kerala Street Admin Portal"
	index_title = "Welcome to Kerala Street Admin Panel"

	# Use a custom app_index template for grouping
	app_index_template = "custom_admin/app_index.html"

admin_site = CustomAdminSite(name='custom_admin')

from .models import GalleryImage, HeroImage, News, MainCategory, Category
from hotel.models import register as RegisterModel

# Register models with both admin.site (default) and admin_site (custom)
@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'heading')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'main_category', 'name')

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'phone')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
	list_display = ('id', 'caption', 'description')

@admin.register(HeroImage)
class HeroImageAdmin(admin.ModelAdmin):
	list_display = ('id', 'headline', 'subheadline')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'date')

# Optionally, also register with custom admin_site for grouped view if needed
# admin_site.register(MainCategory, MainCategoryAdmin)
# admin_site.register(Category, CategoryAdmin)
# admin_site.register(RegisterModel, RegisterAdmin)
# admin_site.register(GalleryImage, GalleryImageAdmin)
# admin_site.register(HeroImage, HeroImageAdmin)
# admin_site.register(News, NewsAdmin)
