from django.contrib import admin
from rango.models import Category, Page
from django.contrib.admin import AdminSite


# add category and url as columsn in Admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')



admin.site.register(Category)
admin.site.register(Page, PageAdmin)

