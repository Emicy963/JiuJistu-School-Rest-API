from ninja import ModelSchema
from .models import Student

class StudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ['name', 'email', 'belt', 'date_birth']
