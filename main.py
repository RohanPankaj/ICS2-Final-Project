import applicationMap




print(applicationMap.introuction_prompt)
print(applicationMap.instructions)

while True:

    action = input("What do you want to do? ")
    if action == "add task":
        topic, task = applicationMap.task_action_prompt()
        if applicationMap.m_user.check_if_active_topic(topic) == False:
            applicationMap.m_user.add_topic(topic)
        #topic = topic()
        applicationMap.m_user.topics[topic].add_task(topic, task)
    elif action == "add topic":
        u_topic = input("What is the name of the new topic")
        applicationMap.m_user.add_topic(u_topic)
        print(applicationMap.m_user.topics)
    elif action == "remove task":
        opic, task = applicationMap.task_action_prompt()
        applicationMap.m_user.delete_topic(u_topic)
    elif action == "remove topic":
        u_topic = input("What is the name of the topic you want to delete")
        applicationMap.m_user.delete_topic(u_topic)
    elif action == "print all":
        applicationMap.m_user.print_all()