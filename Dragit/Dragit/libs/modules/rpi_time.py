#!/usr/bin/python
from datetime import datetime
import ds1302


class DS1302:
	def __init__(self, rangechecks=True):
		self.rangechecks = rangechecks
		ds1302.init_clock()

	def get_datetime(self):
		if not self.check_sanity():
			# if clock are insane: try to reset it
			self.reset_clock()
			# if clock are still insane: return None
			if not self.check_sanity():
				return None
		year, month, day = ds1302.get_date()
		hour, minute, second = ds1302.get_time()
		return datetime(year, month, day,
						hour, minute, second)

	def set_datetime(self, date, time):
		if not self.check_sanity():
			# if clock are insane: try to reset it
			self.reset_clock()
			# if clock are still insane: return False
			if not self.check_sanity():
				return False
		year   = int(date[0])
		month  = int(date[1])
		day    = int(date[2])
		hour   = int(time[0])
		minute = int(time[1])
		second = int(time[2])
		if year<1900 or year>3000:
			year = 2017
			print("year   out of range, set to default")
		if month not in range(1, 13):
			month = 6
			print("month  out of range, set to default")
		if day not in range(1, 32):
			day = 9
			print("day    out of range, set to default")
		if hour not in range(0, 24):
			hour = 0
			print("hour   out of range, set to default")
		if minute not in range(0, 60):
			minute = 0
			print("minute out of range, set to default")
		if second not in range(0, 60):
			second = 0
			print("second out of range, set to default")

		ds1302.set_date(year, month, day)
		ds1302.set_time(hour, minute, second)
		return True

	def check_sanity(self):
		"check sanity of a clock. returns True if clock is sane and False otherwise"
		year, month, day = ds1302.get_date()
		hours, mins, secs = ds1302.get_time()
		if year == 2000 or month == 0 or day == 0:
			return False
		if secs == 80:
			return False
		return True

	def reset_clock(self):
		ds1302.reset_clock()

def format_time(dt):
	if dt is None:
		return ""
	fmt = "%m/%d/%Y %H:%M"
	return dt.strftime(fmt)

def parse_time(s):
	fmt = "%m/%d/%Y %H:%M"
	return datetime.strptime(s, fmt)


