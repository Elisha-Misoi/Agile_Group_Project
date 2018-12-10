import unittest
from user import User
from comment import Comment
from admin import Admin
from moderator import Moderator

class UserTestCase(unittest.TestCase):
  def setUp(self):
    self.user1 = User('JohnPaul', 'password')
    self.mod1 = Moderator('Elisha', 'password')
    self.admin1 = Admin('Anthonny', 'admin')
    self.username = "Test user"
    self.comment = Comment(self.user1, 'Hello world')
    self.new_comment = "Hello World"
    self.edit_comment = Admin.edit_comment
    self.delete_comment = Admin.delete_comment

  def test_instantiation(self):
    self.assertIsInstance(self.mod1, User, 'Moderator is a user')
    self.assertIsInstance(self.admin1, User, 'Admin is a user')

  def test_username_is_set(self):
    self.assertEqual(self.user1.username,'JohnPaul', 'User name is set')
    self.assertEqual(self.mod1.username,'Elisha', 'User name is set')
    self.assertEqual(self.admin1.username,'Anthonny', 'User name is set')

  def test_admin_can_edit_comment(self):
    self.assertTrue(self.admin1.edit_comment(self.comment, self.new_comment))
  
  def test_admin_can_delete_comment(self):
    self.assertTrue(self.admin1.delete_comment(self.comment))

  def test_moderator_can_delete_comment(self):
    self.assertTrue(self.mod1.delete_comment(self.comment))
    