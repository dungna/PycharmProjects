import numpy as np
import re
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from nltk.classify import SklearnClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

reviews = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training\Data_Mining_Training_V6_Week2\new train")
files, categories = reviews.data, reviews.target

reviews2 = load_files(r"C:\Users\Asus\PycharmProjects\Data Mining - Training\Data_Mining_Training_V6_Week2\new test")
files2, categories2 = reviews2.data, reviews2.target

# Test files
files_edited = []

for n in range(0, len(files)):
    file = str(files[n])
    # data stored as bytes => convert to string
    file = re.sub(r'\W', ' ', file)
    # Remove all the special characters
    file = re.sub(r'\s+[a-zA-Z]\s+', ' ', file)
    # remove all single characters
    file = re.sub(r'\s+', '', file, flags=re.I)
    # Substituting multiple spaces with single space
    file = re.sub(r'^b\s+', '', file)
    # Removing prefixed 'b'
    file = file.lower()
    # Converting to Lowercase
    files_edited.append(file)

files_edited2 = []
for n in range(0, len(files2)):
    file2 = str(files2[n])
    # data stored as bytes => convert to string
    file2 = re.sub(r'\W', ' ', file2)
    # Remove all the special characters
    file2 = re.sub(r'\s+[a-zA-Z]\s+', ' ', file2)
    # remove all single characters
    file2 = re.sub(r'\s+', '', file2, flags=re.I)
    # Substituting multiple spaces with single space
    file2 = re.sub(r'^b\s+', '', file2)
    # Removing prefixed 'b'
    file2 = file2.lower()
    # Converting to Lowercase
    files_edited2.append(file2)

vectorizer = TfidfVectorizer()
files_vectorized = vectorizer.fit_transform(files_edited).toarray()

clf = SVC()
clf.fit(files_vectorized, categories)

vectorizer2 = TfidfVectorizer()
files_vectorized2 = vectorizer2.fit_transform(files_edited2).toarray()

categories2_pred = clf.predict(files_vectorized2)
print(confusion_matrix(categories2, categories2_pred))
print(classification_report(categories2, categories2_pred))
print(accuracy_score(categories2, categories2_pred))

with open("svc_clf", "wb") as picklefile:
    pickle.dump(clf, picklefile)

# with open("svc_clf", "rb") as svc_clf:
#     clf = pickle.load(svc_clf)
#     categories2_pred = clf.predict(files_vectorized2)
#     print(confusion_matrix(categories2, categories2_pred))
#     print(classification_report(categories2, categories2_pred))
#     print(accuracy_score(categories2, categories2_pred))
