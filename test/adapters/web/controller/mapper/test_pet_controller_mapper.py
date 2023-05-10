from datetime import date
from unittest import TestCase

from main.adapters.web.controller.dto.pet_dto import PetDto
from main.adapters.web.controller.mapper.pet_controller_mapper import PetControllerMapper
from main.domain.enums.pet_type import PetType
from main.domain.pet import Pet


class TestPetControllerMapper(TestCase):

    def test_given_pet_dto_when_map_then_return_pet(self):
        pet_dto = PetDto().dumps({'name': 'Tobby',
                                  'type': 'DOG',
                                  'date_of_birth': date(2022, 3, 10)
                                  })
        pet = PetControllerMapper.map_to_domain(pet_dto)
        self.assertEqual(pet.name, pet_dto.name)
        self.assertEqual(pet.pet_type[1], PetType.from_code(pet_dto.pet_type))
        self.assertEqual(pet.date_of_birth, pet_dto.date_of_birth)

    def test_given_pet_when_map_then_return_pet_dto(self):
        pet = Pet('Tobby', PetType.DOG, date(2022, 10, 4))
        pet_dto = PetControllerMapper.map_to_dto(pet)
        self.assertEqual(pet_dto.name, pet.name)
        self.assertEqual(pet_dto.pet_type, pet.pet_type.value[1])
        self.assertEqual(pet_dto.date_of_birth, pet.date_of_birth)
