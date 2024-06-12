from Scheduler.scheduler import *
import time

scheduler = Scheduler()
scheduler.SCH_Init()

c = 0
def privateTask1():
    print("Run task1")

def privateTask2():
    global c, task2ID
    print("Run task2")
    c += 1
    if c == 15:
        check = scheduler.SCH_Delete(task2ID)
        if check == True:
            task2ID = None

def privateTask3():
    print("Run task3")

def privateTask4():
    print("Run task4")

print("Create a new task1")
print("Create a new task2")
task1ID = scheduler.SCH_Add_Task(privateTask1, 1, 5000)
task2ID = scheduler.SCH_Add_Task(privateTask2, 1, 5000)
task3ID = None
task4ID = None

counter = 0

while True:
    counter += 1
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    if counter == 1:
        print(f"ID: task1: {task1ID} -- task2: {task2ID} -- task3: {task3ID} -- task4: {task4ID}")
        print("-----------------------")
    if counter == 100:
        check = scheduler.SCH_Delete(task1ID)
        print(f"Delete task1 is: {check}")
        if check == True:
            task1ID = None
        print("-----------------------")
    if counter == 200:
        print(f"ID: task1: {task1ID} -- task2: {task2ID} -- task3: {task3ID} -- task4: {task4ID}")
        print("-----------------------")
    if counter == 300:
        print("Create a new task3")
        task3ID = scheduler.SCH_Add_Task(privateTask3, 1, 5000)
        print("-----------------------")
    if counter == 300:
        print(f"ID: task1: {task1ID} -- task2: {task2ID} -- task3: {task3ID} -- task4: {task4ID}")
    if counter == 400:
        print("Create a new task4")
        task4ID = scheduler.SCH_Add_Task(privateTask4, 1, 5000)
        print("-----------------------")
    if counter == 500:
        print(f"ID: task1: {task1ID} -- task2: {task2ID} -- task3: {task3ID} -- task4: {task4ID}")
        print("-----------------------")
    if counter == 600:
        check = scheduler.SCH_Delete(task3ID)
        print(f"Delete task3 is: {check}")
        if check == True:
            task3ID = None
        print("-----------------------")
    if counter == 700:
        print(f"ID: task1: {task1ID} -- task2: {task2ID} -- task3: {task3ID} -- task4: {task4ID}")
        print("-----------------------")
    if counter == 900:
        print(f"ID: task1: {task1ID} -- task2: {task2ID} -- task3: {task3ID} -- task4: {task4ID}")
        print("-----------------------")
    if counter == 1000:
        break