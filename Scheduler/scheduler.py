from Scheduler.task import *


class Scheduler:
    TICK = 100
    SCH_MAX_TASKS = 40

    def __init__(self):
        self.SCH_tasks_G = []    
        self.current_index_task = 0

    def SCH_Init(self):
        self.current_index_task = 0
        self.SCH_tasks_G = []

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if len(self.SCH_tasks_G) < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.SCH_GenerateID()
            self.SCH_tasks_G.append(aTask)
            return aTask.TaskID
        else:
            print("Task list is full!")

    def SCH_Update(self):
        for task in self.SCH_tasks_G:
            if task.Delay > 0:
                task.Delay -= 1
            else:
                task.Delay = task.Period
                task.RunMe += 1

    def SCH_Dispatch_Tasks(self):
        for task in self.SCH_tasks_G:
            if task.RunMe > 0:
                task.RunMe -= 1
                task.pTask()

    def SCH_Delete(self, taskID):
        for i, task in enumerate(self.SCH_tasks_G):
            if task.TaskID == taskID:
                del self.SCH_tasks_G[i]
                return True
        return False

    def SCH_GenerateID(self):
        existing_ids = [task.TaskID for task in self.SCH_tasks_G]
        new_id = 0
        while new_id in existing_ids:
            new_id += 1
        return new_id