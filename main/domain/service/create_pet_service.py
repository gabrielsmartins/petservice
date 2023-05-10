from datetime import date

from injector import inject

from main.domain.pet import Pet
from main.domain.ports.input.create_pet_use_case import CreatePetUseCase
from main.domain.ports.output.create_pet_port import SavePetPort


class CreatePetService(CreatePetUseCase):

    @inject
    def __init__(self, port: SavePetPort):
        self._port = port

    def create(self, pet: Pet) -> Pet:
        pet.created_at = date.today()
        pet.updated_at = date.today()
        return self._port.save(pet)



