from sklearn.metrics import confusion_matrix
import pylab as pl
import numpy as np
from random import shuffle


def split_training(activities, percent_training):
    train = {}
    test = {}

    for a in activities:
        shuffle(activities[a]) #shuffle so we train on a random subset
        start = int(len(activities[a])*percent_training)
        train[a] = activities[a][:start]
        test[a] = activities[a][start:]

    return train, test

def format_data(X, y):
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
            
            if len(add) > 19:
                activities[current_activity].append(np.array(add))
            
            #reset for next activity
            add = []
            current_activity = activity
        print(len(row[1]))
        add.append(row[1][0:3])

    return activities

def show_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)

    # Show confusion matrix in a separate window
    pl.matshow(cm)
    pl.title('Confusion matrix')
    pl.colorbar()
    pl.ylabel('True label')
    pl.xlabel('Predicted label')
    pl.show()

    return cm