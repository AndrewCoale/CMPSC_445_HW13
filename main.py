import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
df = pd.read_csv("Life Expectancy Data.csv")

# Drop 'Country' and 'Year'
df.drop(columns=['Country', 'Year'], inplace=True)

# Rename the target column
df.rename(columns={'Life expectancy ': 'LifeExpectancy'}, inplace=True)

# Fill missing values with median
df.fillna(df.median(numeric_only=True), inplace=True)

# Encode 'Status' column
df['Status'] = LabelEncoder().fit_transform(df['Status'])

# Binning LifeExpectancy into classes
bins = [0, 60, 75, 100]
labels = ['Low', 'Medium', 'High']
df['LifeExpectancyCategory'] = pd.cut(df['LifeExpectancy'], bins=bins, labels=labels)

# Split into features and targets
X = df.drop(columns=['LifeExpectancy', 'LifeExpectancyCategory'])
y_clf = LabelEncoder().fit_transform(df['LifeExpectancyCategory'])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_clf, test_size=0.2, random_state=42)

# Define classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "BaggingClassifier": BaggingClassifier(random_state=42),
    "GradientBoostingClassifier": GradientBoostingClassifier(random_state=42),
    "XGBClassifier": XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42)
}

# Train, predict, and evaluate
for name, clf in classifiers.items():
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(f"\n{name} Results")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
