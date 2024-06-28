from library.instruction import Instruction

class Stp(Instruction):
    def __init__(self):
        opcode = "stp"
        suffixes = [""]
        registerPrefixes = ["d"]  # For different SIMD and FP registers
        numberOfOperators = 3  # Three operands: two registers and the memory address
        shift = [""]  # No shift needed for this instruction
        immediates = ["#5"]  # Example offsets
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)
