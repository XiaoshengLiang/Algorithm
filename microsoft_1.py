import sys

    
def acceptable_partitions(num,list):
  n=0
  for i in range(1,num-1):
    for j in range(1,num-i):
      if (num-i-j):
        s1 = s2 = s3 = 0
        for m in range(i):
          s1 += list[m]
        for n in range(i,i+j):
          s2 += list[n]
        for q in range(i+j+1, num):
          s3 += list[q]
        if ((abs(s1-s2)<1)and (abs(s2-s3)<1) and(abs(s3-s1)<1)):
          n += 1
  print (n)


num=int(raw_input())
raw_list = raw_input().split()
list = []
for i in range(len(raw_list)):
  list.append(int(raw_list[i]))
  
acceptable_partitions(num, list)