from library.instruction import Instruction


class Fmov(Instruction):
    def __init__(self):
        opcode = "fmov"
        suffixes = [""]
        registerPrefixes = ["d"]
        numberOfOperators = 2               # mit 1 ist auch ausführbar
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)