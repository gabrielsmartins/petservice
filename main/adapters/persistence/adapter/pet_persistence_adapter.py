from injector import inject

from main.adapters.persistence.mapper.pet_persistence_mapper import PetPersistenceMapper
from main.adapters.persistence.repository.pet_repository import PetRepository
from main.common import logger
from main.domain.ports.output.create_pet_port import SavePetPort
from main.domain.ports.output.search_pet_port import SearchPetPort


class PetPersistenceAdapter(SavePetPort, SearchPetPort):

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

    def find_by_id(self, id):
        logger.info("Searching pet by id %s", id)
        pet_entity = self._repository.find_by_id(id)
        logger.info("Mapping found pet %s", pet_entity)
        pet = PetPersistenceMapper.map_to_domain(pet_entity)
        logger.info("Found pet was mapped successfully %s", pet)
        return pet
