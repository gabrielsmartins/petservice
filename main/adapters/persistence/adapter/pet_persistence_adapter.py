from injector import inject

from main.adapters.persistence.mapper.pet_persistence_mapper import PetPersistenceMapper
from main.adapters.persistence.repository.pet_repository import PetRepository
from main.common import logger
from main.domain.ports.output.create_pet_port import SavePetPort


class PetPersistenceAdapter(SavePetPort):

    @inject
    def __init__(self, repository: PetRepository):
        self._repository = repository

    def save(self, pet):
        logger.info("Mapping pet %s", pet)
        pet_entity = PetPersistenceMapper.map_to_entity(pet)
        logger.info("Pet was mapped successfully %s", pet_entity)

        logger.info("Saving pet %s", pet_entity)
        self._repository.save(pet_entity)
        logger.info("Pet was saved successfully %s", pet_entity)
        pet.id = pet_entity.id

        logger.info("Mapping saved pet %s", pet_entity)
        saved_pet = PetPersistenceMapper.map_to_domain(pet_entity)
        logger.info("Saved pet was mapped successfully %s", saved_pet)
        return saved_pet
