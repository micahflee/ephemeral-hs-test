import sys, threading, time
from stem.control import Controller
from stem import SocketError, UnsatisfiableRequest
from flask import Flask

import socks

WEB_PORT = 8080
TOR_CONTROL_PORT = 9151
TOR_SOCKS5_PORT = 9150

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

def start_web_app():
    print 'Starting web app'
    app.run(port=WEB_PORT, threaded=True)

def main():
    # Start the flask web app in a separate thread
    t = threading.Thread(target=start_web_app)
    t.daemon = True
    t.start()

    # Connect to the Tor control port
    try:
        c = Controller.from_port(port=TOR_CONTROL_PORT)
        c.authenticate()
    except SocketError:
        print 'Cannot connect to Tor control port'
        sys.exit()

    # Create an ephemeral hidden service
    try:
        res = c.create_ephemeral_hidden_service(WEB_PORT)
        onion = res.content()[0][2].split('=')[1] + '.onion'
        print onion
    except UnsatisfiableRequest:
        print 'Cannot create ephemeral hidden service, Tor version is too old'
        sys.exit()

    # Try connecting to the hidden service until it's ready
    ready = False
    while not ready:
        try:
            print 'Attempting to connect to {0:s}'.format(onion)
            s = socks.socksocket()
            s.setproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', TOR_SOCKS5_PORT)
            s.connect((onion, 80))
            s.close()
        except socks.ProxyConnectionError:
            print 'Cannot connect to Tor socks5 port'
            sys.exit()
        except socks.SOCKS5Error:
            print 'Not ready yet, waiting...'
            time.sleep(1)

if __name__ == '__main__':
    main()
