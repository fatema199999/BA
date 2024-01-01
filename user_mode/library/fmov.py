from library.instruction import Instruction


class Fmov(Instruction):
    def __init__(self):
        opcode = "fmov"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 2               # mit 1 ist auch ausführbar
        shift = [""]
        immediates = ["", "#1"]                # mit #5 ist auch ausführbar
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)