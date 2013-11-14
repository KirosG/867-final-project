import csv
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals.six import StringIO
from sklearn import cross_validation
import pydot 
from collections import Counter

data = np.loadtxt("fourier/energy.txt", delimiter=",")

X = []
y = []
for row in data:
    y.append(int(row[1]))
    X.append(map(int,row[2:]))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=.4, random_state=0)

clf = tree.DecisionTreeClassifier(max_depth=4)
clf = clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)

print score



with open("tree.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

graph = pydot.graph_from_dot_file('tree.dot')
graph.write_png('tree.png')

# dot_data = StringIO.StringIO() 
# tree.export_graphviz(clf, out_file=dot_data) 
# graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
# graph.write_pdf("tree.pdf") 