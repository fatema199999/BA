from library.instruction import Instruction

class Fcmp(Instruction):
    def __init__(self):
         opcode = "fcmp"
         suffixes = ["", "e"]
         registerPrefixes = ["s", "d"]
         numberOfOperators = 2
         shift = [""]
         immediates = [""]
         bothAllowed = False
         super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed) 