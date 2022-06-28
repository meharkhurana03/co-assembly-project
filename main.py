import sys

#Global Constants
MAX_LINES = 256
REG_SIZE = 3
MEM_SIZE = 8
OPCODE_SIZE = 5
IMM_SIZE = 8

assembly_input = sys.stdin.read().split('\n')

lst = [i.split() for i in assembly_input]

code_length = len(lst)-1

i = 0
var_count = 0
while lst[i][0] == "var":
    var_count += 1
    i += 1

for inst in lst[var_count:length]:
    pass
    # convert(inst)



rdict = {"R0" : "000",  "R1" : "001", "R2" : "010", "R3" : "011", "R4" : "100", "R5" : "101", "R6" : "110", "FLAGS" : "110"}
#----EOF----


opCode = {
        "add":"10000",
        "sub":"10001",
        "movi":"10010",
        "movr":"10011",
        "ld":"10100",
        "st":"10101",
        "mul":"10110",
        "div":"10111",
        "rs":"11000",
        "ls":"11001",
        "xor":"11010",
        "or":"11011",
        "and":"11100",
        "not":"11101",
        "cmp":"11110",
        "jmp":"11111",
        "jlt":"01100",
        "jgt":"01101",
        "je":"01111",
        "hlt":"01010"
        }
