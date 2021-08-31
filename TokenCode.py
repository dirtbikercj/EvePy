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
