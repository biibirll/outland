import evennia
from typeclasses.accounts import Account
from commands.command import Command
from typeclasses.accounts import Account
from evennia.utils.evmenu import EvMenu


# class LoginMenu(EvMenu):


class UnconnectedLoginCommand(Command):
    key = "login"

    def func(self):
        session: Session = self.caller

        username = yield "Username (leave blank to abort): "

        if not username:
            session.msg("Aborting...")
            return

        if not (
            len(
                evennia.search_account(
                    username,
                )
            )
        ):
            session.msg("Account does not exist.")
            return

        password = yield "Password (leave blank to abort): "

        if not password:
            session.msg("Aborting...")
            return

        account, errors = Account.authenticate(username, password, ip=session.address)

        if errors:
            session.msg("Invalid password.")
            return

        session.sessionhandler.login(session, account)


class UnconnectedCreateCommand(Command):
    key = "create"

    def func(self):
        session = self.caller

        username = yield "New account username (leave blank to abort): "

        if not username:
            session.msg("Aborting...")
            return

        if len(evennia.search_account(username)):
            session.msg("Username already taken. Pick another.")
            return

        password = (
            yield """Create a new password. Your password must:
        
        1. Be at least 8 characters long.
        2. Contain numbers and letters.
        3. Not be a common pattern (e.g. "12345678").
        4. Not include your username.
        
        Password (leave blank to abort): """
        )

        if not password:
            session.msg("Aborting...")
            return

        account, errors = Account.create(
            username=username,
            password=password,
            ip=session.address,
            permissions="Player",
        )

        if errors:
            self.msg(errors)

        session.msg(
            "Account created successfully. You can now login with your username + password."
        )
