init = int(input("Enter initial position of head:"))
queue = list(map(int, input("Enter requests queue data:").split()))

seek_time = 0

for i in queue:
	seek_time+=abs(init-i)
	init = i


print("Total Seek Time: {}".format(seek_time))
