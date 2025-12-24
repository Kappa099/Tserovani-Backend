from rest_framework import viewsets, filters
from .models import House
from .serializers import HouseSerializer

class HouseViewSet(viewsets.ModelViewSet):
    sdds =dsds
    
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['listing_type', 'property_type', 'location']
    ordering_fields = ['price', 'posted_at']

