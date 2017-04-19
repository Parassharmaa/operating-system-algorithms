def main():	
	print("Enter no. of processes:", end="")
	p = int(input())
	print("Enter no. of resources:", end="")
	r = int(input())

	print("Enter resource matrix:")
	resource_matrix = []
	for _ in range(p):
		temp = list(map(int, input().split()))
		resource_matrix.append(temp[:r+1])

	print("Enter allocation matrix:")
	allocation_matrix = []
	for _ in range(p):
	        temp = list(map(int, input().split()))
	        allocation_matrix.append(temp[:r+1])

	print("Enter available resources:", end="")
	available_resources = list(map(int , input().split()))


	if allocation_matrix > resource_matrix:
		print("Allocation matrix cannot be greater than resource matrix")
		exit()


if __name__=="__main__":
	while(True):
		try:
			main()
		except Exception as e:
			print("Error: {}".format(e))



