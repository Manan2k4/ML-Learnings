from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

X,y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)

# define parameter space that will be searched over
param_distributions = {'n_estimators': randint(1,5),
                      'max_depth': randint(5,10)}

# now create a searchCV object and fit it to the data
search = RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0),
                            n_iter=5,
                            param_distributions=param_distributions,
                            random_state=0)

print(search.fit(X_train, y_train))

print(search.best_params_)

# the search object now acts like a normal random forest estimator
# with max_depth = 9 and n_estimators = 4
print(search.score(X_test, y_test))