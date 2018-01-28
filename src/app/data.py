data = {'active_tab': 1}


def update_data(*args):
    global data
    for i in range(0, len(args), 2):
        data[args[i]] = args[i + 1]
