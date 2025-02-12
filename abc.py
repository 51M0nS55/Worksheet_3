import os

def binary_multiply_turing(bin1: str, bin2: str, filename: str):
    bin1 = list(bin1)
    bin2 = list(bin2)
    positions = [i for i, bit in enumerate(reversed(bin2)) if bit == '1']
    result = 0
    multiplicand = int(''.join(bin1), 2)
    tape_states = []
    
    # Initialization
    tape = ["B", "B", "B"] + bin1 + ["#"] + bin2 + ["B", "B", "B"]
    tape_states.append(f"q0: {' '.join(tape)}")
    
    # Marking
    for i in range(len(bin2)):
        if bin2[i] == '1':
            tape[3 + len(bin1) + 1 + i] = 'X'
    tape_states.append(f"q1: {' '.join(tape)}")
    
    # Multiplication
    for idx, pos in enumerate(positions):
        shift_result = multiplicand << pos
        result += shift_result
        tape_result = list(bin(shift_result)[2:])
        tape_extended = ["B", "B", "B"] + bin1 + ["#"] + ["X" if b == '1' else b for b in bin2] + ["$"] + tape_result + ["B", "B"]
        tape_states.append(f"q{idx + 2}: {' '.join(tape_extended)}")
    
    final_result = list(bin(result)[2:])
    tape_final = ["B", "B", "B"] + final_result + ["B", "B", "B"]
    tape_states.append(f"q_halt: {' '.join(tape_final)}")
    
    with open(filename, 'w') as f:
        for state in tape_states:
            f.write(state + "\n")


bin1 = "101" 
bin2 = "110"
filename = f"multiplication_{bin1}_x_{bin2}.dat"

binary_multiply_turing(bin1, bin2, filename)
print(f"Multiplication steps saved in {filename}")