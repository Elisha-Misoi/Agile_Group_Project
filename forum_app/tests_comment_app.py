import unittest
from user import User
from comment import Comment
from admin import Admin
from moderator import Moderator

class UserTestCase(unittest.TestCase):
  def setUp(self):
    self.user1 = User('JohnPaul')
    self.mod1 = Moderator('Elisha')
    self.admin1 = Admin('Anthonny')
    self.comment = "Hello"
    self.new_comment = "Hello World"
    self.edit_comment = User.edit_comment
    self.delete_comment = User.delete_comment
    self.log_in = User.log_in

  def test_instantiation(self):
    self.assertIsInstance(self.mod1, self.user1, 'Moderator is a user')
    self.assertIsInstance(self.admin1, self.user1, 'Admin is a user')

  def test_username_is_set(self):
    self.assertEqual(self.user1.username,'JohnPaul', 'User name is set')
    self.assertEqual(self.mod1.username,'Elisha', 'User name is set')
    self.assertEqual(self.admin1.username,'Anthonny', 'User name is set')

  def test_admin_can_edit_comment(self):
    self.assertTrue(self.edit_comment(self, self.comment, self.new_comment))
  
  def test_admin_can_delete_comment(self):
    self.assertTrue(self.delete_comment(self, self.comment))

  def test_moderator_can_delete_comment(self):
    self.assertTrue(self, self.delete_comment(self, self.comment))

  def test_user_can_login(self):
    self.assertTrue(self.log_in(self, "username", "password"))