import data
from sklearn.hmm import GaussianHMM
import numpy as np
from random import shuffle
import utils


def split_training(activities, num_training):
    train = {}
    test = {}


    for a in activities:
        shuffle(activities[a]) #shuffle so we train on a random subset
        train[a] = activities[a][:num_training]
        test[a] = activities[a][num_training:]

    return train, test


def train_hmm(X):
    # print X[0].transpose().shape
    print len(X)
    print X[0]
    hmm = GaussianHMM(n_components=5)
    hmm.fit(X)
    return hmm

def train_all_hmm(activities):
    hmms = {}
    for a in activities:
        print "Training hmm for activity %s" % (a)
        hmms[a] = train_hmm(activities[a])

    return hmms

def classify_activity(a, hmms):
    best_score = None
    best_activity = None

    for hmm in hmms:
        score = hmms[hmm].score(a)
        if best_score is None or score > best_score:
            best_score = score
            best_activity = hmm

    return best_activity

def test_error(test_activites, hmms):
    total = 0.
    incorrect = 0.

    y_test = []
    y_pred = []
    for a in test_activites:
        for x in test_activites[a]:
            total += 1
            y_test.append(a)
            pred = classify_activity(x, hmms)
            y_pred.append(pred)
            print pred
            if a != pred:
                incorrect += 1

    utils.show_confusion_matrix(y_test, y_pred)
    
    return incorrect/total

if __name__ == "__main__":
    X, y = data.load_time()


    #format data 
    activities = {}
    add = []
    current_activity = y[0]
    for row in zip(y,X):
        activity = row[0]
        # reached new activity
        if current_activity != activity:
            # add current activity
            if current_activity not in activities:
                activities[current_activity] = []
            
            if len(add) > 5:
                activities[current_activity].append(np.array(add))
            
            #reset for next activity
            add = []
            current_activity = activity

        add.append(row[1])

    train, test = split_training(activities, 4)

    hmms = train_all_hmm(train)

    error = test_error(test, hmms)

    print error

    # # X = [np.array(x) for x in activities[2]]
    # print len(X), X[:2]
    # print train_hmm(X)
        

