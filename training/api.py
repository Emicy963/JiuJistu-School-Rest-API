from ninja import Router
from .schema import StudentSchema
from .models import Student
from ninja.errors import HttpError

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


