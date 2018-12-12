*************************
PyNmcli
*************************

.. image:: https://travis-ci.org/fbarresi/PyNmcli.svg?branch=master
    :alt: Travis CI build status

Simple python interface to Network Manager CLI

PyNmcli provides a easy to use python (2.7+ or 3+) interface to Network Manager CLI.
Official documentation of nmcli under: https://developer.gnome.org/NetworkManager/stable/nmcli.html

Dependencies
========

This project has no dependencies and works with python 2.7+ (python 3 as well)

This package directly uses ``Network-Manager``.

Your can install it running the following command from shell: ::

	sudo apt-get install network-manager

Installation
========

You may install this package in two ways:

- Compile from code ::

    git clone https://github.com/fbarresi/PyNmcli.git
    cd PyNmcli
    python setup.py install

- Pypi ::

    pip install pynmcli

Usage
========

Just import the package::

    import pynmcli

and call Network Manager function just like: ::

    result = pynmcli.NetworkManager('--version').execute()

or ::

    result = pynmcli.NetworkManager.Device().wifi('list').execute()

you can also use some built-in help methods in order to convert output tables in more handy python dictionaries: ::

    wifi_dict = pynmcli.get_data(pynmcli.NetworkManager.Device().wifi().execute())

Contribute
========

Whould you like to contribute to this project? YES, PLEASE!

Just fork this repository and submit your pull request.

Change log
========
- Version 1.0.5 - Fixed table-header handling

- Version 1.0.4 - Fixed localization issues in the use of nmcli

- Version 1.0.3 - Enhanced usability

- Version 1.0.2 - Added utils for converting cli outputs into python dicts 

- Version 1.0.1 - First working release

- Version 1.0.0 - Test release
