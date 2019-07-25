from django.contrib import admin

# Register your models here.
from .models import Company
admin.site.register(Company)

from .models import Close
admin.site.register(Close)
