#coding=UTF-8
'''
测试TCP的慢启动,内容为<HTTP权威指南> P89
'''
from socket import *
from time import ctime
import traceback

def createServer():
	HOST=''
	PORT=65535
	BUFSIZE=1024
	ADDR=(HOST,PORT)
	tcp=socket(AF_INET,SOCK_STREAM)
	tcp.bind(ADDR)
	tcp.listen(10)
	while True:
		try:
			print 'Wating for data'
			tcpAccept=tcp.accept()
			remoteData=tcpAccept[0]
			print 'get data from :',tcpAccept[1]
			while True:
				data=remoteData.recv(BUFSIZE)
				if not data:
					break
				print data
				#tcp.send('[%s]%s'%(ctime(),data))
				#tcp.close()
		except Exception,e:
			print traceback.format_exc()
	#tcp.close()
if __name__ == '__main__':
	createServer()