#from main import m_user
import user
import applicationMap
class task(object):
  def __init__(self):
    self.task_list = []

  def add_task(self, topic):
    
    task = input("What is the name of the new task")
    print(applicationMap.m_user.new_topic_def.task_list)
    applicationMap.m_user.topics[topic] = applicationMap.m_user.new_topic_def.task_list.append(task)
    print(applicationMap.m_user.topics[topic])
