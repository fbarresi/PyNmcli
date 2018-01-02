import unittest

import pynmcli


class CliTests(unittest.TestCase):

    def test_base_command(self):
        command = pynmcli.NetworkManager('--version').command

        self.assertEqual(command, 'nmcli --version')

    def test_shell_command(self):
        result = pynmcli.NetworkManager('--version').execute()
        assert result.find('nmcli tool, version') != -1
