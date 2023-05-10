import json
import logging

from flask import jsonify, request, Blueprint
from injector import inject

from main.adapters.web.controller.dto.pet_dto import PetDto
from main.adapters.web.controller.mapper.pet_controller_mapper import PetControllerMapper
from main.domain.ports.input.create_pet_use_case import CreatePetUseCase

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

pet_blueprint = Blueprint('pet', __name__)


@inject
@pet_blueprint.route('/pets/v1', methods=['POST'])
def post(use_case: CreatePetUseCase):
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
    return jsonify(created_pet_dto.__dict__), 201
