import data
from sklearn.hmm import GaussianHMM
import numpy as np

def train_hmm(X):
    # print X[0].transpose().shape
    hmm = GaussianHMM(n_components=5)
    hmm.fit(X)
    return hmm.predict(X[5]), hmm.score(X[5]), 

    

if __name__ == "__main__":
    X, y = data.load_time()


    #format data 
    activities = {}
    add = []
    current_activity = ""
    for row in zip(map(int,y),X):
        activity = row[0]
        if current_activity != activity:
            if current_activity not in activities:
                activities[current_activity] = []

            activities[current_activity].append(add)
            add = []
            current_activity = activity

        add.append(row[1])


    X = [np.array(x) for x in activities[2]]
    print len(X), X[:2]
    print train_hmm(X)
        

