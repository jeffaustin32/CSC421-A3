from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
import os 
path = os.path.dirname(os.path.realpath(__file__))

# Load the movie reviews from file 
data = datasets.load_files(path + "/reviews", shuffle=False, categories=["pos", "neg"])
# Get index->label relationships
y = data.target

# Vectorize the movie reviews using our 8 words
vect = CountVectorizer(vocabulary=["awful", "bad", "boring", "dull", "effective", "enjoyable", "great", "hilarious"])
X = vect.fit_transform(data.data)
X = X.toarray()

# Define our classifier and cross-validation
clf = BernoulliNB(binarize=True)
kf = KFold(n_splits=10, shuffle=True)
kf.get_n_splits(X)

# Perform cross-validation
score = 0
for k, (train, test) in enumerate(kf.split(X, y)):
    clf.partial_fit(X[train], y[train], [0,1])
    score += clf.score(X[test], y[test])

# Calculate average prediction accuracy
score = score / 10
print("Bernoulli Average Score: {0:.5f}".format(score))

# Define our classifier and cross-validation
clf = MultinomialNB()
kf = KFold(n_splits=10, shuffle=True)
kf.get_n_splits(X)

# Perform cross-validation
score = 0
for k, (train, test) in enumerate(kf.split(X, y)):
    clf.partial_fit(X[train], y[train], [0,1])
    score += clf.score(X[test], y[test])

# Calculate average prediction accuracy
score = score / 10
print("MultinomialNB Average Score: {0:.5f}".format(score))