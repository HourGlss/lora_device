current_screen = "Message from:                                               M                  "
address = "6000"
data = "hello world"
last_message = " "
next_message = "N"
next_screen = "{}{:<6}{:<40}{:<2} {} {}{}".format(current_screen[0:14], address,
                                                               data, current_screen[60:62], last_message,
                                                                      next_message,current_screen[66:])


addr_to_use = 100
data_to_send = {"address":400, "data":"Testing the data"}
message = "{}/{}/{}".format(str(addr_to_use), data_to_send['address'],
                                          str(data_to_send['data']))


sender = message.split("/")
print(message)
print(sender[0])