## pip install websocket-client ##
import websocket
#Connect to websocket server
ws = websocket.WebSocket()
ws.connect("ws://websocket server ip")
print("Connected to WebSocket Server")
#Ask the user for some input
inputStr = input("Say something: ")
ws.send(inputStr)
#Wait for server to respond
result = ws.recv()
print("Received: " + result)
#Socket close
ws.close()