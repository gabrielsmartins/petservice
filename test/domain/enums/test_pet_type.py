import unittest
from unittest import TestCase

from main.domain.enums.pet_type import PetType


class TestPetType(TestCase):

    def test_given_code_when_exists_then_return_type(self):
        pet_type = PetType.from_code(1)
        self.assertEqual(pet_type, PetType.DOG)

    def test_given_code_when_not_exists_then_return_none(self):
        pet_type = PetType.from_code(99)
        self.assertEqual(pet_type, None)

if __name__ == '__main__':
    unittest.main()

