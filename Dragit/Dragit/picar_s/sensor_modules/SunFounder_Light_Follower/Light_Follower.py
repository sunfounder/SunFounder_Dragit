import math
import time

class Light_Follower(object):
	"""docstring for light_follower_module"""
	def __init__(self, chn0=0, chn1=1, chn2=2, references=[10, 10, 10], analog_function=None):
		self._references = references
		if analog_function == None:
			self.read_analog = None
		else:
			self.analog_function = analog_function
		self._channel0 = chn0
		self._channel1 = chn1
		self._channel2 = chn2

	@property
	def analog_function(self):
		return self.read_analog

	@analog_function.setter
	def analog_function(self, func):
		self.read_analog = func
		self._analog_func_avalible()

	def _analog_func_avalible(self):
		try:
			self.read_analog(self._channel0)
			self.read_analog(self._channel1)
			self.read_analog(self._channel2)
			return True
		except:
			raise ValueError("analog function setup error, please set the analog with a callable function with 'analog_function = <analog function>'")

	def read_analogs(self):
		if self._analog_func_avalible():
			analog_result = [0, 0, 0]
			analog_result[0] = self.read_analog(self._channel0)
			analog_result[1] = self.read_analog(self._channel1)
			analog_result[2] = self.read_analog(self._channel2)
			return analog_result

	def read_digital(self):
		analog_list = self.read_analogs()
		#print "Analog_result = %s, References = %s "%(lt, self._references)
		digital_list = []
		for i in range(0, 3):
			if analog_list[i] >= self._references[i]:
				digital_list.append(0)
			elif analog_list[i] < self._references[i]:
				digital_list.append(1)
		return digital_list

	def read_flashlight(self):
		mount = 50
		lt = [0, 0, 0]
		lt_list = [[], [], []]
		for times in range(0, mount):
			lt = self.read_digital()
			for lt_id in range(0, 3):
				lt_list[lt_id].append(lt[lt_id])
		for lt_id in range(0, 3):
			if lt_list[lt_id].count(1) > 3:
				lt[lt_id] = 1
			else:
				lt[lt_id] = 0
			#print "lt_id = %d   count(1) = %d   count(0) = %d"%(lt_id,lt_list[lt_id].count(1),lt_list[lt_id].count(0)) 
		return lt

	def get_average(self, mount):
		if not isinstance(mount, int):
			raise ValueError("Mount must be interger")
		average = [0, 0, 0]
		lt_list = [[], [], []]
		for times in range(0, mount):
			lt = self.read_analogs()
			for lt_id in range(0, 3):
				lt_list[lt_id].append(lt[lt_id])
		for lt_id in range(0, 3):
			average[lt_id] = int(math.fsum(lt_list[lt_id])/mount)
		return average

	def found_light_in(self, timeout):
		if isinstance(timeout, int) or isinstance(timeout, float):
			pass
		else:
			raise ValueError("timeout must be interger or float")
		time_start = time.time()
		time_during = 0
		while time_during < timeout:
			lt_status = self.read_digital()
			result = 0
			if 1 in lt_status:
				return lt_status
			time_now = time.time()
			time_during = time_now - time_start
		return False

	def wait_tile_status(self, status):
		while True:
			lt_status = self.read_digital()
			if lt_status in status:
				break

	def wait_tile_center(self):
		while True:
			lt_status = self.read_digital()
			if lt_status[1] == 1:
				break

	@property
	def references(self):
		return self._references
	
	@references.setter
	def references(self, value):
		self._references = value

