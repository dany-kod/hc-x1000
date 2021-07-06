import os
import signal


class killRouge():
	def kill_child(child_pid):
		if child_pid is None:
			pass
		else:
			os.kill(child_pid, signal.SIGTERM)
	
