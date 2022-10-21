
from analyzer import runtime_analyzer
import argparse


if __name__ == "__main__":

	# parse args
	parser = argparse.ArgumentParser(description="load runtime analyzer")
	parser.add_argument("-f", "--filename", type=str, help="log file")
	parser.add_argument("-g", "--graphname", type=str, default="log_plot.png", help="name of the graph plot")
	parser.add_argument("-d", "--display", type=str, default="no", help="(yes/no) display the output")
	args = parser.parse_args()
	print(args.graphname)
	if args.display:
		import matplotlib.pyplot as plt

	runtime_analyzer(args.filename, args.graphname, args.display)
	print("Analysis done!")