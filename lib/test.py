from lib.server import hcXSERVER
# this will find our local systems ip address for us.
class testSystem():
	def main():
		what = hcXSERVER.getTracks();
		if what is None :
			return "failed"
		print(what)
		return what