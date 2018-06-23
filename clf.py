from sklearn import datasets
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import KFold
from sklearn.naive_bayes import BernoulliNB, MultinomialNB

# Load the movie reviews from file 
data = datasets.load_files("/UVic/2018/Summer/CSC421/assignment3/reviews", shuffle=False, categories=["pos", "neg"])
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
    print("Bernoulli [fold {0}] score: {1:.5f}".format(k, clf.score(X[test], y[test])))

# Calculate average prediction accuracy
score = score / 10
print("Bernoulli Average Score: {0:.5f}".format(score))

# Test with what should be obvious polarity reviews
print(clf.predict([[1,1,1,0,0,0,0,0], [0,0,0,0,1,1,0,1]]))

# Define our classifier and cross-validation
clf = MultinomialNB()
kf = KFold(n_splits=10, shuffle=True)
kf.get_n_splits(X)

# Perform cross-validation
score = 0
for k, (train, test) in enumerate(kf.split(X, y)):
    clf.partial_fit(X[train], y[train], [0,1])
    score += clf.score(X[test], y[test])
    print("MultinomialNB [fold {0}] score: {1:.5f}".format(k, clf.score(X[test], y[test])))

# Calculate average prediction accuracy
score = score / 10
print("MultinomialNB Average Score: {0:.5f}".format(score))
# Test with what should be obvious polarity reviews
print(clf.predict([[1,1,1,0,0,0,0,0], [0,0,0,0,1,1,0,1]]))