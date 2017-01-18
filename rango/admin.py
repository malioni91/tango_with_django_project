from django.contrib import admin
from rango.models import Category, Page, UserProfile
from django.contrib.admin import AdminSite


# add category and url as columsn in Admin interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

