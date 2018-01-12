import urllib2
import requests
import threading
import time


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


def create_tuple(article):
	tup = (article['source']['id'],article['title'],article['url'],article['description'],article['publishedAt'])

	return tup

def create_url_info(url):
	
	response = requests.get(url)
	json_dict = response.json()
	list_art = []

	for i in range(len(json_dict['articles'])):
		
		info_tuple = create_tuple(json_dict['articles'][i])
		list_art.append(info_tuple)

	

	#print "in create url"


def single_thread_request(import_urls):
	print "starting single thread clock"
	t0 = time.clock()

	for line in import_urls:
		url = line.strip()

		if is_URL_valid(url):
			create_url_info(url)


	time_taken = time.clock() - t0
	print "single thread time"
	print time_taken

	



def multi_thread_request(import_urls):
	print "start multithread clock"
	t0 = time.clock()
	
	threads = []

	for line in import_urls:
		url = line.strip()

		if is_URL_valid(url):
			t = threading.Thread(target=create_url_info, args=(url,))

			threads.append(t)
		
	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()
	
	
	time_taken = time.clock() - t0
	print "multi time"
	print time_taken
