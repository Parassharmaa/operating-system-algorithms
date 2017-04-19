process_queue = []
total_wtime = 0
n = int(input('Enter the total no of processes: '))
for i in range(n):
    process_queue.append([])
    process_queue[i].append(input('Enter p_name: '))
    process_queue[i].append(int(input('Enter p_burst: ')))
    print()

process_queue.sort(key = lambda process_queue:process_queue[1])

total_wtime = 0
for i in process_queue[:n-1]:
	total_wtime+=total_wtime+i[1]
print('ProcessName\tBurstTime')
for i in range(n):
    print(process_queue[i][0],'\t\t',process_queue[i][1])
    
print('Total waiting time: ',total_wtime)
print('Average waiting time: ',(total_wtime/n))