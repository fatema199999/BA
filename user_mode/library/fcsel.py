from library.instruction import Instruction

class Fcsel(Instruction):
    def __init__(self):
         opcode = "fcsel"
         suffixes = [""]
         registerPrefixes = ["d", "s"]
         numberOfOperators = 3
         shift = [""]
         immediates = [""]
         bothAllowed = False
         super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed) 