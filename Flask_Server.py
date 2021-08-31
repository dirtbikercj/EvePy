'''

Flask server

'''


from flask import Flask, request
from Routes import logon, shutdown
import threading

host_name = "localhost"
port = 15584

flask_app = Flask(__name__)

'''
Registered Routes
'''
flask_app.register_blueprint(logon)
flask_app.register_blueprint(shutdown)


def start_flask():
    threading.Thread(target=lambda: flask_app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()


def shutdown_server():
    import requests
    response = requests.get('http://localhost:15584/shutdown')
