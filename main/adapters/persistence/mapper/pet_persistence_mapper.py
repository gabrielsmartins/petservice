from main.adapters.persistence.entity.pet_entity import PetEntity
from main.domain.enums.pet_type import PetType
from main.domain.pet import Pet


class PetPersistenceMapper:

    @staticmethod
    def map_to_entity(pet: Pet) -> PetEntity:
        pet_entity = PetEntity()
        pet_entity.id = pet.id
        pet_entity.name = pet.name
        pet_entity.type = pet.pet_type.value[0]
        pet_entity.date_of_birth = pet.date_of_birth
        pet_entity.created_at = pet.created_at
        pet_entity.updated_at = pet.updated_at
        return pet_entity

    @staticmethod
    def map_to_domain(pet_entity: PetEntity) -> Pet:
        pet = Pet(pet_entity.name, PetType.from_code(pet_entity.type), pet_entity.date_of_birth)
        pet_entity.id = pet.id
        pet_entity.created_at = pet_entity.created_at
        pet_entity.updated_at = pet_entity.updated_at
        return pet
