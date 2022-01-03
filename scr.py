menu = ("* Send", "* Messages", "* Settings")
next_screen = ""
for item in menu:
    next_screen += "{:<20}".format(item)
print(next_screen)