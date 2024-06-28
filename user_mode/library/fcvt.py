from library.instruction import Instruction


class Fcvt(Instruction):
    def __init__(self):
        opcode = "fcvt"
        suffixes = [""]
        registerPrefixes = ["d", "s"]
        numberOfOperators = 2
        shift = [""]
        immediates = []
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)