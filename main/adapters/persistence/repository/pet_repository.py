import uuid
from datetime import datetime

from botocore.exceptions import ClientError
from injector import inject

from main.adapters.persistence.config.dynamodb_connection_factory import DynamoDbConnectionFactory
from main.adapters.persistence.entity.pet_entity import PetEntity
from main.common import logger


class PetRepository:

    @inject
    def __init__(self, dynamodb_factory: DynamoDbConnectionFactory):
        self._dynamodb = dynamodb_factory.create_connection()

    def save(self, pet_entity: PetEntity):
        try:
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
        except ClientError as e:
            logger.error("Error saving pet", e)
            raise e

    def find_by_id(self, id):
        try:
            response = self._dynamodb.Table('Pets')\
                                     .get_item(Key={'id': id})
            item = response.get('Item')
            if item is not None:
                pet_entity = PetEntity()
                pet_entity.id = item.get('id')
                pet_entity.name = item.get('name')
                pet_entity.type = int(item.get('type'))
                pet_entity.date_of_birth = datetime.strptime(item.get('date_of_birth'), '%Y-%m-%d').date()
                pet_entity.created_at = datetime.strptime(item.get('created_at'), '%Y-%m-%d').date()
                pet_entity.updated_at = datetime.strptime(item.get('updated_at'), '%Y-%m-%d').date()
                return pet_entity
            return None
        except ClientError as e:
            logger.error("Error searching pet", e)
            raise e
