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
    data = np.loadtxt("../statistics/stats_quick2.txt", delimiter=",", skiprows=1)
    X = []
    y = []
    user = []
    # for row in data:
    #     row = map(int, row)
    #     y.append(row[1])
    #     X.append(row[2:])
    count = 0;
    for row in data:
        user.append(int(row[0]));
        y.append(int(row[1]))
        X.append(map(float, row[3:]))
        count += 1
    order = sorted(xrange(count), key=lambda i: user[i]);
    #print order
    return [X[i] for i in order],[y[i] for i in order]
    #return X,y


def load_raw():
    data = np.loadtxt("../fourier/raw.txt", delimiter=",")
    X = []
    y = []
    user = []
    # for row in data:
    #     row = map(int, row)
    #     y.append(row[1])
    #     X.append(row[2:])
    count = 0;
    for row in data:
        row = map(float, row)
        user.append(int(row[0]));
        y.append(int(row[1]))
        X.append(map(float, row[3:]))
        count += 1;
    order = sorted(xrange(count), key=lambda i: user[i]);
    #print order
    return [X[i] for i in order],[y[i] for i in order]
    #return X,y