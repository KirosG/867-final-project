import data
from sklearn.hmm import GaussianHMM
import numpy as np
import utils



def train_hmm(X):
    hmm = GaussianHMM(n_components=8)
    hmm.fit(X);
    print hmm.score(X[0])
    print np.shape(X[0])
    return hmm

def train_all_hmm(activities):
    hmms = {}
    for a in activities:
        print "Training hmm for activity %s" % (a)
        hmms_a = train_hmm(activities[a]);
        #for X in activities[a]:
        #    hmms_a.append(train_hmm(X));
        hmms[a] = hmms_a;

    return hmms

def classify_activity(a, hmms):
    best_score = None
    best_activity = None

    for hmm in hmms:
        #for hmm_a in hmms[hmm]:
            #score = hmm_a.score(a)
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
    activity_error = [0]*(len(hmms)+1);
    activity_count = [0]*(len(hmms)+1);
    for a in test_activites:
        for x in test_activites[a]:
            total += 1
            activity_count[a] += 1;
            y_test.append(a)
            pred = classify_activity(x, hmms)
            y_pred.append(pred)
            #print pred
            if a != pred:
                incorrect += 1
                activity_error[a] += 1;

    for a in test_activites:
        print "Activity " + str(a) + ": " + str(float(activity_error[a])/activity_count[a]);

    utils.show_confusion_matrix(y_test, y_pred)
    
    return incorrect/total

if __name__ == "__main__":
    X, y = data.load_time()


    activities = utils.format_data(X, y)
    
    train, test = utils.split_training(activities, .2)

    hmms = train_all_hmm(train)

    error = test_error(test, hmms)

    print error

    #for a in activities:
    #    print "Activity " + str(a);
    #    for array in activities[a]:
    #        print np.shape(array);
    # # X = [np.array(x) for x in activities[2]]
    # print len(X), X[:2]
    # print train_hmm(X)
        

