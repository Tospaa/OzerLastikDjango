from rest_framework import serializers
from .models import Ayakkabi
class AyakkabiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayakkabi
        # fields = ('alis','satis') // belirtilen kisimlari ceker.
        # fields = '__all__' // tum kisimlari ceker.
        fields = ('Numara','Adet')