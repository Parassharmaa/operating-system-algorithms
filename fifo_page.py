def revrs(l):
	return l[::-1]

n_part = int(input("Enter no. of partitions:"))
pages = list(map(int, input("Enter pages string:").split()))

frame = []

page_fault = 0

frame = revrs(list(set(pages)))[-n_part:]
pages = revrs(revrs(pages)[:-n_part])


print("--"*5)
print("Initial frame->", end="")
print(frame)
print("--"*5)
for i,p in enumerate(pages):
	if p not in frame:
		page_fault+=1
		frame.pop()
		frame = revrs(frame)
		frame.append(p)
		frame = revrs(frame)
		print("Frame after PageFault "+str(page_fault)+"->", frame)
		print("--"*5)


print("Total No. of page-faults: {}".format(page_fault))
