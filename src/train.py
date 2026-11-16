import pandas as pd
import matplotlib.pyplot as plt
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.metrics import(
    accuracy_score,precision_score,
    recall_score, f1_score,classification_report,
    confusion_matrix,ConfusionMatrixDisplay
)

BASE_DIR=Path(__file__).resolve().parent.parent
df=pd.read_csv(BASE_DIR/"data"/"cleaned_tickets.csv")
print(df.head())

X=df["ticket_description"]
y=df["category"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42,stratify=y)
print("Training records:", len(X_train))
print("Testing records:", len(X_test))

model=Pipeline([
    ("tfidf",TfidfVectorizer()),
    ("classifier",LogisticRegression(max_iter=1000))
])

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred,average="weighted",zero_division=0)
recall=recall_score(y_test,y_pred,average="weighted",zero_division=0)
f1=f1_score(y_test,y_pred,average="weighted",zero_division=0)

print(f"Accuracy:  {accuracy * 100}%")
print(f"Precision: {precision * 100}%")
print(f"Recall:    {recall * 100}%")
print(f"F1 Score:  {f1 * 100}%")

print(classification_report(y_test, y_pred))

cm=confusion_matrix(y_test,y_pred,labels=model.classes_)
print(cm)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

disp.plot(cmap="Blues")

plt.title("Customer Support Ticket Classification")
plt.savefig(BASE_DIR / "screenshots" / "confusion_matrix.png")
plt.show()

joblib.dump(model,BASE_DIR/"model"/"ticket_classifier.pkl")