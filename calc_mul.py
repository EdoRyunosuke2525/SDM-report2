#!/usr/bin/python3

import re
                
def calc(A, B):
    if not isinstance(A, int) or not isinstance(B, int) or isinstance(A, bool) or isinstance(B, bool):
        return -1
    
    if 1 <= A <= 999 and 1 <= B <= 999:
        return A * B
    return -1
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
