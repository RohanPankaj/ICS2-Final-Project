from task import task
import applicationMap
#from task.add_task import u_topic
class user(object):
  def __init__(self):
    self.topics = {}
  def add_topic(self, new_topic):
      print("yay again")
      new_topic
      
      self.new_topic_def = task()
    
      
      self.topics[new_topic] = self.new_topic_def
      print(self.topics)
      #return self.topics
  def delete_topic(self, old_topic):
    self.topics.remove(old_topic)
  
  def check_if_active_topic(self, topic):
    #global applicationMap.m_user.add_topic(topic)
    if topic not in applicationMap.m_user.topics:
      print("yay")
      return False


  
