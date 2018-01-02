import unittest

from pynmcli import NetworkManager


class CliTests(unittest.TestCase):

    def test_base_command(self):
        command = NetworkManager.NetworkManager('--version').command

        self.assertEqual(command, 'nmcli --version')

    def test_shell_command(self):
        result = NetworkManager.NetworkManager('--version').execute()
        print(result)
        assert result.startswith('nmcli tool, version')
