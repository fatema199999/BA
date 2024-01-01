from library.instruction import Instruction


class Fnmul(Instruction):
    def __init__(self):
        opcode = "fnmul"
        suffixes = [""]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 3
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)