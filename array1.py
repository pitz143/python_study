import array as arr

num_arr = arr.array('i')
i=0
val=0
while i<6:
    i+=1
    print "enter your number:"
    val=int(input())
    num_arr.append(val)
num_arr.reverse()
for val in num_arr:
    print "%d " % val
