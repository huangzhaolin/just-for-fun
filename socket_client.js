//娴嬭瘯TCP鐨勬參鍚姩,鍐呭涓�HTTP鏉冨▉鎸囧崡> P89 瀹㈡埛绔�var net = require('net');
var fs=require('fs');
var socket_client=new net.Socket();
socket_client.setKeepAlive(true);
socket_client.connect(8888,"localhost",function(){
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