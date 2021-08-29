content = input('content:')
n = 1

for i in content:
    print(content[0:n])
    n = n+1

n = len(content) - 1
for i in content:
    print(content[0:n])
    n = n-1
