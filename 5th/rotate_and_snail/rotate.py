# -*- coding: utf-8 -*-
init_array = []

for i in range(5):
	empty_array = []
	for j in range(5):
		empty_array.append(i*5 + j +1)
	init_array.append(empty_array)

for column in init_array:
	for num in column:
		print "%2s" % num,
	print
# print init array
#  1  2  3  4  5
#  6  7  8  9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

#(0,0) = (4,0)
#(0,1) = (3,0)
#(0,2) = (2,0)
#(3,2) = (2,3)
#(i,j) = (4-j,i)
#(0,4)=(4,4)
#(i,j)=(j,4-i)

# change array like this
# 21 16 11  6 1
# 22 17 12  7 2
# 23 18 13  8 3
# 24 19 14  9 4
# 25 20 15 10 5 
rotate_array = []

for i in range(5):
	empty_array = []
	for j in range(5):
		empty_array.append(0)
	rotate_array.append(empty_array)

######## insert your algorithm here ########
for i in range(5):
	for j in range(5):
		rotate_array[i][j]=init_array[4-j][i]



print
for column in rotate_array:
	for num in column:
		print "%2s" % num,
	print
# print result array
# 영어 주석 힘들다.