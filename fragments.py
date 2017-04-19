def main():
	print("Enter no. of partitions:", end="")
	n_partition = int(input())
	partition_size = []
	print ("Enter size for each partition:")
	for i in range(n_partition):
		print("Size for partition "+str(i+1)+":", end="")
		partition_size.append(int(input()))
	print("--"*5)
	print("Enter no. of processes (<{}):".format(n_partition), end="")
	n_proc = int(input())
	proc_size = []
	for i in range(n_proc):
		print("Size for process "+str(i+1)+":", end="")
		proc_size.append(int(input()))

	print("--"*5)
	exf = []
	print("Allocating processes with best-fit algo.....")
	size = sum(partition_size)
	for n,i in enumerate(proc_size):
		t = [tp for tp in partition_size if tp>=i]
		t = min(t)
		size-=i
		print("Partition size for process {}: {}".format(n+1,t))
		partition_size.pop(partition_size.index(t))
		ef = t-i
		if ef>0:
			print("Internal Fragment size: {}".format(ef))
			exf.append(ef)
		
	print("--"*5)
	print("External Fragments:", exf)
	print("--"*5)
	print("Applying Compaction......")
	print("Free space available after compaction: {}".format(size))



if __name__=="__main__":
	try:
		main()
	except Exception as e:
		print("Error: {}".format(e))
