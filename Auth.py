from Main import security
from TokenCode import security_tokens
import time, threading


def get_logon_url():
    print(security.get_auth_uri(state='8273098709287', scopes=[
        'esi-wallet.read_character_wallet.v1']))


def authenticate():
    try:
        token_code = security_tokens.get_token()
        while token_code == '':
            print('Checking for Token....')
            token_code = security_tokens.get_token()
            if token_code != '':
                print('Token Recieved')
                set_initial_token(security_tokens.get_token())
                refresh_token_thread_start()
            time.sleep(2)
    except KeyboardInterrupt:
        print('\nProcess terminated by user')


def set_initial_token(token):
    tokens = security.auth(token)
    security_tokens.set_refresh_token(tokens['refresh_token'])
    security_tokens.set_expires_in(tokens['expires_in'])
    print('Refresh token is: \n', security_tokens.get_refresh_token())
    print('Expires in: \n', security_tokens.get_expires_in())


def refresh_token_thread():
    while security_tokens.get_expires_in() >= 0:
        # print('Token Refresh In: ', security_tokens.get_expires_in(), ' seconds')
        if security_tokens.get_expires_in() == 0:
            print('Token Refresh..')
            tokens = security.refresh()
            security_tokens.set_refresh_token(tokens['refresh_token'])
            security_tokens.set_expires_in(tokens['expires_in'])
            print('Refresh token is: \n', security_tokens.get_refresh_token())
            print('Expires in: \n', security_tokens.get_expires_in())
            time.sleep(1)
            refresh_token_thread()
        else:
            security_tokens.set_expires_in(security_tokens.get_expires_in() - 1)
            time.sleep(1)


def refresh_token():
    tokens = security.refresh()
    security_tokens.set_refresh_token(tokens['refresh_token'])
    security_tokens.set_expires_in(tokens['expires_in'])
    print('Refresh token is: \n', security_tokens.get_refresh_token())
    print('Expires in: \n', security_tokens.get_expires_in())


def refresh_token_thread_start():
    r_token_thread = threading.Thread(target=lambda: refresh_token_thread())
    r_token_thread.start()
