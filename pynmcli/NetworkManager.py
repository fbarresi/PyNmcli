from .cli import execute_shell


class Nmcli(object):
    """doc under: https://developer.gnome.org/NetworkManager/stable/nmcli.html """
    def __init__(self, *args):
        self.command = 'nmcli '
        for arg in args:
            self.command += arg

    def execute(self):
        return execute_shell(self.command)


class NetworkManager(Nmcli):
    def __init__(self, *args):
        super(NetworkManager, self).__init__()
        for arg in args:
            self.command += arg

    class General(Nmcli):
        def __init__(self, *args):
            super(NetworkManager.General, self).__init__()
            self.command += 'general '
            for arg in args:
                self.command += arg

        def status(self):
            self.command += 'status'
            return self

        def hostname(self, *args):
            self.command += 'hostname'
            for arg in args:
                self.command += arg
            return self

        def permissions(self):
            self.command += 'permissions'
            return self

        def logging(self, *args):
            self.command += 'logging '
            for arg in args:
                self.command += arg
            return self

    class Networking(Nmcli):
        def __init__(self, *args):
            super(NetworkManager.Networking, self).__init__()
            self.command += 'networking '
            for arg in args:
                self.command += arg

        def on(self):
            self.command += 'on'
            return self

        def off(self):
            self.command += 'off'
            return self

        def connectivity(self, *args):
            self.command += 'connectivity '
            for arg in args:
                self.command += arg
            return self

    class Radio(Nmcli):
        def __init__(self, *args):
            super(NetworkManager.Radio, self).__init__()
            self.command += 'radio '
            for arg in args:
                self.command += arg

        def wifi(self, *args):
            self.command += 'wifi '
            for arg in args:
                self.command += arg
            return self

        def wwan(self, *args):
            self.command += 'wwan '
            for arg in args:
                self.command += arg
            return self

        def all(self, *args):
            self.command += 'all '
            for arg in args:
                self.command += arg
            return self

    class Connection(Nmcli):
        def __init__(self, *args):
            super(NetworkManager.Connection, self).__init__()
            self.command += 'connection '
            for arg in args:
                self.command += arg

        def show(self, *args):
            self.command += 'show '
            for arg in args:
                self.command += arg
            return self

        def up(self, *args):
            self.command += 'up '
            for arg in args:
                self.command += arg
            return self

        def down(self, *args):
            self.command += 'down '
            for arg in args:
                self.command += arg
            return self

        def modify(self, *args):
            self.command += 'modify '
            for arg in args:
                self.command += arg
            return self

        def add(self, *args):
            self.command += 'add '
            for arg in args:
                self.command += arg
            return self

        def edit(self, *args):
            self.command += 'edit '
            for arg in args:
                self.command += arg
            return self

        def clone(self, *args):
            self.command += 'clone '
            for arg in args:
                self.command += arg
            return self

        def delete(self, *args):
            self.command += 'delete '
            for arg in args:
                self.command += arg
            return self

        def monitor(self, *args):
            self.command += 'monitor '
            for arg in args:
                self.command += arg
            return self

        def reload(self):
            self.command += 'reload '
            return self

        def load(self, *args):
            self.command += 'load '
            for arg in args:
                self.command += arg
            return self

        def import_configuration(self, *args):
            self.command += 'import '
            for arg in args:
                self.command += arg
            return self

        def export(self, *args):
            self.command += 'export '
            for arg in args:
                self.command += arg
            return self

    class Device(Nmcli):
        def __init__(self, *args):
            super(NetworkManager.Device, self).__init__()
            self.command += 'device '
            for arg in args:
                self.command += arg

        def status(self, *args):
            self.command += 'status '
            for arg in args:
                self.command += arg
            return self

        def show(self, *args):
            self.command += 'show '
            for arg in args:
                self.command += arg
            return self

        def set_properties(self, *args):
            self.command += 'set '
            for arg in args:
                self.command += arg
            return self

        def connect(self, *args):
            self.command += 'connect '
            for arg in args:
                self.command += arg
            return self

        def reapply(self, *args):
            self.command += 'reapply '
            for arg in args:
                self.command += arg
            return self

        def modify(self, *args):
            self.command += 'modify '
            for arg in args:
                self.command += arg
            return self

        def disconnect(self, *args):
            self.command += 'disconnect '
            for arg in args:
                self.command += arg
            return self

        def delete(self, *args):
            self.command += 'delete '
            for arg in args:
                self.command += arg
            return self

        def monitor(self, *args):
            self.command += 'monitor '
            for arg in args:
                self.command += arg
            return self

        def wifi(self, *args):
            self.command += 'wifi '
            for arg in args:
                self.command += arg
            return self

        def lldp(self, *args):
            self.command += 'lldp '
            for arg in args:
                self.command += arg
            return self
