from library.instruction import Instruction

class Ldur(Instruction):
    def __init__(self):
        opcode = "ldur"
        suffixes = [""]
        registerPrefixes = ["q", "d"]  
        numberOfOperators = 2 
        shift = [""] 
        immediates = ["#-16"] 
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)
