from library.instruction import Instruction


class Ldnp(Instruction):
    def __init__(self):
        opcode = "ldnp"
        suffixes = [""]
        registerPrefixes = ["s"]
        numberOfOperators = 3    
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)