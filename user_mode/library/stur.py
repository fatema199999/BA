from library.instruction import Instruction


class Stur(Instruction):
    def __init__(self):
        opcode = "stur"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 2
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)