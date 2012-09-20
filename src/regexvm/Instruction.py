#: VM Instruction
class Instruction(object):
	MATCH, CHAR, SPLIT, JUMP = range(4)
	
	def __init__(self, opcode, value=None, arg1=None, arg2=None):
		self.opcode = opcode
		self.value = value
		self.arg1 = arg1
		self.arg2 = arg2
		
	def __repr__(self):
		if self.opcode is self.MATCH:
			return '<MATCH>'
		elif self.opcode is self.CHAR:
			return '<CHAR = %s>' % self.value
		elif self.opcode is self.SPLIT:
			return '<SPLIT = %d %d>' % (self.arg1, self.arg2)
		elif self.opcode is self.JUMP:
			return '<JUMP = %d>' % self.arg1
	
	@classmethod	
	def inst_char(cls, value):
		return cls(cls.CHAR, value=value)
	
	@classmethod	
	def inst_split(cls, line1, line2):
		return cls(cls.SPLIT, arg1=line1, arg2=line2)	
		
	@classmethod	
	def inst_jump(cls, line1):
		return cls(cls.JUMP, arg1=line1)	
		
	@classmethod
	def inst_match(cls):
		return cls(cls.MATCH)
		
