from timeit import default_timer as timer
from dateutil import parser
import datetime
import time


def print_nodes(time_array):
    print("Nodes with their Time")
    for i in range(len(time_array)):
        print(f"N{i+1} Time : {time_array[i]}")


def time_diff(a, b):
    a = datetime. datetime. strptime(a, "%H:%M")
    b = datetime. datetime. strptime(b, "%H:%M")
    seconds = (a-b).total_seconds()
    return - seconds/60


def adjust_time(a, b):
    a = datetime. datetime. strptime(a, "%H:%M")
    b = datetime. datetime. strptime(b, "%H:%M")
    seconds = (a-b).total_seconds()
    return((b + datetime.timedelta(seconds=seconds)).strftime('%I:%M'))


master_time = datetime.datetime.now().strftime('%I:%M')
total_slaves = int(input("Enter the total number of slaves >>>> "))

print("The nodes are >>>> ", end="")
print("N1(Master)", end="")
for i in range(total_slaves):
    print(f' N{i+2}', end="")

time_array = [master_time]
print("\nEnter time for each slave node (Input format should be HH:MM)")
for i in range(total_slaves):
    time_ip = input(f"Enter time for N{i+2} >>>> ")
    time_ip = datetime.datetime.strptime(
        time_ip, "%H:%M").strftime('%I:%M')
    time_array.append(time_ip)


print_nodes(time_array)

difference_array = []
for i in range(total_slaves+1):
    difference_array.append(time_diff(master_time, time_array[i]))
print(difference_array)

avg_time = sum(difference_array)/len(difference_array)
print(f"Average of time difference is {avg_time}")

print("Adjusting time now ..... ")
# Master clock time
hh, mm = time_array[0].split(":")
mm = int(int(mm)+avg_time)
time_array[0] = f"{hh}:{mm}"

# Adjusting Slave time
for i in range(len(time_array)-1):
    time_array[i+1] = adjust_time(time_array[0], time_array[i+1])

print_nodes(time_array)
