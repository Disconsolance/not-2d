# Exception raised when a not2d script has been improperly configured
class NOT2DScriptMisconfig(Exception):

    def __init__(self, errcode, str="") -> None:
        msg=""
        match errcode:
            case 0:
                msg = f"Incorrect number of parameters"
            case 1:
                msg = "Draw frames are out of order"
            case 2:
                msg = "Incorrect type"
            case 3:
                msg = "Cannot be DEFAULT"
            case 4:
                msg = "Cannot be RANDOM"
            case 5:
                msg = "Wrong Order Index"
        super().__init__(f"Improperly configured not2d script!\n{msg}\n{str}")