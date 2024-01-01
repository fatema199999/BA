import random
from library.instruction import Instruction


class Fabs(Instruction):
    def __init__(self):
        opcode = "fabs"
        suffixes = [""]
        registerPrefixes = ["d", "s"]           #h"16 Bits" wird nicht unterstüzt
        numberOfOperators = 2
        shift = [""]
        immediates = [""]
        bothAllowed = False
        super().__init__(opcode, suffixes, registerPrefixes, numberOfOperators, shift, immediates, bothAllowed)
		