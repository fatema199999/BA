from library.instruction import Instruction


class Fmadd(Instruction):
    def __init__(self):
        opcode = "fmadd"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 4
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)