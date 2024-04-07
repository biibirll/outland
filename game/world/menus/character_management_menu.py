from typeclasses.characters import Character


def start(caller, raw_string, **kwargs):
    text = "Choose an existing character or create a new one."

    options = [
        *[
            {
                "desc": character.key,
                "goto": ("puppet_character", {"character": character}),
            }
            for character in caller.characters.all()
        ],
        {"desc": "New character", "goto": "get_character_name"},
    ]

    return text, options


def get_character_name(caller, raw_input, **kwargs):
    def create_character(caller, name, **kwargs):
        if not name:
            return "start"

        Character.create(name, account=caller)

        return "start"

    text = "New character's name: "

    options = {"key": "_default", "goto": create_character}

    return text, options


def puppet_character(caller, raw_string, **kwargs):
    character = kwargs["character"]
    session = caller.sessions.get()[0]

    caller.puppet_object(session, character)

    return None
