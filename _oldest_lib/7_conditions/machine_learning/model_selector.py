from sklearn.multioutput import MultiOutputRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
# import autosklearn.regression

def model_selector(regressor):
  if regressor == 'gradient boosting':
    return MultiOutputRegressor(
      Pipeline(
          [
            ('min_max', MinMaxScaler()),
            ('reg', GradientBoostingRegressor())
          ]
      ) 
    )       
    # use grid search CV
  elif regressor == 'random forest':
    return MultiOutputRegressor(
    Pipeline(
      [
        ('min_max', MinMaxScaler()),
        ('reg', RandomForestRegressor(n_estimators=200, max_depth=10, random_state=0))
      ]
    )
  )
  # use grid search CV
  # epsilons to try (0.5, 0.1, 0.01, 0.001, 0.0001)
  # C values to try (10, 1, 0.1, 0.01, 0.001)
  elif regressor == 'support vector':
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', SVR())
        ]
      )
    )
    # try hidden layers (5,5,5) or (5,5)
    # use cross validationCV
    # https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
  elif regressor == 'neural net (relu)':
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', MLPRegressor(hidden_layer_sizes=(20, 20), tol=1e-2, max_iter=500, random_state=0, activation='relu'))
        ]
      )
    )
  elif regressor == 'neural net (tanh)':
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', MLPRegressor(hidden_layer_sizes=(20, 20), tol=1e-2, max_iter=500, random_state=0, activation='tanh'))
        ]
      )
    )
  elif regressor == 'neural net (log)':
    return MultiOutputRegressor(
      Pipeline(
        [
          ('min_max', MinMaxScaler()),
          ('reg', MLPRegressor(hidden_layer_sizes=(20, 20), tol=1e-2, max_iter=500, random_state=0, activation='logistic'))
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