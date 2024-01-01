from library.instruction import Instruction


class Ldr(Instruction):
    def __init__(self):
        opcode = "ldr"
        suffixes = [""]
        registerPrefixes = ["s"]
        numberOfOperators = 1
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)