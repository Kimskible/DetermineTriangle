import unittest
from user import validUsername

class test_username(unittest.TestCase):
  def test_username(self):
    self.assertEqual("Valid Username", validUsername("Kimmie"), "Valid Username")
    self.assertEqual("Valid Username", validUsername("eT6bk*"), "Valid Username")
    self.assertEqual("Valid Username", validUsername("randy5"), "Valid Username")
    self.assertNotEqual(validUsername("$Kimmie"), "Valid Username", "Invalid Username")
    self.assertNotEqual(validUsername("5randy"), "Valid Username", "Invalid Username")
    self.assertNotEqual(validUsername("$purple"), "Valid Username", "Invalid Username")


if __name__ == "__main__":
    unittest.main()