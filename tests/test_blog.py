import unittest
from app.models import Writer, Blog

class BlogModelCase(unittest.TestCase):
    def setUp(self):
        self.writer_Jon = Writer(username = 'Jon',password = 'testing', email = 'jon@winterfell.com')
        self.new_blog = Blog(post = 'some dummy blog', writer = self.writer_Jon)


    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog, Blog))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.post,'some dummy blog')
        self.assertEquals(self.new_blog.writer,self.writer_Jon)
