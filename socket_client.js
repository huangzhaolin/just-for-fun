//测试TCP的慢启动,内容为<HTTP权威指南> P89 客户端
var net = require('net');
var fs=require('fs');
var socket_client=new net.Socket();
socket_client.setKeepAlive(true);
socket_client.connect(65535,"localhost",function(){
	console.log('start to send data info');
	socket_client.write("data");
	// fs.readFile('/tmp/big.data',function(err,data){
	// 	socket_client.write(data);
	// });
});
socket_client.on('data',function(data){
	console.log(data);
	socket_client.destroy();
})
socket_client.on('close',function(){
	console.log('close!');
})