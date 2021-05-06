process_time = {}
n = int(input("Enter the number of processes >>>> "))
print("Now Enter their timestamps\n")
for i in range(n):
    process_time[i] = int(
        input(f"Enter the timestamp for Process : {i} >>>> "))

p1, p2 = input("Enter 2 process who wants a shared resource >>>> ").split(" ")
p1, p2 = int(p1), int(p2)
for i in range(n):
    print(
        f"Process : {p1} sends timestamp {process_time[p1]} to Process : {i}")
for i in range(n):
    print(
        f"Process : {p2} sends timestamp {process_time[p2]} to Process : {i}")

if(process_time[p1] < process_time[p2]):
    print(f"Process : {p1} has the lowest timestamp = {process_time[p1]}")
    for i in range(n):
        if(i == p1):
            continue
        else:
            print(f"Process : {i} sent OK! message to Process : {p1}")
    print(
        f"Hence Process : {p1} is accessing the shared resource, once it is done using it,\n Process : {p2} can use it")
elif(process_time[p2] < process_time[p1]):
    print(f"Process : {p2} has the lowest timestamp = {process_time[p2]}")
    for i in range(n):
        if(i == p2):
            continue
        else:
            print(f"Process : {i} sent OK! message to Process : {p2}")
    print(
        f"Hence Process : {p2} is accessing the shared resource, once it is done using it,\n Process : {p1} can use it")
