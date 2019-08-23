import json
import unittest
from project.tests.base import BaseTestCase
from project.serializer import *


class TestSerializer(BaseTestCase):

    def test_serialize(self):
        """Ensure Serializer works"""
        id = [1, 3, 2]
        n = comp_serialize(id)
        bit_string = '{0:b}'.format(n)
        self.assertEqual('1110', bit_string)

    def test_serialize_bad_input(self):
        id = []
        n = comp_serialize(id)
        bit_string = '{0:b}'.format(n)
        self.assertEqual('-1', bit_string)


if __name__ == '__main__':
    unittest.main()
