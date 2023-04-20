import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('tokenized_data.csv')
print(df.head())

x = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.10, random_state=1)

Encoder = LabelEncoder()
Train_Y = Encoder.fit_transform(y_train)
Test_Y = Encoder.fit_transform(y_test)

Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(df["text"])
Train_X_Tfidf = Tfidf_vect.transform(X_train)
Test_X_Tfidf = Tfidf_vect.transform(X_test)

SVM = SVC(C=3.6, kernel="poly", degree=1, gamma="scale")
SVM.fit(Train_X_Tfidf,Train_Y)

print("PREDICTED-----------ACTUAL")
predictions_SVM = SVM.predict(Test_X_Tfidf)
for i in predictions_SVM:
    t1=[predictions_SVM[i]]
    t2=[Test_Y[i]]
    print(Encoder.inverse_transform(t1)[0],"------",Encoder.inverse_transform(t2)[0])
print()
print("Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100) 
print()
print("Classification Report:-\n", classification_report(Test_Y, predictions_SVM))