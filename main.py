import json

from datetime import date

from main.adapters.persistence.adapter.pet_persistence_adapter import PetPersistenceAdapter
from main.adapters.persistence.config.dynamodb_connection_factory import DynamoDbConnectionFactory
from main.adapters.persistence.repository.pet_repository import PetRepository
from main.domain.ports.input.search_pet_use_case import SearchPetUseCase
from main.domain.ports.output.create_pet_port import SavePetPort

from flask import Flask
from flask_injector import FlaskInjector
from injector import Binder, singleton

from main.adapters.web.controller.create_pet_controller import controller as create_pet_controller
from main.adapters.web.controller.search_pet_controller import controller as search_pet_controller
from main.domain.ports.input.create_pet_use_case import CreatePetUseCase
from main.domain.ports.output.search_pet_port import SearchPetPort
from main.domain.service.create_pet_service import CreatePetService
from main.domain.service.search_pet_service import SearchPetService

app = Flask(__name__)
app.register_blueprint(create_pet_controller)
app.register_blueprint(search_pet_controller)


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


app.json_encoder = CustomJsonEncoder


def configure(binder: Binder) -> None:
    binder.bind(CreatePetUseCase, to=CreatePetService, scope=singleton)
    binder.bind(SavePetPort, to=PetPersistenceAdapter, scope=singleton)
    binder.bind(PetRepository, to=PetRepository, scope=singleton)
    binder.bind(DynamoDbConnectionFactory, to=DynamoDbConnectionFactory, scope=singleton)
    binder.bind(SearchPetUseCase, to=SearchPetService, scope=singleton)
    binder.bind(SearchPetPort, to=PetPersistenceAdapter, scope=singleton)


app_injector = FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(port=8080)
