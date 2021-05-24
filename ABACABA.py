"The easy way based on iterating over a growing sequence"
import math

sequence = ""
firstNumber = 97
for i in range(0, 26):
    sequence += chr(firstNumber + i) + sequence
print(sequence)
print(len(sequence))


"Im also going to do this the hard way based on math"
"This one takes a long time but it will work"
totalLen = len(sequence)

sequence2 = ''
n = 26

for j in range(2 ** 10 - 1):
    if j % 2 == 0:
        sequence2 += 'a'
        print("here")
    else:
        k = 2 ** 26
        while k > 1:
            if (j + 1) % k == 0:
                sequence2 += chr(firstNumber + int(math.log(k,2)))
                print("there")
                break
            k = int(k / 2)

print(sequence2)
print(len(sequence2))





