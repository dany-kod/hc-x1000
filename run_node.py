import subprocess as sp

# this will find our local systems ip address for us.
class runNode():

	def main(nodejsCommand):
		nodeRun = sp.Popen(nodejsCommand, stdin=None, stdout=None, stderr=None, close_fds=True)
		return nodeRun.pid
