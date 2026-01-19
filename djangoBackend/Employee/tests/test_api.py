from rest_framework.test import APIClient
from Employee.models import Employee
from datetime import date
import pytest

@pytest.mark.django_db
class TestEmployee:

    #test crear usuario
    def test_create_employee(self):
        client = APIClient()
        response = client.post('/employee/create/',
                            data = {
                            "name": "Pablo Maldonado",
                            "birthday": "1995-06-12",
                            "position": "Backend Developer",
                            "deparment": "IT",
                            "entry_date": "2024-01-15",
                            "dni": "12345678-9",
                            "is_active": True},
                            format='json')
        
        user = Employee.objects.get(dni="12345678-9")
        assert response.status_code == 201
        assert user.name == "Pablo Maldonado"
    
    #test obtener employee especifico
    def test_get_employee(self):
        employee = Employee.objects.create(
            name="Pablo Maldonado",
            birthday=date(1995, 3, 15),
            position="Backend Developer",
            deparment=Employee.Deparment.IT,
            entry_date=date(2024, 1, 10),
            dni="12345668-9"
            )

        client = APIClient()
        response = client.get('/employee/get-employee/?dni=12345668-9')
        assert response.status_code == 200
        assert response.data["id"] == 2
    
    #test para obtener tabla
    def test_get_table(self):
        client = APIClient()
        response = client.get('/employee/list/')
        assert response.status_code == 200

    #test obtener departamentos
    def test_get_deparments(self):
        client = APIClient()
        response = client.get('/employee/get-deparments/')
        assert response.status_code == 200
    
    #test eliminar employee
    def test_delete_employee(self):
        employee = Employee.objects.create(
            name="Pablo Maldonado",
            birthday=date(1995, 3, 15),
            position="Backend Developer",
            deparment=Employee.Deparment.IT,
            entry_date=date(2024, 1, 10),
            dni="12345678-9"
        )

        client = APIClient()
        response = client.delete(f"/employee/delete/{employee.id}")

        assert response.status_code == 204
        assert Employee.objects.filter(id=employee.id).exists() is False
    
    #test cambiarle nombre a un employee
    def test_update_employee(self):
        employee = Employee.objects.create(
            name="Juan",
            birthday=date(1995, 6, 12),
            position="Backend Developer",
            deparment=Employee.Deparment.IT,
            entry_date=date(2024, 1, 15),
            dni="12345999-9",
            is_active=True
        )

        client = APIClient()
        response = client.patch(
            f"/employee/update-employee/{employee.id}",
            {"name": "Pablo Maldonado"},
            format="json"
        )

    
        assert response.status_code == 200
        employee.refresh_from_db()
        assert employee.name == "Pablo Maldonado"