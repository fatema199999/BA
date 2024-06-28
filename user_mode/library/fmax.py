from library.instruction import Instruction


class Fmax(Instruction):
    def __init__(self):
        opcode = "fmax"
        suffixes = ["","nm"]
        registerPrefixes = ["d"]
        numberOfOperators = 3
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)