'''

All web routes for the website

'''
import Auth
from flask import request, Blueprint

logon = Blueprint('logon', __name__)
shutdown = Blueprint('shutdown', __name__)


@logon.route('/sso/callback')
def login_callback():
    print('args:', request.args)  # Display text in console
    Auth.security_tokens.set_token(request.args.get('code', 'none'))
    return 'Login Successful, you may now close this window and return to the app.'


@shutdown.route('/shutdown', methods=['GET'])
def shutdown_callback():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    shutdown_func()
    return 'Shutting down...'
