#coding=UTF-8
'''
测试TCP的慢启动,内容为<HTTP权威指南> P89 客户端
'''
from socket import *
from time import *
import traceback

def createClient():
	HOST='jolinhuang.com'
	PORT=65535
	BUFSIZE=1024
	ADDR=(HOST,PORT)
	tcp=socket(AF_INET,SOCK_STREAM)
	tcp.connect(ADDR)
	data=[]
	try:
		print 'Wating for data'
		print 'starting send data:%s'%time()
		output=open("/tmp/big.data","r")
		buffer=[]
		count=0
#		for line in output:
#			buffer.append(line)
#			if len(buffer)==10:
#				print "it's %s time send"%count
#				tcp.send(line)
#				tcp.recv(1024)
		tcp.send(output.readall())
		tcp.recv(1024)
		print 'ending send data:%s'%time()
	except KeyboardInterrupt:
		tcp.close()
		exit()
	except Exception,e:
		print traceback.format_exc()
	#tcp.close()
if __name__ == '__main__':
	createClient()
