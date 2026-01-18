from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    deparment_display = serializers.CharField(
        source='get_deparment_display',
        read_only=True
    )

    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'birthday',
            'position',
            'deparment',
            'deparment_display',
            'entry_date',
            'creation_date',
            'is_active',
            'dni',
        ]
        read_only_fields = ['id', 'creation_date']



class EmployeeTableSerializer(serializers.ModelSerializer):
    deparment_display = serializers.CharField(
        source='get_deparment_display',
        read_only=True
    )

    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            # 'birthday',
            # 'position',
            # 'deparment', 
            'deparment_display',
            # 'entry_date',
            'is_active',
            'dni',
        ]
        read_only_fields = ['id', 'creation_date']