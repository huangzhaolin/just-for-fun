#coding=UTF-8
'''
测试TCP的慢启动,内容为<HTTP权威指南> P89
'''
from socket import *
from time import ctime

def createServer():
	HOST='localhost'
	PORT=65535
	BUFSIZE=1024
	ADDR=(HOST,PORT)
	tcp=socket(AF_INET,SOCK_STREAM)
	tcp.bind(ADDR)
	tcp.listen(1)
	while True:
		print 'Wating for data'
		tcp,fromAddr=tcp.accept()
		print 'get data from :%s'%fromAddr
		while True:
			data=tcp.recv(BUFSIZE)
			if not data:
				break
			tcp.send('[%s]%s'%(ctime()),'recvied')
			#tcp.close()
	tcp.close()
if __name__ == '__main__':
	createServer()
