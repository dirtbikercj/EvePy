from flask import Flask, request
import threading, Auth




host_name = "localhost"
port = 15584
flask_app = Flask(__name__)


def start_flask():
    threading.Thread(target=lambda: flask_app.run(host=host_name, port=port, debug=True, use_reloader=False)).start()


@flask_app.route('/oauth-callback/')
def login_callback():
    print('args:', request.args)  # Display text in console
    Auth.security_tokens.set_token(request.args.get('code', 'none'))
    return request.args.get('code', 'none')
