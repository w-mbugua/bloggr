import unittest
from app.models import Writer, Comment, Blog

class CommentModelCase(unittest.TestCase):
    def setUp(self):
        self.author_Jon = Writer(username = 'Jon',password = 'testing', email = 'jon@jonson.com')
        self.new_blog = Blog(post = 'some dummy blog', writer = self.author_Jon)
        self.new_comment = Comment(blog_id = 15, body = "some rude comment")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.body,'some rude comment')
        self.assertEquals(self.new_comment.blog_id, 15)

