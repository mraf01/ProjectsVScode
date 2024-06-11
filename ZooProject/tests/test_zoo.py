import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def setUp(self) -> None:
        self.zoo_l: Zoo = Zoo()
        self.zookeeper_l: ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id=1)
        self.fence_l: Fence = Fence(area=100, temperature=25.0, habitat="Savana")
        self.animal_l: Animal = Animal(name="Pluto", species="Canide", age=5, height=300.0, width=1.0, preferred_habitat="Savana")

    def test_animal_dimension(self):
        """
        Questo test controlla che animali troppo grandi non vengano aggiunti alla fence
        """

        self.zookeeper_l.add_animal(self.animal_l, self.fence_l)
        result: int = len(self.fence_l.animals)
        message: str = f"Error: the function add_animal should not add self.animal_l into self.fence_l"

        self.assertEqual(result, 0, message)

    def test_remove(self):
        lenlist:int = len(self.fence_l.animals)
        self.zookeeper_l.remove_animal(self.animal_l, self.fence_l)
        lenlist: int= len(self.fence_l.animals)
        result: int = lenlist
        message: str = f"Error: the function remove animal doesn't work"

        self.assertEqual(result, lenlist, message) 

if __name__ == "__main__":
        
    unittest.main()