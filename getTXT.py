# -*- coding: utf-8 -*-

import readCSV
import getchlistfromhtml
import time
import signal

urlArr = readCSV.getURL("browserHistory.csv")



def handler(signum,frame):
	raise AssertionError

'''
#initialize : delete the record of all txt file
file_arr=["CSDN.txt","zhihu.txt","buptbbs.txt","ustcbbs.txt","baiduQA.txt","othersites.txt"]
for filename in file_arr:
	delf = open(filename,'w')
	delf.close() 
'''
print "-"
print "--------------------------------------------------------"
print "- Initialize txt_files success , empty is a good start ! "
print "--------------------------------------------------------"
print "-"


count = 12189

for url in urlArr[12189:]:
	
	try:
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(60)
	
		wdlist = getchlistfromhtml.getChListFromHtml(url)
		fenci=",".join(wdlist)
	
		#restore the string:fenci
		if(url.find('csdn')!=-1):
			filename = "CSDN.txt"
		elif(url.find('zhihu')!=-1):
			filename = "zhihu.txt"
		elif(url.find('byr')!=-1):
			filename = "buptbbs.txt"
		elif(url.find('ustc')!=-1):
			filename = "ustcbbs.txt"
		elif(url.find('baidu')!=-1):
			filename = "baiduQA.txt"
		else:
			filename = "othersites.txt"
	
		print "---  url_id = ",count
		print "--- ",url
		print "--- ",filename," add a new list ! "
		print "-------------------------------"
		print "-"
	
	
		fo = open(filename,'a')
		fo.write(str(count)+'-'+filename[0:-4]+':')
		fo.write(fenci.encode('utf-8'))
		fo.write('\n')
		#time.sleep(2)
		fo.close()
		count += 1
		signal.alarm(0)
	except AssertionError:
		print "---  url_id = ",count
		print "--- ",url
		print "--- timeout XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
		print "-------------------------------"
		print "-"
		count += 1
	
	
	
	
