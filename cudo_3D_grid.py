x = int ( raw_input())
y = int ( raw_input())
z = int ( raw_input())
n = int ( raw_input())
print[[ i , j, x] for i in range ( x + 1 ) for j in range( y + 1) for x in range( z + 1) if ((i+j+x) != n)]
