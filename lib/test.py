from lib.server import hcXSERVER as hc
# this will find our local systems ip address for us.
class testSystem():
	def main():
		what = hc.getTracks();
		if what is None :
			return "failed"
		print(what)
		return what