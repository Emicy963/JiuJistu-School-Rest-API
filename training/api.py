from ninja import Router

training_router = Router()

""" HTTP Verbs: """
""" GET -> Found data in API
    POST -> Creat data for API
    PUT -> Upgrade data from API
    DELETE -> Delete data from API
"""

@training_router.get('test/')
def creat_student(request):
    return {'Hello Word!': 'Hello Word!'}
