from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score,recall_score,f1_score,roc_auc_score
from sklearn.model_selection import train_test_split


# Carregar os dados
data = load_breast_cancer()

# Dividir os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Criar e treinar o modelo

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Realizar previsões
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]


# Avaliar o modelo
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1_score = f1_score(y_test, y_pred)
roc_auc_score = roc_auc_score(y_test, y_pred_proba)

# Exibir os dados
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1 Score: {f1_score:.4f}')
print(f'ROC AUC Score: {roc_auc_score:.4f}')

