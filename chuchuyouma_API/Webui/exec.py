import tc.test_login
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(tc.test_login.test_login('login_sucess'))
    suite.addTest(tc.test_login.test_login('login_user_fail'))
    runner = unittest.TextTestRunner()
    runner.run(suite)