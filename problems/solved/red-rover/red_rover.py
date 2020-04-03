#!/bin/python3

seq = input()
seq_length = len(seq)

for i in range(len(seq) - 1):
    for j in range(i + 1, len(seq)):
        macro = seq[i:j]
        modified_s = seq.replace(macro, 'm')
        modified_len = len(modified_s) + len(macro)
        seq_length = min(modified_len, seq_length)

print(seq_length)
