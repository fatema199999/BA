from library.instruction import Instruction


class Fadd(Instruction):
    def __init__(self):
        opcode = "fadd"
        suffixes = [""]
        registerPrefixes = ["d"]
        numberOfOperators = 3
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)