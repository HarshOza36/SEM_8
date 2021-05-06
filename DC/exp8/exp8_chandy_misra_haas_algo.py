print("------------------Input Process Graph for the Program-------------------")
print("  _________ 1 --> 3")
print(" |          ^")
print(" |          |")
print(" |-> 0 -- > 2 -> 4")
print("\n")
procs = int(input("Enter the number of processes >>>> "))
print("Enter the resources of each process >>>> ")
resource_array = [(list(map(int, input().split()))) for i in range(procs)]


print("Initiating Chandy Misra Haas Algorithm from Process 0 >>>> ")
flag = False
initiator = 0
prob_msg_list = []
dead_proc_init = ""
dead_proc_recv = ""
print("Probe Message Creation >>>>")
for i in range(procs):
    for j in range(procs):
        if(resource_array[i][j] == 1):
            prob_msg = (initiator, i, j)
            print(
                f"Probe Message : {prob_msg} with Initiating Process:{initiator} and Receiving Process:{j}")
            prob_msg_list.append(prob_msg)
for i in range(procs):
    for j in range(procs):
        if(prob_msg_list[i][0] == prob_msg_list[j][2]):
            flag = True
            dead_proc_init = prob_msg_list[i][0]
            dead_proc_recv = prob_msg_list[j][2]

if(flag == False):
    print("\n From the probe message list we can see that,\nNo Deadlock was not detected in the system when initiator is process 0")
else:
    print(
        f"\n From the probe message list we can see that,\nThe Deadlock was detected in the system when initiator is process 0 when the initiating process is {prob_msg_list[i][0]} and Receiving Process is also {prob_msg_list[i][0]}")
