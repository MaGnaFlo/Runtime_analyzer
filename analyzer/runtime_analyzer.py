import numpy as np 
import matplotlib.pyplot as plt 
import time
from analyzer import Analyzer


if __name__ == "__main__":

	file = "../data/mylog.tl"
	analyzer = Analyzer(file)
	analyzer.scan()
	fig, ax = analyzer.plot()
	plt.show()
	analyzer.save("log_chart")