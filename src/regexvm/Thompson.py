import Queue
from Instruction import Instruction

def thompson(program, string):
	cqueue = Queue.Queue()
	nqueue = Queue.Queue()
	cqueue.put(0)
	
	tc = 0

	while tc <= len(string):
		while not cqueue.empty():
			pc = cqueue.get()
			inst = program[pc]

			if inst.opcode is Instruction.CHAR:
				if tc < len(string) and string[tc] == inst.value:
					nqueue.put(pc+1)
			
			elif inst.opcode is Instruction.MATCH:
				if tc == len(string):
					return True
			
			elif inst.opcode is Instruction.JUMP:	
				cqueue.put(inst.arg1)
				
			elif inst.opcode is Instruction.SPLIT:
				cqueue.put(inst.arg1)
				cqueue.put(inst.arg2)	

		tc = tc + 1
			
		cqueue, nqueue = nqueue, cqueue
		
	return False	
