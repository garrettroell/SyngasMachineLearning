from sklearn.multioutput import MultiOutputRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import GridSearchCV
# import autosklearn.regression

def model_selector(regressor):
  
  if regressor == 'gradient boosting':
    parameters = {'n_estimators':[5, 20, 100, 200], 'max_depth':[2, 5, 10, 20]}
    return MultiOutputRegressor(
      Pipeline(
          [
            ('min_max', MinMaxScaler()),
            ('reg', GridSearchCV(GradientBoostingRegressor(), parameters, n_jobs=-1))
          ]
      ) 
    )       
    # use grid search CV
  elif regressor == 'random forest':
    parameters = {'n_estimators':[5, 20, 100, 200], 'max_depth':[2, 5, 10, 20]}
    return MultiOutputRegressor(
    Pipeline(
      [
        ('min_max', MinMaxScaler()),
        ('reg', GridSearchCV(RandomForestRegressor(random_state=0), parameters, n_jobs=-1))
      ]
    )
  )
  # use grid search CV
  # epsilons to try (0.5, 0.1, 0.01, 0.001, 0.0001)
  # C values to try (10, 1, 0.1, 0.01, 0.001)
  elif regressor == 'support vector':
    parameters = {'kernel':('linear', 'rbf'), 'C':[10, 1, 0.1, 0.01, 0.001], 'epsilon':[0.5, 0.1, 0.01, 0.001, 0.0001] }

    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', GridSearchCV(SVR(), parameters, n_jobs=-1))
        ]
      )
    )
    # try hidden layers (5,5,5) or (5,5)
    # use cross validationCV
    # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
  elif regressor == 'neural net':
    parameters = {'activation': ['relu', 'tanh', 'logistic'], 'hidden_layer_sizes':[(20, 20), (5,5,5), (5,5)],  'max_iter':[10, 100, 500]}

    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', GridSearchCV(MLPRegressor(random_state=0), parameters, n_jobs=-1))
        ]
      )
    )
  elif regressor == 'lasso':
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', LassoCV(n_jobs=-1))
        ]
      )
    )

  else: 
      print('unknown regressor')