class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []    
        
    def __init__(self, name, pet_type, owner="John"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}")
        
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []
        
    def pets(self):
        owner_pets = [pet for pet in Pet.all if pet.owner == self]
        return owner_pets
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError(f"{pet} is not a pet")
        
        pet.owner = self
        self.pets_list.append(pet)
        
    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets_list, key=lambda pet: pet.name)
        return sorted_pets