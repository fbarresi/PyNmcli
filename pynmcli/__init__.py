from .NetworkManager import NetworkManager
from .utils import get_data

__version__ = '1.0.3'


if __name__ == '__main__':
    print(pynmcli.NetworkManager('--version').execute())
    print(pynmcli.get_data(pynmcli.NetworkManager.Device().wifi('list').execute()))