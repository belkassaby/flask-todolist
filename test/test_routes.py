""" Tests for the routes """
from test import BaseTestCase
import requests


class RoutesTest(BaseTestCase):
    """
    A class to test the user endpoints. It uses the LDAP mock
    server and mock entry with a test user
    """

    def test_login(self):
        """
        Test that the login works
        Note: this is likely to fail
        """
        # login here
        login_url = '/login' # make sure that this is the correct URL
        # Add a headers if necessary
        auth_header = {}
        response = requests.get(login_url, headers=auth_header)
        json_resp = response.json()
        # make sure that the response returns a json with the 'message' key
        login_message = json_resp['message']
        # check that the message and the expected message are equal
        self.assertEqual(login_message, 'Expected Login Message')

    def test_logout(self):
        """
        Test that the logout works
        """
        # logout here
        # TODO
        # self.assertEqual('Logout Result Message', 'Expected Logout Message')

    def test_complete(self):
        """

        :return:
        """
        # TODO

    def test_delete(self):
        """

        :return:
        """
        # TODO

    def update(self):
        """

        :return:
        """
        # TODO
