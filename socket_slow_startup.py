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
	tcp.setblocking(1)
	tcp.listen(10)
	data=[]
	while True:
		try:
			print 'Wating for data'
			tcpAccept=tcp.accept()
			remoteData=tcpAccept[0]
			print 'starting received data:%s'%ctime()
			output=open("/tmp/big.data.in%s"%ctime(),"w")
			while True:
				data.append(remoteData.recv(BUFSIZE))
				if not data:
					break
				if len(data)>10240:
					output.write(data)
					data=None
			output.close()
			print '[%s] ending!'%(ctime())
			remoteData.send('[%s]%s'%(ctime(),'close!'))
		except KeyboardInterrupt:
			tcp.close()
			exit()
		except Exception,e:
			print traceback.format_exc()
	#tcp.close()
if __name__ == '__main__':
	createServer()
