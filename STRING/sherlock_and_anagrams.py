#!/usr/local/bin/ python3
# solution for https://www.hackerrank.com/challenges/sherlock-and-anagrams


def sherlockAndAnagrams(s):
    # Complete this function
    n = len(s)
    if n == len(set(s)):
        return 0
 
    def find_substr(s):
        if len(s) == 1:
            return [s]
        return  [s[0]] + [s[0] + suffix for suffix in find_substr(s[1:])]

    ans = []
    for i in range(len(s)):
        ans += find_substr(s[i:])

    anagram = [sorted(x) for x in ans] #compare two anagrams..
    picked = 0
    for i in range(len(ans)):
        for ana in  anagram[i+1:]:
            if ana == anagram[i]:
                picked += 1
    return picked 

def main():
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = sherlockAndAnagrams(s)
        print(result)

if __name__ == '__main__':
    main()
