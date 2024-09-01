from rest_framework import serializers
from auctions.models import Makale,Personel


from datetime import datetime
from datetime import date
from django.utils.timesince import timesince



class MakaleSerializer(serializers.ModelSerializer):

    #time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()

    class Meta:
        model = Makale
        fields = '__all__'

        read_only_fields = ['id', 'teslimtarihi', 'guncellenmetarihi']

class PersonelSerializer(serializers.ModelSerializer):
    teslimat = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )

    class Meta:
        model = Personel
        fields = '__all__'