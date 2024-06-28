from library.instruction import Instruction

#LDR (literal, SIMD and FP)
class Ldr(Instruction):
    def __init__(self):
        opcode = "ldr"
        suffixes = [""]
        registerPrefixes = ["q", "d"]
        numberOfOperators = 2
        shift = [""]
        immediates = ["#0x20"]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)
