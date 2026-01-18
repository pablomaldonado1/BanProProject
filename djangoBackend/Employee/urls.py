from django.urls import path
from . import views
from .views import CreateEmployee, EmployeeListView

urlpatterns = [
    path("create/", CreateEmployee.as_view(), name="create-employee"),
    path("list/", EmployeeListView.as_view(), name="employee-list"),
    path("get-deparments/", views.get_deparments, name="get-deparments"),
    path("get-employee/", views.get_employee,name="get-employee"),
    path("delete/<int:employee_id>", views.delete_employee, name="delete-employee"),
    path("update-employee/<int:employee_id>", views.update_employee,name="update-employee")
]