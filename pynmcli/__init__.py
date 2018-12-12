from .NetworkManager import NetworkManager
from .utils import get_data

__version__ = '1.0.5'


if __name__ == '__main__':
    print(NetworkManager('--version').execute())
    print(get_data(NetworkManager.Device().wifi('list').execute()))
