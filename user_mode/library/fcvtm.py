from library.instruction import Instruction


class Fcvtm(Instruction):
    def __init__(self):
        opcode = "fcvtm"
        suffixes = ["s", "u"]
        registerPrefixes = ["s"]
        numberOfOperators = 2
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)