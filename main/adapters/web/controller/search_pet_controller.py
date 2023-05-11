import uuid

from flask import jsonify, Blueprint
from injector import inject

from main.adapters.web.controller.mapper.pet_controller_mapper import PetControllerMapper
from main.common import logger
from main.domain.ports.input.search_pet_use_case import SearchPetUseCase

controller = Blueprint('search_pet_controller', __name__)


@inject
@controller.route('/pets/v1/<id>', methods=['GET'])
def find_by_id(use_case: SearchPetUseCase, id: uuid):
    logger.info("Searching pet by id %s", id)
    pet = use_case.find_by_id(id)
    logger.info("Pet was found successfully %s", pet)

    logger.info("Mapping pet %s", pet)
    pet_dto = PetControllerMapper.map_to_dto(pet)
    logger.info("Pet was mapped successfully %s", pet_dto)
    return jsonify(pet_dto.dump(pet_dto)), 200
