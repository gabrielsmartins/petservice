import uuid

from main.domain.pet import Pet


class SearchPetPort:

    def find_by_id(self, id: uuid) -> Pet | None:
        pass
