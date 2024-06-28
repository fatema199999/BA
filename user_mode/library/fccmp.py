from library.instruction import Instruction

class Fccmp(Instruction):
    def __init__(self):
         opcode = "fccmp"
         suffixes = [""] #"e"]
         registerPrefixes = ["s", "d"]
         numberOfOperators = 2
         shift = [""]
         immediates = ["1"]
         bothAllowed = False
         super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)