import string
from datetime import date

from main.domain.enums.pet_type import PetType


class Pet:

    def __init__(self, name: string, pet_type: PetType, date_of_birth: date):
        self._name = name
        self._pet_type = pet_type
        self._date_of_birth = date_of_birth

    @property
    def name(self):
        return self._name

    @property
    def pet_type(self):
        return self._pet_type

    @property
    def date_of_birth(self):
        return self._date_of_birth
