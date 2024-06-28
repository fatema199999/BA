from library.instruction import Instruction


class Fneg(Instruction):
    def __init__(self):
        opcode = "fneg"
        suffixes = [""]
        registerPrefixes = ["d"]
        numberOfOperators = 2        
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)