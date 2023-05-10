import uuid

from injector import inject

from main.adapters.persistence.config.dynamodb_connection_factory import DynamoDbConnectionFactory
from main.adapters.persistence.entity.pet_entity import PetEntity
from main.common import logger


class PetRepository:

    @inject
    def __init__(self, dynamodb_factory: DynamoDbConnectionFactory):
        self._dynamodb = dynamodb_factory.create_connection()

    def save(self, pet_entity: PetEntity):
        table = self._dynamodb.Table('Pets')
        id = uuid.uuid4()
        response = table.put_item(
            Item={
                'id': str(id),
                'name': pet_entity.name,
                'type': pet_entity.type,
                'date_of_birth': str(pet_entity.date_of_birth),
                'created_at': str(pet_entity.created_at),
                'updated_at': str(pet_entity.updated_at)
            }
        )
        logger.info("Pet was saved successfully: %s", response)
        pet_entity.id = id
        return pet_entity
