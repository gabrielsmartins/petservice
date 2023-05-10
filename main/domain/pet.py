import string
import uuid
from datetime import date

from main.domain.enums.pet_type import PetType


class Pet:

    def __init__(self, name: string, pet_type: PetType, date_of_birth: date):
        self._id = None
        self._name = name
        self._pet_type = pet_type
        self._date_of_birth = date_of_birth
        self._created_at = date.today()
        self._updated_at = date.today()


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        self._pet_type = pet_type

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at
