class Task:
    def __init__(self, pTask, Delay, Period):
        self.pTask = pTask
        self.Delay = Delay
        self.Period = Period
        self.RunMe = 0
        self.TaskID = None
