from ninja import Router
from .schema import StudentSchema, ProgressStudentSchema
from .models import Student, CompletedClass
from ninja.errors import HttpError
from typing import List
from .graduation import *

training_router = Router()

""" HTTP Verbs: """
""" GET -> Found data in API
    POST -> Creat data for API
    PUT -> Upgrade data from API
    DELETE -> Delete data from API
"""

@training_router.post('', response={200: StudentSchema})
def creat_student(request, student_schema: StudentSchema):
    name = student_schema.dict().get('name')
    email = student_schema.dict().get('email')
    belt = student_schema.dict().get('belt')
    date_birth = student_schema.dict().get('date_birth')

    """Descompreencion Variable"""
    #name, email, belt, date_birth = **student_schema.dict
    #student = Student(**student_schema.dict())

    if Student.objects.filter(email=email).exists():
        raise HttpError(400, 'Email já cadastrado!')
    student = Student(name=name,
                      email=email,
                      belt=belt,
                      date_birth=date_birth,)
    student.save()

    return student

@training_router.get('/students/', response=List[StudentSchema])
def list_student(request):
    students = Student.objects.all()
    return students

@training_router.get('/progress_student/', response={200: ProgressStudentSchema})
def progress_student(request, email_student: str):
    student = Student.objects.get(email=email_student)
    now_belt = student.get_belt_display()
    n = order_belt.get(now_belt, 0)

    total_class_next_belt = calculate_lesson_to_upgrade(n)
    total_class_concluid_belt = CompletedClass.objects.filter(student=student, now_belt=student.belt).count()
    were_left_classes = total_class_next_belt - total_class_concluid_belt

    return {
        'email': student.email,
        'name': student.name,
        'belt': now_belt,
        'total_class':
        total_class_concluid_belt,
        'class_for_next_belt': were_left_classes
    }
