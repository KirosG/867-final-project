from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn import cross_validation
import data
import sys

def run_method(clf, X, y):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.4, random_state=0)

    clf.fit(X_train, y_train)  

    return (1-clf.score(X_train, y_train)), (1-clf.score(X_test, y_test)) 

if __name__ == "__main__":
    

    methods = {
    	"random_forest" : RandomForestClassifier,
    	"svm" : svm.SVC,
    	
    }

    sources = {
    	'time' : data.load_time,
    	'fourier' : data.load_fourier
    }

    if len(sys.argv) > 1:
        method = sys.argv[1]

    source = "time"
    if len(sys.argv) > 2:
        source = sys.argv[2]

    X, y = sources[source]()

    train, test = run_method(methods[method](), X, y)

    print "training error:  %f" % (train)
    print "testing error:  %f" % (test)