class Pet: 

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

# adding this PASSES lib/testing/test_owner_pet.py::test_has_pet_types 
# - AttributeError: type object 'Pet' has no attribute 'PET_TYPES'

    all = []
# adding this PASSES lib/testing/test_owner_pet.py::test_pet_has_all - 
# assert <owner_pet.Pet object at 0x7ff743a25e50> in []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

# adding this PASSES lib/testing/test_owner_pet.py::test_pet_init 
# - TypeError: Pet() takes no arguments
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type 

# adding this PASSESlib/testing/test_owner_pet.py::test_checks_pet_type 
# - Failed: DID NOT RAISE <class 'Exception'>

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

# adding this PASSES lib/testing/test_owner_pet.py::test_owner_init 
# - TypeError: Owner() takes no arguments
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
# adding this PASSESlib/testing/test_owner_pet.py::test_owner_has_pets - 
# AttributeError: 'Owner' object has no attribute 'pets'

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self            
# adding this PASSES lib/testing/test_owner_pet.py::test_owner_adds_pets - 
# AttributeError: 'Owner' object has no attribute 'add_pet'

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
# adding this PASSES lib/testing/test_owner_pet.py::test_sort_pets_by_name - 
# AttributeError: 'Owner' object has no attribute 'get_sorted_pets'