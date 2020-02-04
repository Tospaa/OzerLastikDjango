from django.contrib import admin
from .models import KoliDegisiklik, HammaddeDegisiklik, KoliSonDurum, HammaddeSonDurum

# Register your models here.

admin.site.register(KoliDegisiklik)
admin.site.register(HammaddeDegisiklik)
admin.site.register(KoliSonDurum)
admin.site.register(HammaddeSonDurum)
