from library.instruction import Instruction


class Fcvta(Instruction):
    def __init__(self):
        opcode = "fcvta"
        suffixes = []
        registerPrefixes = ["d"]
        numberOfOperators = 2
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)