from library.instruction import Instruction


class Fnm(Instruction):
    def __init__(self):
        opcode = "fnm"
        suffixes = ["add", "sub"]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 4   
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)