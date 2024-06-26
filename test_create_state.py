#!/usr/bin/python3


import unittest
import os
import MySQLdb
from models import storage
from models.state import State


class TestCreateState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the test environment
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_MYSQL_USER'] = 'hbnb_test'
        os.environ['HBNB_MYSQL_PWD'] = 'hbnb_test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'hbnb_test_db'
        os.environ['HBNB_TYPE_STORAGE'] = 'db'

    @classmethod
    def tearDownClass(cls):
        # Clean up the test environment
        del os.environ['HBNB_ENV']
        del os.environ['HBNB_MYSQL_USER']
        del os.environ['HBNB_MYSQL_PWD']
        del os.environ['HBNB_MYSQL_HOST']
        del os.environ['HBNB_MYSQL_DB']
        del os.environ['HBNB_TYPE_STORAGE']

    def setUp(self):
        # Set up the database connection
        self.db = MySQLdb.connect(host=os.getenv('HBNB_MYSQL_HOST'),
                                  user=os.getenv('HBNB_MYSQL_USER'),
                                  passwd=os.getenv('HBNB_MYSQL_PWD'),
                                  db=os.getenv('HBNB_MYSQL_DB'),
                                  charset='utf8')

        # Create a cursor to execute SQL queries
        self.cursor = self.db.cursor()

        # Clear the states table before each test
        self.cursor.execute("TRUNCATE TABLE states")

    def tearDown(self):
        # Close the database connection
        self.db.close()

    def test_create_state(self):
        # Get the initial count of records in the states table
        initial_count = self.get_states_count()

        # Execute the console command
        os.system('echo "create State name=\'California\'" | ./console.py')

        # Get the count of records in the states table after executing the command
        final_count = self.get_states_count()

        # Assert that the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    def get_states_count(self):
        # Execute a query to get the count of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        result = self.cursor.fetchone()
        return result[0]


if __name__ == '__main__':
    unittest.main()
