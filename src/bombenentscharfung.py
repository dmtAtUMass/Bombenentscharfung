import string
import collections
from pwn import *

MAX_LENGTH = 5
MAX_INT = 10000
NUM_PHASE = 5

correct = []
length = []
keys = list(string.ascii_lowercase)
keys.extend(list(string.ascii_uppercase))
keys.extend([str(i) for i in range(1, MAX_INT)])

def infuseNTimes(arr, n):
    res = collections.deque(arr)
    for _ in range(1,n):
        for i in range(len(res)):
            temp = res.popleft()
            res.extend([temp + " " + ay for ay in arr])
    return res

def phaseLength(phase):
    for i in range(1, MAX_LENGTH + 1):
        p = process('./binary_bomb')
        for j in range(len(correct)):
            ans = correct[j]
            p.sendline(ans.encode())
        query = "a"*i
        # print(query)
        p.sendline(query.strip().encode())
        out = p.recv()
        # print(query, out.decode().strip().split('\n'))
        if (out.decode().strip().count("phase") == phase):
            p.close()
            return i
        p.close()
def defuse(number_of_phases):
    while len(correct) < number_of_phases:
        # Writing all the answers to the previous questions
        length.append(phaseLength(len(correct) + 1))
        length_input = length[len(correct)]
        print(length)
        possible_answer = infuseNTimes(keys, length_input)
        p = process('./binary_bomb')
        for i in range(len(correct)):
            ans = correct[i]
            p.sendline(ans.encode())
        for _ in range(len(possible_answer)):
            p = process('./binary_bomb')
            # Writing all the answers to the previous questions
            for i in range(len(correct)):
                ans = correct[i]
                p.sendline(ans.encode())
            ans = possible_answer.popleft()
            p.sendline(ans.encode())
            out = p.recv()
            print(ans, out.decode().strip().split("\n"))
            # if len(out.decode().strip().split('\n')) > len(correct) + 2:
            if (out.decode().strip().count("BOOM!") == 0):
                correct.append(ans)
                print(f"Solution to {len(correct)} found!")
                break
            else:
                p.close()
        print(correct)

if __name__ == "__main__":
    defuse(NUM_PHASE)   