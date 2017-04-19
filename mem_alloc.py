def first_fit(p, pc):
	for n,i in enumerate(pc):
		for e,j in enumerate(p):
			if i<j:
				print("Partition size for process {}: {}".format(n+1,j))
				p.pop(e)
				break

def best_fit(p, pc):
	for n,i in enumerate(pc):
		t = [tp for tp in p if tp>=i]
		t = min(t)
		print("Partition size for process {}: {}".format(n+1,t))
		p.pop(p.index(t))

def worst_fit(p, pc):
	for n,i in enumerate(pc):
                t = [tp for tp in p if tp>=i]
                t = max(t)
                print("Partition size for process {}: {}".format(n+1,t))
                p.pop(p.index(t))




def cont():
	print("Do you want to continue: (y or n):", end="")
	c = input()
	if c=='n' or c=="N":
		exit()
	elif c=="y" or c=="Y":
		pass
	else:
		print("Please Enter y or n:", end="")
		cont()

def choose(i,p,pc):
	if i==1:
		first_fit(p,pc)
	elif i==2:
		best_fit(p,pc)
	elif i==3:
		worst_fit(p,pc)
	else :
		print("Enter 1,2 or 3")

def main():
	partition_size = []
	process_size = []
	print("No. of memory partition:", end="")
	n_partition = int(input())
	print("--"*5)
	print ("Enter size for each partition:")
	for i in range(n_partition):
		print("Size for partition "+str(i+1)+":", end="")
		partition_size.append(int(input()))
	print("--"*5)
	print ("Enter size for each process:")
	for i in range(n_partition):
		print("Size for Process "+str(i+1)+":", end="")
		process_size.append(int(input()))
	print("--"*5)
	print("""Select algo for partition:
	1. First Fit
	2. Best Fit
	3. Worst Fit""")
	algo = int(input())
	print("--"*5)
	choose(algo, partition_size, process_size)
	print("--"*5)
	cont()
	print("--"*5)

if __name__=="__main__":
	while(True):
		try:
			main()
		except Exception as e:
			print("Error: {}".format(e))
