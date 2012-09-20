from rajax.cmd import parse
from rajax.const import opcode_to_cmd
from Instruction import Instruction
from Thompson import thompson

#: Takes a regex and returns a list of tuple opcodes
def str_to_opcodes(str):
	opcodes = parse(str)
	
	return opcodes

#: Takes opcodes and adds them to the program list
def build_instructions(opcodes):
	program = []
	
	for opcode in opcodes:
		if opcode[0] is Instruction.CHAR:
			program.append(Instruction.inst_char(chr(opcode[1])))
		elif opcode[0] is Instruction.MATCH:
			program.append(Instruction.inst_match())
		elif opcode[0] is Instruction.SPLIT:
			program.append(Instruction.inst_split(opcode[1], opcode[2]))
		elif opcode[0] is Instruction.JUMP:
			program.append(Instruction.inst_jump(opcode[1]))
			
	return program		
	
if __name__ == '__main__':
	list = build_instructions(str_to_opcodes('a*b'))
		
	for item in list:
		print item	
		
	print thompson(list, 'aaab')
	
