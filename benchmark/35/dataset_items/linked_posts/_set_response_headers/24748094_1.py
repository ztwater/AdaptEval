$ curl -v -o - http://localhost:8000/static/js/test.js
* Adding handle: conn: 0x7f8ffa003a00
* Adding handle: send: 0
* Adding handle: recv: 0
* Curl_addHandleToPipeline: length: 1
* - Conn 0 (0x7f8ffa003a00) send_pipe: 1, recv_pipe: 0
* About to connect() to localhost port 8000 (#0)
*   Trying ::1...
*   Trying fe80::1...
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /static/js/test.js HTTP/1.1
> User-Agent: curl/7.30.0
> Host: localhost:8000
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Date: Tue, 15 Jul 2014 00:19:11 GMT
< Server: WSGIServer/0.1 Python/2.7.6
< Last-Modified: Tue, 15 Jul 2014 00:07:22 GMT
< Content-Length: 69
< Content-Type: application/javascript
< Accept-Ranges: bytes
< Cache-Control: public, max-age=604800
<
$(document).ready(function () {
    console.log("Hello World!");
});
* Closing connection 0
