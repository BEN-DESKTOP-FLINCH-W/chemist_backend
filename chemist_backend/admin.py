from django.contrib import admin
from .models import Products
from .models import Sales
from .models import Categories
from .models import Expenses
from .models import Users

admin.site.register(Products)
admin.site.register(Sales)
admin.site.register(Categories)
admin.site.register(Expenses)
admin.site.register(Users)