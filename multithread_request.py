import urllib2
import requests


def is_URL_valid(URL):

	try:
		urllib2.urlopen(URL)		
		return True
	except ValueError, ex:
		sys.stderr.write("This URL is not valid")		
		return False
	except urllib2.URLError, ex:
		sys.stderr.write("This URL is not valid")		
		return False


def single_thread_request(list_url):



def time_taken_multi = multi_thread_request(list_url):


