def fibona(num):
    fibs = [0,1]

    for i in range(num-2):
        fibs.append(fibs[ -2 ]+fibs[ -1 ])

    return(fibs)
