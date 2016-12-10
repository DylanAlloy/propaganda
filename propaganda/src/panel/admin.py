from django.contrib import admin

# Register your models here.
from .forms import AddRedditForm
from .models import Account

class AddRedditAdmin(admin.ModelAdmin):
	list_display = ["__str__", "user_name", "timestamp", "user"]
	form = AddRedditForm

admin.site.register(Account)
