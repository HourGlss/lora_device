test = ['a', 'b', 'c']


def current_message():
    global index, test
    if index < 0:
        return None
    try:
        return test[index]
    except:
        return None


def next_message():
    global index, test
    if index + 1 < 0:
        return None
    try:
        return test[index+1]
    except:
        return None


def last_message():
    global index, test

    if index - 1 < 0:
        return None
    try:
        return test[index-1]
    except:
        return None

index = 3
print(last_message())
print(current_message())
print(next_message())
