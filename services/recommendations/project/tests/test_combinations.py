import json
import unittest
from project.tests.base import BaseTestCase
from project.serializer import *


class TestSerializer(BaseTestCase):

    def test_serialize(self):
        """Ensure Serializer works"""
        id = [1, 3, 2]
        result = comp_serialize(id)
        self.assertEqual('1110', result)

    def test_serialize_bad_input(self):
        id = []
        result = comp_serialize(id)
        self.assertEqual('0', result)

class TestDeserialize(BaseTestCase):
    def test_deserialize(self):
        """basic test case"""
        bit_string = '1110'
        result = comp_deserialize(bit_string)
        self.assertEqual("1,2,3", result)

    def test_deserialize(self):
        """Leading zeroes"""
        bit_string = '0001110'
        result = comp_deserialize(bit_string)
        self.assertEqual("1,2,3", result)

if __name__ == '__main__':
    unittest.main()
