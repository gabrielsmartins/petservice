from flask import jsonify, request, Blueprint
from injector import inject

from main.adapters.web.controller.dto.pet_dto import PetDto
from main.adapters.web.controller.mapper.pet_controller_mapper import PetControllerMapper
from main.common import logger
from main.domain.ports.input.create_pet_use_case import CreatePetUseCase

controller = Blueprint('create_pet_controller', __name__)


@inject
@controller.route('/pets/v1', methods=['POST'])
def create(use_case: CreatePetUseCase):
    body = request.json
    logger.info("Receiving request %s", body)
    schema = PetDto()
    pet_dto = schema.load(body)

    logger.info("Mapping pet %s", pet_dto)
    pet = PetControllerMapper.map_to_domain(pet_dto)
    logger.info("Pet was mapped successfully %s", pet)

    logger.info("Creating pet %s", pet)
    created_pet = use_case.create(pet)
    logger.info("Pet was created successfully %s", created_pet)

    logger.info("Mapping created pet %s", created_pet)
    created_pet_dto = PetControllerMapper.map_to_dto(created_pet)

    logger.info("Created pet was mapped successfully %s", created_pet_dto)
    return jsonify(created_pet_dto.dump(created_pet_dto)), 201
