import unittest
from app.models import Writer

class UserModelTest(unittest.TestCase):

    
    def setUp(self):
        self.new_writer = Writer(password = 'password')
        self.new_writer2 = Writer(password = 'password')

    def test_password_setter(self):
        self.assertTrue(self.new_writer.password_hash is not None)
    
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_writer.password

    def test_password_verification(self):
        self.assertTrue(self.new_writer.verify_password('password'))
        self.assertFalse(self.new_writer.verify_password('testing'))
    
    def test_password_salts_are_random(self):
        self.assertTrue(self.new_writer.password_hash != self.new_writer2.password_hash)