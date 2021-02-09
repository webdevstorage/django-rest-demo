from django.shortcuts import render
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import (
    AllowAny, 
    IsAdminUser,
    DjangoModelPermissionsOrAnonReadOnly
    )
from .models import (
    Customer, 
    Profession,
    DataSheet,
    Document
)
from .serializers import (
    CustomerSerializer, 
    ProfessionSerializer,
    DataSheetSerializer,
    DocumentSerializer
)
from rest_framework import viewsets
from rest_framework.response import Response

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('name', )
    search_fields = ('name', 'address', 'data_sheet__description', )
    ordering_fields = ('id', 'name', )
    ordering = ('id', ) # default order
    lookup_field = 'doc_num' # this will turn url parms into name field. name should be unique
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        # this is where you catch query params
        address = self.request.query_params.get('address', None)
        
        if self.request.query_params.get('active') == 'False':
            status = False
        else:
            status = True

        if address:
            customers = Customer.objects.filter(address__icontains=address, active=status)
        else:
            customers = Customer.objects.filter(active=status)
        return customers

    def retrieve(self, request, *args, **kwargs):
        customer = self.get_object()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.create(
            name=data['name'], address=data['address'], data_sheet_id=data['data_sheet']                
        )
        profession = Profession.objects.get(id=data['profession'])

        customer.professions.add(profession)
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        customer = Customer.objects.get()
        data = request.data
        customer.name = data['name']
        customer.address = data['address']
        customer.data_sheet_id = data['data_sheet']
        profession = Profession.objects.get(id=data['profession'])

        for p in customer.professions.all():
            customer.professions.remove(p)

        customer.professions.add(profession)
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.name = request.data.get('name', customer.name)
        customer.address = request.data.get('address', customer.address)
        customer.data_sheet_id = request.data.get('data_sheet', customer.data_sheet_id)

        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def destory(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.delete()
        return Response('Object removed')

    @action(detail=True)
    def deactivate(self, rquest, **kwargs):
        customer = self.object_get()
        customer.active = False
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    @action(detail=False)
    def deactivate_all(self, request, **kwargs):
        customers = self.get_queryset()
        customers.update(active=False)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def activate_all(self, request, **kwargs):
        customers = self.get_queryset()
        customers.update(active=True)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class ProfessionViewSet(viewsets.ModelViewSet):
    # queryset = objects.all() will pull all objects in database.
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny, ]

class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer
    permission_classes = [AllowAny, ]

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]