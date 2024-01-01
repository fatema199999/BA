from library.instruction import Instruction


class Fcvtp(Instruction):
    def __init__(self):
        opcode = "fcvtp"
        suffixes = ["s", "u"]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 2
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)