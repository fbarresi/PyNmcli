import unittest

import pynmcli


class CliTests(unittest.TestCase):

    def test_base_command(self):
        command = cli.NetworkManager('--version').command

        self.assertEqual(command, 'nmcli --version')

    def test_shell_command(self):
        result = cli.NetworkManager('--version').execute()
        assert result.find('nmcli tool, version') != -1
