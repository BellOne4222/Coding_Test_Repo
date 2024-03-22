import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  
  cases = [] # ['113', '12340', '12345', '98346', '123440']
  for i in range(n):
    cases.append(sys.stdin.readline().rstrip())
  
  cases.sort()
  
  flag = "YES"
  
  for j in range(n-1):
    if cases[j] == cases[j+1][:len(cases[j])]:
      flag = "NO"
      break
  
  print(flag)