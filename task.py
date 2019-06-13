#from main import m_user
import user
import applicationMap


class topic(object):
    def __init__(self):
        self.task_list = []
        self.duration = None
        self.notes = None
        self.topic_def = [self.task_list, self.duration, self.notes]

    def add_task(self, topic):

        task = input("What is the name of the new task")

        applicationMap.m_user.topics[topic] = applicationMap.m_user.new_topic_def.topic_def
        applicationMap.m_user.topics[topic][0].append(task)
        print(applicationMap.m_user.topics[topic])
