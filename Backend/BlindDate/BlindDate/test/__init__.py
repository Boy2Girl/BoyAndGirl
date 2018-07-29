import sys, os

from model import UserModel
from publicdata import Role

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import time
from factory.BlFactory import userBl


class ConversationTest(unittest.TestCase):
    def setUp(self):
        self.user_bl = userBl

    def test_update(self):
        self.assertLessEqual(self.user_bl.sign_up(UserModel("law", "123456", Role.USER)), 10)


if __name__ == '__main__':
    unittest.main()