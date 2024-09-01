from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from auctions.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from auctions.api.pagination import SmallPagination, LargePagination


from auctions.api.serializers import PersonelSerializer,MakaleSerializer
from auctions.models import Personel,Makale

class PersonelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Personel.objects.all().order_by('id')
    serializer_class = PersonelSerializer
    permission_classes = [IsAdminUserOrReadOnly]



class PersonelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all().order_by('id')
    serializer_class = PersonelSerializer
    permission_classes = [IsAdminUserOrReadOnly]



class MakaleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Makale.objects.all().order_by('id')
    serializer_class = MakaleSerializer
    permission_classes = [IsAdminUserOrReadOnly]





class MakaleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Makale.objects.all().order_by('id')
    serializer_class = MakaleSerializer
    permission_classes = [IsAdminUserOrReadOnly]



