from esipy import EsiApp, EsiClient, EsiSecurity
from esipy.cache import FileCache
import time, threading


#  Global variables
class TokenCode:
    def __init__(self, token='', refresh_token='', expires_in=0):
        self._token = token
        self._refresh_token = refresh_token
        self._expires_in = expires_in

    def get_token(self):
        return self._token

    def set_token(self, x):
        self._token = x

    def get_refresh_token(self):
        return self._refresh_token

    def set_refresh_token(self, x):
        self._refresh_token = x

    def get_expires_in(self):
        return self._expires_in

    def set_expires_in(self, x):
        self._expires_in = x


security_tokens = TokenCode()

cache = FileCache(path="/tmp")

security = EsiSecurity(
    redirect_uri='http://localhost:15584/oauth-callback',
    client_id='72f5bcdb0154445092b534fbadc1bcc0',
    secret_key='K7CRQggDJpbx9XPrMzLfVv7rLYbboZEoHbs7fpbJ',
    headers={'User-Agent': 'In-game name: Death Scout'}
)

security.update_token({
    'access_token': '',
    'expires_in': security_tokens.get_expires_in(),
    'refresh_token': security_tokens.get_refresh_token()
})


def start_esi():
    app = EsiApp(cache=cache).get_latest_swagger
    client = EsiClient(
        retry_requests=True,
        headers={'User-Agent': 'In-game name: Death Scout'},
        security=security
    )
    print('ESI Client Setup.')


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
            time.sleep(5)
    except KeyboardInterrupt:
        print('\nProcess terminated by user')


def set_initial_token(token):
    tokens = security.auth(token)
    security_tokens.set_refresh_token(tokens['refresh_token'])
    security_tokens.set_expires_in(tokens['expires_in'])
    print('Refresh token is: \n', security_tokens.get_refresh_token())
    print('Expires in: \n', security_tokens.get_expires_in())


def refresh_token():
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


def refresh_token_thread():
    r_token_thread = threading.Thread(target=refresh_token())
    r_token_thread.start()
