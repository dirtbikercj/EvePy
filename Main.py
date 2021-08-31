import Auth, Flask_Server, Commands, time
from esipy import EsiSecurity, EsiApp, EsiClient
from esipy.cache import FileCache
from TokenCode import security_tokens, TokenCode

security = EsiSecurity(
    redirect_uri='http://localhost:15584/sso/callback',
    client_id='72f5bcdb0154445092b534fbadc1bcc0',
    secret_key='K7CRQggDJpbx9XPrMzLfVv7rLYbboZEoHbs7fpbJ',
    headers={'User-Agent': 'In-game name: Death Scout'}
)
security.update_token({
    'access_token': '',
    'expires_in': security_tokens.get_expires_in(),
    'refresh_token': security_tokens.get_refresh_token()
})

cache = FileCache(path="/tmp")
app = EsiApp(cache=cache).get_latest_swagger

client = EsiClient(
        retry_requests=True,
        headers={'User-Agent': 'In-game name: Death Scout'},
        security=security
    )
print('Client Setup')


if __name__ == "__main__":
    TokenCode.__init__(TokenCode, token='', refresh_token='', expires_in=0)
    Flask_Server.start_flask()
    time.sleep(0.2)  # Thread staggering
    Commands.RegisterCommands.command_loop_thread(Commands)
