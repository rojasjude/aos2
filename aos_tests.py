import unittest

import aos_methods as methods


class AosAppPositiveTestCases(unittest.TestCase):  # create class

    @staticmethod  # signal to unittest that this is a static method
    def test_create_aos():
        methods.setUp()
        methods.create_user()
        methods.check_text()
        methods.check_tab_menu()
        methods.check_logo()
        methods.contact_us()
        methods.check_social_media()
        methods.logout()
        methods.login()
        methods.logout()
        methods.tearDown()


if __name__ == "__main__":
    unittest.main()
