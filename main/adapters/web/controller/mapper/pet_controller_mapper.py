from main.adapters.web.controller.dto.pet_dto import PetDto
from main.domain.enums.pet_type import PetType
from main.domain.pet import Pet


class PetControllerMapper:

    @staticmethod
    def map_to_domain(pet_dto: PetDto) -> Pet:
        return Pet(pet_dto['name'], PetType.from_name(pet_dto['pet_type']), pet_dto['date_of_birth'])

    @staticmethod
    def map_to_dto(pet: Pet) -> PetDto:
        pet_dto = PetDto()
        pet_dto.id = pet.id
        pet_dto.name = pet.name
        pet_dto.type = pet.pet_type.value[1]
        pet_dto.date_of_birth = pet.date_of_birth
        pet_dto.created_at = pet.created_at
        pet_dto.updated_at = pet.updated_at
        return pet_dto

