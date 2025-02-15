from ninja import NinjaAPI
from training.api import training_router

api = NinjaAPI()
api.add_router('', training_router)
