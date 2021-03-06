### frontend 설정

##### index.js

```js
const express = require('express'); 
const app = express(); 
const http = require('http'); 
const server = http.createServer(app); 
const { Server } = require("socket.io"); 
const io = new Server(server); 

// localhost:3000으로 방문 시 index.html로 라우팅 
app.get('/', (req, res) => { 
    res.sendFile(__dirname + '/index.html'); 
}); 

// socket이 connection 상태일때 
io.on('connection', (socket) => { 
    socket.on('chat message', (msg) => { 
        io.emit('chat message', msg); 
        console.log('message: ' + msg); 
    }); 
    socket.on('disconnect', () => { 
        console.log('user disconnected'); 
    }); 
}); 

// server는 localhost:3000 
server.listen(3000, () => { 
    console.log('listening on *:3000'); 
});
```

##### index.html

```html
<!DOCTYPE html> 
<html> 
    <head> 
        <title>Socket.IO chat</title> 
        <style> 
        body { 
            margin: 0; 
            padding-bottom: 3rem; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
        } 
        #form { 
            background: rgba(0, 0, 0, 0.15); 
            padding: 0.25rem; position: fixed; 
            bottom: 0; left: 0; right: 0; display: flex; 
            height: 3rem; box-sizing: border-box; backdrop-filter: blur(10px); 
        } 
        #input { 
            border: none; padding: 0 1rem; flex-grow: 1; 
            border-radius: 2rem; margin: 0.25rem; 
        } 
        #input:focus { 
            outline: none; 
        } 
        #form > button { 
            background: #333; border: none; padding: 0 1rem; 
            margin: 0.25rem; border-radius: 3px; outline: none; color: #fff; 
        } 
        #messages { 
            list-style-type: none; margin: 0; padding: 0; 
        } 
        #messages > li { 
            padding: 0.5rem 1rem; 
        } 
        #messages > li:nth-child(odd) { 
            background: #efefef; 
        } 
        </style> 
    </head> 
    <body> 
        <ul id="messages"></ul> 
        <form id="form" action=""> 
            <input id="input" autocomplete="off" />
            <button>Send</button> 
        </form> 

        <script src="/socket.io/socket.io.js"></script> 

        <script> 
            var socket = io(); 
            var form = document.getElementById('form'); 
            var input = document.getElementById('input'); 
            //send 
            form.addEventListener('submit', function(e) { 
                e.preventDefault(); 
                if (input.value) { 
                    socket.emit('chat message', input.value); 
                    input.value = ''; 
                } 
            }); 
            // input 
            socket.on('chat message', function(msg) { 
                var item = document.createElement('li'); 
                item.textContent = msg; 
                messages.appendChild(item); 
                window.scrollTo(0, document.body.scrollHeight); 
            }); 
        </script> 
    </body> 
</html>
```

##### npm 세팅 및 실행

```bash
npm init

npm install express

npm install socket.io

node index.js
```

