import sys
import os
def palindrome(s):
	return s[::-1] == s
def solution(s):
    return palindrome(s)
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))
    print(solution(sys.argv[1]))