import multithread_request as mreq
import sys
import time


def main():

	input_file = sys.stdin.readlines()
	
	
	time_taken_single = mreq.single_thread_request(input_file)

	t0 = time.clock()
	time_taken_multi = mreq.multi_thread_request(input_file)
	time_taken = time.clock() - t0

	print "time taken"
	print time_taken
	
	
	


if __name__ == '__main__':
	main()
