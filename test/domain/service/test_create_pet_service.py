from datetime import date
from unittest import TestCase
from unittest.mock import Mock

from main.domain.enums.pet_type import PetType
from main.domain.pet import Pet
from main.domain.ports.output.create_pet_port import CreatePetPort
from main.domain.service.create_pet_service import CreatePetService


class TestCreatePetService(TestCase):

    def setUp(self):
        self._port = Mock(spec=CreatePetPort)
        pet_mock = Pet('Tobby', PetType.DOG, date(2022, 4, 1))
        self._port.create.return_value = pet_mock
        self._service = CreatePetService(self._port)

    def test_pet_given_when_create_then_return_created_pet(self):
        pet = Pet('Tobby', PetType.DOG, date(2022, 4, 1))
        created_pet = self._service.create(pet)
        self.assertIsNotNone(created_pet)
        self._port.create.assert_called_once_with(pet)