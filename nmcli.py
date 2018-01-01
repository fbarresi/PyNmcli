class nmcli(object):
	"""doc under: https://developer.gnome.org/NetworkManager/stable/nmcli.html """
	def __init__(self, *args):
		self.command = 'nmcli '
		for arg in args:
			self.command += arg
	
	def execute(self):
		pass
		

class NetworkManager(nmcli):
	def __init__(self, *args):
		super(NetworkManager, self).__init__()
		for arg in args:
			self.command += arg
		

	class Device(nmcli):
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


		def set(self, *args):
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


if __name__ == '__main__':
	nm = NetworkManager('--version')
	print(nm.command)

	d = NetworkManager.Device().wifi('list')
	print(d.command) 