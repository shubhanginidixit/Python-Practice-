import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


data = {
    'Email_Length': [120, 50, 300, 45, 500, 60],
    'Has_Link': [1, 0, 1, 0, 1, 0],   # 1 = Yes, 0 = No
    'Spam': [1, 0, 1, 0, 1, 0]        # 1 = Spam, 0 = Not Spam
}

df = pd.DataFrame(data)

X = df[['Email_Length', 'Has_Link']]
y = df['Spam']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
