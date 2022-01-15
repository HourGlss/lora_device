current_screen = "Message from:                                               M                  "
address = "6000"
data = "hello world"
last_message = " "
next_message = "N"
next_screen = "{}{:<6}{:<40}{:<2} {} {}{}".format(current_screen[0:14], address,
                                                               data, current_screen[60:62], last_message,
                                                                      next_message,current_screen[66:])

print(next_screen)