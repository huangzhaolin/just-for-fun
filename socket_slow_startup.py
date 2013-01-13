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
	tcp.setblocking(1)
	tcp.listen(10)
	data=[]
	while True:
		try:
			print 'Wating for data'
			tcpAccept=tcp.accept()
			remoteData=tcpAccept[0]
			startTime=time()
			output=open("/tmp/big.data.in%s"%time(),"w")
			while True:
				recevieData=remoteData.recv(BUFSIZE)
				print bool(recevieData)
				if (not recevieData) or len(data)>10:
					print "im in %s"%recevieData
					output.write(str(data))
					data=[]
					break
				else:
					print 'hello'
					data.append(recevieData)
			output.close()
			print 'it takes %s s ending!'%((time()-startTime)%1000)
			remoteData.send('[%s]%s'%(ctime(),'close!'))
		except KeyboardInterrupt:
			tcp.close()
			exit()
		except Exception,e:
			print traceback.format_exc()
	#tcp.close()
if __name__ == '__main__':
	createServer()
