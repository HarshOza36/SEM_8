def allocate(servers, processes):
    each = int(processes/servers)
    proc_array = [i+1 for i in range(processes)]
    allocations = {}
    for i in range(servers):
        allocations[int(i)+1] = []
    for i in range(len(allocations)):
        for j in range(each):
            allocations[int(i+1)].append("P"+str(proc_array.pop(0)))
    if(len(proc_array) != 0):
        try:
            for i in range(len(allocations)):
                allocations[int(i+1)].append("P"+str(proc_array.pop(0)))
        except Exception as e:
            pass
    return allocations


def print_allocations(allocations):
    for i in range(len(allocations)):
        print(f"Server:{i+1} -> {allocations[i+1]}")


servers = int(input("Enter the initial amount of servers >>>> "))
processes = int(input("Enter the initial amount of processes >>>> "))

# Allocate
allocations = allocate(servers, processes)
print("Initial Allocation will be as shown below")
print_allocations(allocations)


ex_loop = ""
while (ex_loop.lower() != 's'):
    print("----------------------------------CASES---------------------------------------")
    print("1. Add servers  2. Add processes 3. Remove servers 4. Remove processes")
    print("-------------------------------------------------------------------------------")
    case = int(input("Enter the case you want to execute  >>>> "))
    if(case == 1):
        # Add New servers
        new_servers = int(input(
            f"Enter the new amount of servers to be added to old server count of {servers} >>>> "))
        servers = servers + new_servers
        allocations = allocate(servers, processes)
        print("New Allocation will be as shown below")
        print_allocations(allocations)
    elif(case == 2):
        # Add new processes
        new_procs = int(input(
            f"Enter the new amount of processes to be added to old process count of {processes} >>>> "))
        processes = processes + new_procs
        allocations = allocate(servers, processes)
        print("New Allocation will be as shown below")
        print_allocations(allocations)
    elif(case == 3):
        # Remove servers
        new_servers = int(input(
            f"Enter the amount of servers to be removed from old server count of {servers} >>>> "))
        servers = servers - new_servers
        allocations = allocate(servers, processes)
        print("New Allocation will be as shown below")
        print_allocations(allocations)
    elif(case == 4):
        # Remove processes
        new_procs = int(input(
            f"Enter the amount of processes to be removed from old process count of {processes} >>>> "))
        processes = processes - new_procs
        allocations = allocate(servers, processes)
        print("New Allocation will be as shown below")
        print_allocations(allocations)

    ex_loop = input("To continue press 'c' else press 's' to stop >>>>  ")
