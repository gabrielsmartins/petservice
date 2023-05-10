from main.domain.ports.output.create_pet_port import CreatePetPort


class PetPersistenceAdapter(CreatePetPort):

    def create(self, pet):
        return pet