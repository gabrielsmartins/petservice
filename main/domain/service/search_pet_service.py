from injector import inject

from main.domain.ports.input.search_pet_use_case import SearchPetUseCase
from main.domain.ports.output.search_pet_port import SearchPetPort


class SearchPetService(SearchPetUseCase):

    @inject
    def __init__(self, port: SearchPetPort):
        self._port = port

    def find_by_id(self, id):
        return self._port.find_by_id(id)