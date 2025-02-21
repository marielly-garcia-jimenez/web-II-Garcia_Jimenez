
from django.contrib import admin
from .models import User, UserAddress
from .models import Direccion

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(Direccion)