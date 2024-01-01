# Class to generate the list of instructions which you want to benchmark

from library.add import Add   
from library.sub import Sub    

from library.fabs import Fabs
from library.fadd import Fadd
from library.fcmp import Fcmp
from library.fccmp import Fccmp
from library.fcsel import Fcsel
from library.fcvt import Fcvt
from library.fcvta import Fcvta
from library.fcvtm import Fcvtm
from library.fcvtn import Fcvtn
from library.fcvtp import Fcvtp
from library.fcvtz import Fcvtz
from library.fdiv import Fdiv
from library.fmadd import Fmadd
from library.fmax import Fmax
from library.fmin import Fmin
from library.fmov import Fmov
from library.fmsub import Fmsub
from library.fmul import Fmul
from library.fneg import Fneg
from library.fnm import Fnm
from library.fnmul import Fnmul
from library.frint import Frint
from library.fsqrt import Fsqrt
from library.fsub import Fsub
from library.ldnp import Ldnp
from library.ldp import Ldp
from library.ldr import Ldr
from library.ldur import Ldur
from library.scvtf import Scvtf
from library.stnp import Stnp
from library.stp import Stp
from library.str import Str
from library.stur import Stur
from library.ucvtf import Ucvtf




class Generator():
    def __init__():
        blocks = []
    
    def generate():
        blocks = []
        #blocks.extend(Add().generate_instruction_block())
        #blocks.extend(Fabs().generate_instruction_block())
        #blocks.extend(Fadd().generate_instruction_block())
        #blocks.extend(Fcmp().generate_instruction_block())
        #blocks.extend(Fccmp().generate_instruction_block())      #unausführbar
        #blocks.extend(Fcsel().generate_instruction_block())      #unausführbar
        #blocks.extend(Fcvt().generate_instruction_block())       #unausführbar
        #blocks.extend(Fcvta().generate_instruction_block())
        #blocks.extend(Fcvtm().generate_instruction_block())
        #blocks.extend(Fcvtn().generate_instruction_block())
        #blocks.extend(Fcvtp().generate_instruction_block())
        #blocks.extend(Fcvtz().generate_instruction_block())
        #blocks.extend(Fdiv().generate_instruction_block())
        #blocks.extend(Fmadd().generate_instruction_block())
        #blocks.extend(Fmax().generate_instruction_block())
        #blocks.extend(Fmin().generate_instruction_block())
        #blocks.extend(Fmov().generate_instruction_block())
        #blocks.extend(Fmsub().generate_instruction_block())      #unausführbar
        #blocks.extend(Fmul().generate_instruction_block())
        #blocks.extend(Fneg().generate_instruction_block())
        #blocks.extend(Fnm().generate_instruction_block())        #unausführbar
        #blocks.extend(Fnmul().generate_instruction_block())    
        #blocks.extend(Frint().generate_instruction_block())       
        #blocks.extend(Fsqrt().generate_instruction_block())       
        #blocks.extend(Fsub().generate_instruction_block())   
        #blocks.extend(Ldnp().generate_instruction_block())       #unausführbar  
        #blocks.extend(Ldp().generate_instruction_block())        #unausführbar
        #blocks.extend(Ldr().generate_instruction_block())        #teilweise ausführbar(nur mit s)
        #blocks.extend(Ldur().generate_instruction_block())       #unausführbar
        #blocks.extend(Scvtf().generate_instruction_block())       
        #blocks.extend(Stnp().generate_instruction_block())       #unausführbar
        #blocks.extend(Stp().generate_instruction_block())        #unausführbar
        #blocks.extend(Str().generate_instruction_block())        #unausführbar
        #blocks.extend(Stur().generate_instruction_block()) 
        blocks.extend(Ucvtf().generate_instruction_block())       




        return blocks