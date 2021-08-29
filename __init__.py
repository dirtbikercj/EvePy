import Flask_Server, Auth, time, logging, threading
from esipy import EsiApp, EsiClient, EsiSecurity





if __name__ == "__main__":
    Flask_Server.start_flask()
    Auth.start_esi()
    Auth.get_logon_url()
    Auth.authenticate()
    Auth.refresh_token_thread()

# print(json.dumps(tokens, indent=4, sort_keys=True))
