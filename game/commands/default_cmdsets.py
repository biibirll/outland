from evennia.commands.default import unloggedin
from evennia import default_cmds
from commands.unloggedin_commands import (
    UnconnectedLoginCommand,
    UnconnectedCreateCommand,
)


class CharacterCmdSet(default_cmds.CharacterCmdSet):
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()


class AccountCmdSet(default_cmds.AccountCmdSet):
    key = "DefaultAccount"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        self.add(unloggedin.CmdUnconnectedLook)
        self.add(UnconnectedLoginCommand)
        self.add(UnconnectedCreateCommand)


class SessionCmdSet(default_cmds.SessionCmdSet):
    key = "DefaultSession"

    def at_cmdset_creation(self):
        super().at_cmdset_creation()
