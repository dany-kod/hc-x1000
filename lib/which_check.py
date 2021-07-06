import subprocess as sp

# this will find our local systems ip address for us.
class checkInstalls():

	def main(whichCheck):
		findNode = sp.Popen(whichCheck, shell=True, stdout=sp.PIPE)
		findNode_return = findNode.stdout.read().strip()
		return findNode_return