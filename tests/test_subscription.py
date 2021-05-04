import unittest
from app.models import Subscription

class SubscriptionModelCase(unittest.TestCase):
    def setUp(self):
        self.new_subie = Subscription(name = 'Jon Snow', email = 'jon@winterfell.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_subie, Subscription))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_subie.name,'Jon Snow')
        self.assertEquals(self.new_subie.email, 'jon@winterfell.com')