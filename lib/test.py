



# this will find our local systems ip address for us.
class testSystem():
	global trackPid

	def main():
		if trackPid is None :
			return "failed"
		print(trackPid)
		return trackPid