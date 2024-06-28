from library.instruction import Instruction


class Fmsub(Instruction):
    def __init__(self):
        opcode = "fmsub"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 4     
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)