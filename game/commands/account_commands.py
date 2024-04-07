from evennia.commands.default.account import CmdOOCLook
from evennia.utils.evmenu import EvMenu


class CharacterManagementMenu(EvMenu):
    def nodetext_formatter(self, nodetext):
        return nodetext

    def node_formatter(self, nodetext, optionstext):
        return f"{nodetext}\n{optionstext}\n"


class AccountLookCommand(CmdOOCLook):
    def func(self):
        CharacterManagementMenu(
            self.caller,
            "world.menus.character_management_menu",
            "start",
            auto_help=False,
            auto_quit=False,
            cmd_on_exit=None,
        )
