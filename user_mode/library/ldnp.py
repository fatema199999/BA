from library.instruction import Instruction


class Ldnp(Instruction):
    def __init__(self):
        opcode = "ldnp"
        suffixes = [""]
        registerPrefixes = ["s", "d", "q"]
        numberOfOperators = 3    
        shift = [""]
        immediates = ["2"]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)