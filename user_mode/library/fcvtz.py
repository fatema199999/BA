from library.instruction import Instruction


class Fcvtz(Instruction):
    def __init__(self):
        opcode = "fcvtz"
        suffixes = ["s", "u"]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 2
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)