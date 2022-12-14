from atexit import register
from django.contrib import admin
from .models import Deposite,Withdraw,Balance
# Register your models here.
admin.site.register(Deposite)
admin.site.register(Withdraw)
admin.site.register(Balance)