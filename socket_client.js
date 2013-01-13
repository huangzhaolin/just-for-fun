//测试TCP的慢启动,内容为<HTTP权威指南> P89 客户端
var net = require('net');
var fs=require('fs');
var socket=new net.Socket();
socket.setKeepAlive(true);
socket.connect(65535,"localhost",function()){
	console.log('start to send data info');
	fs.readFile('tmp/big.data',function(err,data){
		socket.write(data);
	});
}
socket.on('close',function(){
	console.log('close!');
})