
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        },
            {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "luck_numbers": [10, 14, 3]
        },
            {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers":[1]
        },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return 
        # el metodo append funciona igual que el .push() de javascript, sirve para agregar un 
        # elemento más al final del array       
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        # de esta manera fue que consegui como saber la posicion de un elemento
        # https://www.kite.com/python/answers/how-to-find-the-position-of-an-element-in-an-array-in-python#:~:text=Use%20list.,position%20of%20value%20in%20list%20.
        for x in self._members:
            if x["id"] == int(id):
                # position_to_delete es la variable donde vamos a guardar la posisin encontrada
                # .index() es una funcion de python que se le aplica a un array para saber la posicion de un valor en ella
                # en este caso usamos X porque es el valor que va recorriendo el for y evaluamos el id dado con el que tenemos
                # en el arra, si lo encuentra, te va a dar la posicion
                position_to_delete = self._members.index(x)
                # despues usamos la funcion .pop() que funciona igual que el splice() de javascrip, que sirve para eliminar un elemento especifico
                # del array, en este caso usamos position_to_delete
                self._members.pop(position_to_delete)
            else:
                return "error 404, no se encuentra el member, intente de nuevo"


    def get_member(self, id):
        # fill this method and update the return
        for x in self._members:
            if x["id"] == int(id):
                return x
            else:
                return "error 404, no se encuentra el member, intente de nuevo"

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
