import Webui.tc.test_login
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Webui.tc.test_login.test_login('login_sucess'))
    # suite.addTest(Webui.tc.test_login.test_login('login_password_fail'))
    # suite.addTest(Webui.tc.test_login.test_login('login_username_fail'))
    suite.addTest(Webui.tc.test_login.test_login('checkloginout'))
    # suite.addTest(Webui.tc.test_login.test_login('create_logo'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

