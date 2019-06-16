class task(object):
    def __init__(self):
        self.task_list = []
        self.duration = None
        self.notes = None
        self.task = None
        self.task_def = []

    def update_list(self):
        self.task_def = [self.task, self.duration, self.notes]