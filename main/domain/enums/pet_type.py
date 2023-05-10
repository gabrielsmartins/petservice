from enum import Enum


class PetType(Enum):

    DOG = 1, 'DOG'
    CAT = 2, 'CAT'
    BIRD = 3, 'BIRD'
    MOUSE = 4, 'MOUSE'
    HORSE = 5, 'HORSE'
    COW = 6, 'COW'
    OTHER = 7, 'OTHER'

    @staticmethod
    def from_code(code: int):
        for pet_type in PetType:
            if pet_type.value[0] == code:
                return pet_type
        return None

    @staticmethod
    def from_name(name: str):
        for pet_type in PetType:
            if pet_type.value[1] == name:
                return pet_type
        return None
