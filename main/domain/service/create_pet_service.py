from injector import inject

from main.domain.pet import Pet
from main.domain.ports.input.create_pet_use_case import CreatePetUseCase
from main.domain.ports.output.create_pet_port import CreatePetPort


class CreatePetService(CreatePetUseCase):

    @inject
    def __init__(self, port: CreatePetPort):
        self._port = port

    def create(self, pet: Pet) -> Pet:
        return self._port.create(pet)



