import threading, market_module, Auth, Flask_Server


class RegisterCommands:
    command_thread = threading.Thread(target=lambda: RegisterCommands.command_loop(RegisterCommands))
    commands = {
        "help": ": Enter a module name in order to enter it.",
        "clear_swagger_cache": ": Clears the ESI cache(Dev-Command)",
        "price_checker": ": Downloads prices based on region and item entered.",
        "refresh_token": ": Force refresh authentication token(Dev-Command)",
        "print_active_character": ": Lists the active character",
        "login": ": Log in via ESI",
        "logout": ": logs you out of the program",
        "exit": ": Exits the program"
    }

    class Colors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def help(self):
        print(f"{self.Colors.FAIL}Development Version{self.Colors.ENDC}")
        for key, value in self.commands.items():
            print(key, value)
        self.command_loop(self)

    def clear_swagger_cache(self):  # TODO
        print(f"{self.Colors.WARNING}Clearing Swagger cache...{self.Colors.ENDC}")

        self.command_loop(self)

    def price_checker(self):
        print(f"{self.Colors.OKGREEN}Price Checker Module{self.Colors.ENDC}")
        item = input('Enter item to search: ')
        region = input('Enter Region to search: ')
        market_module.return_item_data(item, region)
        self.command_loop(self)

    def refresh_token(self):
        print(f"{self.Colors.WARNING}Refreshing Token...{self.Colors.ENDC}")
        Auth.refresh_token()
        self.command_loop(self)

    def print_active_character(self):  # TODO
        print(f"{self.Colors.WARNING}Not Yet Implemented{self.Colors.ENDC}")
        self.command_loop(self)

    def login(self):
        if Auth.security_tokens.get_token() == '':
            print(f"{self.Colors.OKGREEN}Click the link to go to the eve online ESI login page{self.Colors.ENDC}")
            Auth.get_logon_url()
            Auth.authenticate()
        else:
            print(f"{self.Colors.WARNING}You are already logged in, "
                  f"please log out to log in with a different character.{self.Colors.ENDC}")
        self.command_loop(self)

    def logout(self):
        if Auth.security_tokens.get_token() != '':
            print(f"{self.Colors.WARNING}Logging out...{self.Colors.ENDC}")
            Auth.security_tokens.set_token('')
            Auth.security_tokens.set_refresh_token('')
            Auth.security_tokens.set_expires_in(-1)
        else:
            print(f"{self.Colors.WARNING}You are not logged in.{self.Colors.ENDC}")
        self.command_loop(self)

    def exit(self):
        print(f"{self.Colors.FAIL}Exiting...{self.Colors.ENDC}")
        Flask_Server.shutdown_server()
        exit()
        self.command_loop(self)

    def command_loop(self):
        command = input('\nEnter a module to enter. Type help for help: ')
        if command in RegisterCommands.commands:
            result = getattr(RegisterCommands, command)(self)
        else:
            print('\nCommand does not exist. Type help for help or enter a valid command \n')
        self.command_loop(self)

    def command_loop_thread(self):
        RegisterCommands.command_thread.start()
