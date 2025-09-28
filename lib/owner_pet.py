class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            self.owner = owner
        Pet.all.append(self)



class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        #return a list of pets that belong to this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        #add this owner to a pet
        if not isinstance(pet, Pet):
            raise Exception("Expected a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of this owner's pets by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


