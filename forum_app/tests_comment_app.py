import unittest
import user, comment, moderator, admin

class UserTestCase(unittest.TestCase):
  def setUp(self):
    user1 = User('JohnPaul')
    mod1 = Moderator('Elisha')
    admin1 = Admin('Anthonny')
    comment = "Hello"
    new_comment = "Hello World"

  def test_instantiation(self):
    self.assertIsInstance(mod1, user1, 'Moderator is a user')
    self.assertIsInstance(admin1, user1, 'Admin is a user')

  def test_username_is_set(self):
    self.assertEqual(user1.name,'JohnPaul', 'User name is set')
    self.assertEqual(mod1.name,'Elisha', 'User name is set')
    self.assertEqual(admin1.name,'Anthonny', 'User name is set')

  def test_admin_can_edit_comment(self):
    self.assertTrue(edit_comment(comment, new_comment))
  
  def test_admin_can_delete_comment(self):
    self.assertTrue(delete_comment(comment))

  def test_moderator_can_delete_comment(self):
    self.assertTrue(delete_comment(comment))

  def test_user_can_login(self):
    self.assertTrue(log_in("username", "password"))