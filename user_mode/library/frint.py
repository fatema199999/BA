from library.instruction import Instruction


class Frint(Instruction):
    def __init__(self):
        opcode = "frint"
        suffixes = ["a", "i", "m", "n", "p", "x", "z"]
        registerPrefixes = ["s", "d"]
        numberOfOperators = 2
        shift = [""]
        immediates = [""]                
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)