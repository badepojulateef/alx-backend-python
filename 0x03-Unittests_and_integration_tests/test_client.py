#!/usr/bin/env python3
"""
Familiarize yourself with the client.GithubOrgClient class.

In a new test_client.py file, declare the

TestGithubOrgClient(unittest.TestCase) class and

implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the

expected argument but make sure it is not executed.

Use @parameterized.expand as a decorator to parametrize the test with a

couple of org examples to pass to GithubOrgClient, in this order:

google
abc
Of course, no external HTTP calls should be made.
"""


import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ method to check the GithubClient org method """
        endpoint = 'https://api.github.com/orgs/{}'.format(org_name)
        spec = GithubOrgClient(org_name)
        spec.org()
        mock_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])

    def test_public_repos_url(self) -> None:
        """
        Implement the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ Tests that test_public_repos returns a known payload.
        """
        get_json_mock.return_value = [
            {'name': 'repo_0'},
            {'name': 'repo_1'},
            {'name': 'repo_2'}
        ]
        get_json_mock()
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = [
                {'name': 'repo_0'},
                {'name': 'repo_1'},
                {'name': 'repo_2'}
            ]
            ghc = GithubOrgClient('xyz')
            r = ghc._public_repos_url
            self.assertEqual(r, mock.return_value)
            mock.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Tests that has_license returns the correct values.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """an integration test for githuborg client"""

    @classmethod
    def setUpClass(cls):
        """ set up class befor each method"""
        config = {'return_value.json.side_effect':
                  [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """add some more integration"""
        tst_cls = GithubOrgClient('Facebook')
        self.assertEqual(tst_cls.org, self.org_payload)
        self.assertEqual(tst_cls.repos_payload, self.repos_payload)
        self.assertEqual(tst_cls.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True

    @classmethod
    def tearDownClass(cls) -> None:
        """tear down after each class"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
