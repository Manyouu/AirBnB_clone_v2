#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test class"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class"""
        del cls.state

    def tearDown(self):
        """Tear down the test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_State(self):
        """Test for PEP 8 compliance of the State module"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP 8")

    def test_checking_for_docstring_State(self):
        """Test if State class has a docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """Test if State instance has the required attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """Test the attribute types of State instance"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """Test if the save method works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Test if the to_dict method works"""
        state_dict = self.state.to_dict()
        self.assertEqual(self.state.__class__.__name__, 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
