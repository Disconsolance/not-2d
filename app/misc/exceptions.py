# Exception raised when a not2d script has been improperly configured
class NOT2DScriptMisconfig(Exception):

    def __init__(self, string) -> None:
        msg = f"Improperly configured not2d script!\n{string}"
        super().__init__(msg)