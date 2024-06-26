#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test class"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The strongest in the Galaxy"

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class"""
        del cls.rev

    def tearDown(self):
        """Tear down the test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Test for PEP 8 compliance of the Review module"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP 8")

    def test_checking_for_docstring_Review(self):
        """Test if Review class has a docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """Test if Review instance has the required attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """Test the attribute types of Review instance"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'Skip for DB storage')
    def test_save_Review(self):
        """Test if the save method works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """Test if the to_dict method works"""
        rev_dict = self.rev.to_dict()
        self.assertEqual(self.rev.__class__.__name__, 'Review')
        self.assertIsInstance(rev_dict['created_at'], str)
        self.assertIsInstance(rev_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
