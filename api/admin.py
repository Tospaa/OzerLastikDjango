from django.contrib import admin
from .models import MamulDegisiklik, HammaddeDegisiklik, MamulSonDurum, HammaddeSonDurum

# Register your models here.

admin.site.register(MamulDegisiklik)
admin.site.register(HammaddeDegisiklik)
admin.site.register(MamulSonDurum)
admin.site.register(HammaddeSonDurum)
