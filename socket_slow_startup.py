#coding=UTF-8
'''
测试TCP的慢启动,内容为<HTTP权威指南> P89
'''
from socket import *
from time import *
import traceback

def createServer():
	HOST=''
	PORT=65535
	BUFSIZE=1024
	ADDR=(HOST,PORT)
	tcp=socket(AF_INET,SOCK_STREAM)
	tcp.bind(ADDR)
	tcp.settimeout(1)
	tcp.setblocking(1)
	tcp.listen(10)
	data=[]
	while True:
		try:
			print 'Wating for data'
			tcpAccept=tcp.accept()
			remoteData=tcpAccept[0]
			startTime=time()
			print 'recevieData from ',tcpAccept[1]
			output=open("/tmp/big.data.in","wb")
			while True:
				recevieData=remoteData.recv(BUFSIZE)
				output.write(recevieData)
				if len(recevieData)<1024:
					break
			output.close()
				#print 'send back'
				#remoteData.send('[%s]%s'%(ctime(),'close!'))
			print 'it takes %ssseconds !'%((time()-startTime))
		except KeyboardInterrupt:
			tcp.close()
			exit()
		except Exception,e:
			print traceback.format_exc()
	#tcp.close()
if __name__ == '__main__':
	createServer()
