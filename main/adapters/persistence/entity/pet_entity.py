import uuid
from datetime import date


class PetEntity:

    id: uuid
    name: str
    type: int
    created_at: date
    updated_at: date
    date_of_birth: date
