//测试TCP的慢启动,内容为<HTTP权威指南> 
var net = require('net');
var fs = require('fs');
var socket_client = new net.Socket();
socket_client.setKeepAlive(true);
socket_client.connect(65535, "localhost", function() {
	console.log('start to send data info');
	var fd = fs.openSync('/tmp/big.data', 'r');
	fs.read(fd,12*1024*1024,0,'utf-8', function(err,data, buffer) {
		console.log("start to send file data");
		socket_client.write(data);
		socket_client.on('data', function(data) {
			console.log(data.toString());
			socket_client.destroy();
		})
		socket_client.on('close', function() {
			console.log('close!');
		})
	});
});
