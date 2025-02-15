from ninja import ModelSchema, Schema
from .models import Student

class StudentSchema(ModelSchema):
    class Meta:
        model = Student
        fields = ['name', 'email', 'belt', 'date_birth']

class ProgressStudentSchema(Schema):
    email: str
    name: str
    belt: str
    total_class: int
    class_for_next_belt: int
