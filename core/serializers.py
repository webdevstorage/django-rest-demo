from rest_framework import serializers
from .models import (
    Customer, 
    Profession,
    DataSheet,
    Document
)

class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = (
            'id', 'description', 'historical_data'
        )

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = (
            'id', 'description', 'status'
        )

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id',
            'dtype',
            'doc_number',
            'customer'
        )


class CustomerSerializer(serializers.ModelSerializer):
    num_professions = serializers.SerializerMethodField()
    data_sheet = DataSheetSerializer(read_only=True)
    professions = ProfessionSerializer(many=True)
    document_set = DocumentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = (
            'id', 'name', 'address', 'professions', 
            'data_sheet', 'active', 'status_message', 
            'num_professions', 'document_set')
            
    def get_num_professions(self, obj):
        return obj.num_professions()


