from pynmcli.Networkmanager import Networkmanager as cli
from pynmcli.utils import get_data


__version__ = '1.0.3'


if __name__ == '__main__':
    print(cli.NetworkManager('--version').execute())
    print(get_data(cli.NetworkManager.Device().wifi('list').execute()))