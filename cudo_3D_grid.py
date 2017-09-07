x = int ( raw_input())
y = int ( raw_input())
n = int ( raw_input())
print [ [i,j] for i in range(x+1) for j in range(y+1) if i+j != n ]
