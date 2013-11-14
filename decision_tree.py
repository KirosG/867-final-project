import numpy as np
from sklearn import tree
from sklearn import cross_validation
import pydot 
import sys


def max_tree(max_depth = None, out_file = None):
    """
    Creates decision tree of max_depth. If max_depth is None the tree's depth won't be bounded.

    If out_file is specificed, function will make a dot file and png of generated tree

    prints training and testing error to stdout
    """

    data = np.loadtxt("fourier/energy.txt", delimiter=",")

    X = []
    y = []
    for row in data:
        y.append(int(row[1]))
        X.append(map(int,row[2:]))

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.4, random_state=0)

    print X_train

    clf = tree.DecisionTreeClassifier(max_depth=max_depth)
    clf = clf.fit(X_train, y_train)

    print "trained tree of depth %s" % (max_depth) 
    print "training error:  %f" % (1-clf.score(X_train, y_train)) 
    print "testing error:  %f" % (1-clf.score(X_test, y_test)) 


    if out_file:
        with open(out_file+".dot", 'w') as f:
            f = tree.export_graphviz(clf, out_file=f)

        graph = pydot.graph_from_dot_file(out_file+".dot")
        graph.write_png(out_file+'.png')


if __name__ == "__main__":
    depth = None
    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
    
    out_file = None
    if len(sys.argv) > 2:
        out_file = sys.argv[2]

    max_tree(depth, out_file)


# dot_data = StringIO.StringIO() 
# tree.export_graphviz(clf, out_file=dot_data) 
# graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
# graph.write_pdf("tree.pdf") 