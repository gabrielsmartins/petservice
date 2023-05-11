import string
from datetime import date

from marshmallow import fields, Schema


class PetDto(Schema):
    id = fields.Str(data_key='id', required=False)
    name = fields.Str(data_key='name', required=True)
    pet_type = fields.Str(data_key='type', required=True)
    date_of_birth = fields.Date(data_key='date_of_birth', required=True)
    created_at = fields.Date(data_key='created_at', required=False)
    updated_at = fields.Date(data_key='updated_at', required=False)
