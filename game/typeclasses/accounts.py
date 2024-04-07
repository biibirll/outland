from evennia.accounts.accounts import DefaultAccount, DefaultGuest


class Account(DefaultAccount):
    ooc_appearance_template = "Login successful. Welcome!"

    def at_post_login(self, session=None, **kwargs):
        self.execute_cmd("look")


class Guest(DefaultGuest):
    pass
