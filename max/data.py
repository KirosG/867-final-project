import numpy as np

def load_fourier():
    data = np.loadtxt("../fourier/energy.txt", delimiter=",")
    X = []
    y = []
    # for row in data:
    #     row = map(int, row)
    #     y.append(row[1])
    #     X.append(row[2:])
    num_combin = 2
    for i in range(0, len(data), num_combin):
        x = []
        for j in range(num_combin):
            x += map(int, data[i+j])[2:]

        y.append(data[i][1])
        X.append(x)

    return X,y

def load_time():
    data = np.loadtxt("../statistics/stats.txt", delimiter=",", skiprows=1)
    X = []
    y = []
    # for row in data:
    #     row = map(int, row)
    #     y.append(row[1])
    #     X.append(row[2:])
    for row in data:
        y.append(int(row[1]))
        X.append(map(float, row[3:]))

    return X,y


def load_raw():
    data = np.loadtxt("../fourier/raw.txt", delimiter=",")
    X = []
    y = []
    # for row in data:
    #     row = map(int, row)
    #     y.append(row[1])
    #     X.append(row[2:])
    for row in data:
        row = map(float, row)
        y.append(int(row[1]))
        X.append(map(float, row[3:]))

    return X,y