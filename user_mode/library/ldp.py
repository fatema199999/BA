from library.instruction import Instruction


class Ldp(Instruction):
    def __init__(self):
        opcode = "ldp"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 1
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)