import pandas as pd
from sklearn.linear_model import LogisticRegression

pd.options.display.max_columns = 12
test = pd.read_csv('concedieri_test.csv')
train = pd.read_csv('concedieri_train.csv')

print('*****test*****')
print(test[:4])
print('*****train*****')
print(train[:4])

train.fillna(train.mean(), inplace=True)
test.fillna(test.mean(), inplace=True)
print(train.isna().sum())
print(test.isna().sum())

train['Barbat'] = (train['Sex'] == 'M').astype(int)
test['Barbat'] = (test['Sex'] == 'M').astype(int)

predictors = ['Vechime', 'Barbat', 'Salariu']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Concediat'].values
y_test = test['Concediat'].values
print(X_train[:5])
print(y_train[:5])

model = LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                           intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
                           penalty='l2', random_state=None, solver='lbfgs', tol=0.0001,
                           verbose=0, warm_start=False)

model.fit(X_train, y_train)
y_predict = model.predict(X_test)
print(y_predict)

print((y_test == y_predict).mean())
