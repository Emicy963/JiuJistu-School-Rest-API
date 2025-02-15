from ninja import Router
from .schema import StudentSchema, ProgressStudentSchema, ClassHeldSchema
from .models import Student, CompletedClass
from ninja.errors import HttpError
from typing import List
from .graduation import *
from datetime import date

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

@training_router.post('/class_held/', response={200: str})
def class_held(request, class_held: ClassHeldSchema):
    qtd = class_held.dict()['qtd']
    email_student = class_held.dict()['email_student']
    
    if qtd <= 0:
        raise HttpError(400, 'Quantidade de aula deve ser maior que zero!')
    
    student = Student.objects.get(email=email_student)

    """ Menos útil em questão de performence """
    for _ in range(0, qtd):
        ch = CompletedClass(
            student=student,
            now_belt=student.belt
        )
        ch.save()

    """ Mais relevante em questão de performance
        class_ = [
        CompletedClass(student=student, belt=student.belt)
        for _ in range(qtd)
    ]
    CompletedClass.objects.bulk_create(class_)"""
    
    return 200, f'Aula realizada para o aluno: {student.name}'

@training_router.put('/students/{student_id}', response=StudentSchema)
def upgrade_student(request, student_id: int, student_data: StudentSchema):
    student = Student.objects.get(id=student_id)
    age = date.today() - student.date_birth

    if int(age.days/365) < 18 and student_data.dict()['belt'] in ('A', 'R', 'M', 'P'):
        raise HttpError(400, 'Menores de 18 não podem receber essa faixa!')
    
    """ That's work but for so many variable it's not ok! """
    #student.name = student_data.dict()['name']
    #student.email = student_data.dict()['email']
    #student.belt = student_data.dict()['belt']

    for attr, value in student_data.dict().items():
        if value:
            setattr(student, attr, value)
    student.save()
    return student
