from library.instruction import Instruction


class Fmin(Instruction):
    def __init__(self):
        opcode = "fmin"
        suffixes = ["","nm"]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 3
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)