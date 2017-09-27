#!/usr/env/bin python3
# solution for https://www.hackerrank.com/challenges/sam-and-substrings

def make_substr2(string):
    cache = {}
    def make_substr(string):
        #print(cache)
        if len(string) < 1:
            return 0

        if string not in cache:
            n = len(string)
            cache[string] = int(string) + make_substr(string[0:n-1]) + make_substr(string[1:n])
            return cache[string]

        else: # no redundancy.. 
            return 0
    return make_substr(string)

def main():
    string = input()
    print(make_substr2(string))

if __name__ == '__main__':
    main()
