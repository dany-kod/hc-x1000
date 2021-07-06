import lib.server
# this will find our local systems ip address for us.
class testSystem():
	def main():
		what = lib.server.hcXSERVER.getTracks();
		if what is None :
			return "failed"
		print(what)
		return what