from ninja import ModelSchema, Schema
from .models import Student
from typing import Optional

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

class ClassHeldSchema(Schema):
    qtd: Optional[int] = 1
    email_student: str
