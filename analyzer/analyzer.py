import numpy as np 
import matplotlib.pyplot as plt 

'''
Class for analyzing the time spent by a function of part of a program
and subdivide its parts in a pie chart. The analyzes takes a core file into
account, which is a log file generated by the targetted software. 

The current version supports this type of log format (ignore '>'):
	> func_name1: 45.2 sec
	> func_name2: 2.0 sec
	> ...
	> func_name1897: 12.7 sec
	> total (big func): 15897 sec

Considers only one 'total' function (16/10/2022).
'''

TOTAL = "Total"
UNTRACKED = "Untracked"
GRAY = '#838B8B'

class Analyzer:
	# init arg: the path/name of the log file
	def __init__(self, file, parts_only=False):
		self.file = file
		self.func_time = {}
		self.total = {}
		self.parts_only = parts_only

	# scans the log line by line.
	# Arg is tolerance for accounting untracked time (untracked_t > tolerance)
	def scan(self, tolerance=0.01):
		with open(self.file) as f:
			for line in f:
				func, time = line.split(': ')
				time = time.split(' sec')[0]
				print(func)
				if func.lower().find(TOTAL.lower()) != -1 and not self.parts_only:
					func = func.split('[')[1].split(']')[0]
					self.total[func] = float(time)
				else:
					self.func_time[func] = float(time)

			if len(self.total) > 0:
				untracked_time = list(self.total.values())[0] - sum(list(self.func_time.values()))
				if untracked_time > tolerance:
					self.func_time[UNTRACKED] = untracked_time


	# generates a pie chart
	def plot(self):
		# utility func to print the values
		def text_plot(pct, values):
		    absolute = pct/100.*np.sum(values)
		    return "{:.1f}%\n({:.1f} s)".format(pct, absolute)

		fig, ax = plt.subplots(1, 2, figsize=(10,5))

		total_labels = list(self.total.keys())
		total_values = list(self.total.values())

		sub_number = len(self.func_time)
		sub_labels = list(self.func_time.keys())
		sub_values = list(self.func_time.values())

		# colors
		if sub_number <= 10:
			sub_colors = dict(zip(sub_labels, plt.cm.tab10.colors[:len(sub_labels)]))
		else:
			sub_colors = dict(zip(sub_labels, plt.cm.tab20.colors[:len(sub_labels)]))
		sub_colors[UNTRACKED] = GRAY
		sub_colors = [sub_colors[key] for key in sub_labels]

		# total func
		ax[0].pie(list(self.total.values()), 
			   labels=total_labels,
			   autopct=lambda pct: text_plot(pct, total_values),
			   radius=1.2)

		# subfuncs
		ax[1].pie(sub_values, 
			   labels=sub_labels,
			   autopct=lambda pct: text_plot(pct, sub_values),
			   radius=1.2,
			   colors=sub_colors)
		self.fig = fig
		return fig, ax

	# save the pie chart. Arg is the name of the out png (ex: "myfig" (no extension))
	# and a specific path.
	def save(self, figname, path="", dpi=300):
		if path != "" and path[-1] != '/' and path[-1] != '\\':
			path += '/'
		self.fig.savefig(path + figname + ".png", dpi=dpi)
		
		if path=="":
			path = "ROOT/"
		print("File saved as " + figname.split('/')[-1].split('\\')[-1] + ".png in " + path)