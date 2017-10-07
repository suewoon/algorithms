#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/candies

def distribute(candies):
    distributed_candies= [1]
    def bi_distribute(i):
        if i==len(distributed_candies)-1:
            return
        if distributed_candies [i]:
            if candies[i]<candies[i+1]:
                distributed_candies.append(distributed_candies[i]+1)
            else:
                distributed_candies.append(1)
        return bi_distribute(i+1)
    bi_distribute(0,1)
    return distributed_candies

if __name__ == '__main__':
    n = int(input())
    candies = []
    for i in range(n):
        candies.append(int(input()))
    print(distribute(candies))
    
