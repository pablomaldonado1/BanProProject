from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EmployeeSerializer, EmployeeTableSerializer
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404




#metodo para crear un usuario
class CreateEmployee(APIView):

    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                employee = serializer.save()
                return Response(
                    EmployeeSerializer(employee).data,
                    status=status.HTTP_201_CREATED
                )

            #guardar en log que se intento crear algo pero no funciono

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

#metodo para traer tabla de todos los trabajadores
class EmployeeListView(ListAPIView):
    serializer_class = EmployeeTableSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()

        # parametros de filtro
        is_active = self.request.query_params.get("is_active")
        deparment = self.request.query_params.get("deparment")
        name = self.request.query_params.get("name")
        dni = self.request.query_params.get("dni")

        #aplicar filtro
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == "true")

        if deparment:
            queryset = queryset.filter(deparment__iexact=deparment)

        if name:
            queryset = queryset.filter(name__icontains=name)

        if dni:
            queryset = queryset.filter(dni=dni)
        

        return queryset.order_by("-id")

#metodo ayuda para conseguir el ENUM de los departamentos
@api_view(["GET"])
def get_deparments(request):
    resp = {}
    for value,full_name in Employee.Deparment.choices:
        resp[value] = full_name
    return Response(resp, status = status.HTTP_200_OK)


#metodo para obtener usuario especifico para editar/eliminar
@api_view(["GET"])
def get_employee(request):
    dni = request.query_params.get("dni")

    if not dni:
        return Response({"error": "parameter is missing"}, status=400)
    
    employee = get_object_or_404(Employee, dni=dni)

    return Response({"id":employee.id},status=status.HTTP_200_OK)


#metodo para eliminar un employee
@api_view(["DELETE"])
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return Response({"message:" : "employee was deleted"},status=status.HTTP_204_NO_CONTENT)


@api_view(["PATCH"])
def update_employee(request, employee_id):
    
    try:
        employee = Employee.objects.get(id=employee_id)
    except Exception as e:
        return Response({'message': "Employee does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    new_name = request.data.get("name", None)
    new_position = request.data.get("position", None)
    new_deparment = request.data.get("deparment", None)
    new_is_active = request.data.get("is_acticve", None)

    if new_name is not None:
        employee.name = new_name

    if new_position is not None:
        employee.position = new_position

    if new_deparment is not None:
        if new_deparment not in dict(Employee.Deparment.choices):
            return Response(
                {"deparment": "deparment does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        employee.deparment = new_deparment

    if new_is_active is not None:
        employee.is_active = new_is_active

    employee.save()

    return Response({"message" : "Employee data updated"}, status=status.HTTP_200_OK)


