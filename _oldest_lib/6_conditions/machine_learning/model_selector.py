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
            ('reg', GridSearchCV(GradientBoostingRegressor(), parameters))
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
        ('reg', GridSearchCV(RandomForestRegressor(random_state=0), parameters))
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
          ('reg', GridSearchCV(SVR(), parameters))
        ]
      )
    )
    # try hidden layers (5,5,5) or (5,5)
    # use cross validationCV
    # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
  elif regressor == 'neural net (relu)':
    parameters = {'hidden_layer_sizes':[(20, 20), (5,5,5), (5,5)],  'tol':[0.1, 0.01, 0.001], 'max_iter':[10, 100, 500]}

    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', GridSearchCV(MLPRegressor(activation='relu', random_state=0), parameters))
        ]
      )
    )
  elif regressor == 'neural net (tanh)':
    parameters = {'hidden_layer_sizes':[(20, 20), (5,5,5), (5,5)], 'tol':[0.1, 0.01, 0.001], 'max_iter':[10, 100, 500]}
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', GridSearchCV(MLPRegressor(activation='tanh', random_state=0), parameters))
        ]
      )
    )
  elif regressor == 'neural net (log)':
    parameters = {'hidden_layer_sizes':[(20, 20), (5,5,5), (5,5)], 'tol':[0.1, 0.01, 0.001], 'max_iter':[10, 100, 500]}
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', GridSearchCV(MLPRegressor(activation='logistic', random_state=0), parameters))
        ]
      )
    )
  elif regressor == 'lasso':
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', LassoCV())
        ]
      )
    )
  # elif regressor == 'ensemble':
  #   return MultiOutputRegressor(
  #     Pipeline(
  #       [
  #         ('min_max', MinMaxScaler()),
  #         ('reg', LassoCV())
  #       ]
  #     )
  #   )
  else: 
      print('unknown regressor')