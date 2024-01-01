from library.instruction import Instruction


class Str(Instruction):
    def __init__(self):
        opcode = "str"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 3
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)