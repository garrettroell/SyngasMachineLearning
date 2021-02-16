from machine_learning.get_X_y_arrays import get_X_y_arrays_conc, get_X_y_arrays_slope
from machine_learning.model_selector import model_selector

def get_trained_models_conc_6(raw_df, smooth_df):

    trained_models = {}
    training_data_set = ['raw', 'smooth']
    regressor_set = ['gradient boosting', 'random forest', 'support vector', 'neural net', 'lasso']
    test_comp_set = ['none', 1, 2, 3, 4, 5, 6]

    for training_data in training_data_set:
      print(training_data)
      for regressor in regressor_set:
        print(regressor)
        for test_comp in test_comp_set:
          print(training_data + ', ' + regressor + ', comp excluded from training: ' + str(test_comp))

          # set up training set
          if training_data == 'raw':
            data = raw_df
          else:
            data = smooth_df

          # set up training comps
          training_comps = [1, 2, 3, 4, 5, 6]
          if test_comp != 'none':
            training_comps.remove(test_comp)

          # get input and output arrays
          X, y = get_X_y_arrays_conc(data, training_comps)

          # get ML model to use
          model = model_selector(regressor)

          model_name = regressor + ', ' + training_data + ', test comp = ' + str(test_comp)
          trained_models[model_name] = model.fit(X, y)

    return trained_models

def get_trained_models_conc_7(raw_df, smooth_df):

    trained_models = {}
    training_data_set = ['raw', 'smooth']
    regressor_set = ['gradient boosting', 'random forest', 'support vector', 'neural net', 'lasso']
    test_comp_set = ['none', 1, 2, 3, 4, 5, 6, 7]

    for training_data in training_data_set:
      print(training_data)
      for regressor in regressor_set:
        print(regressor)
        for test_comp in test_comp_set:
          print(training_data + ', ' + regressor + ', comp excluded from training: ' + str(test_comp))

          # set up training set
          if training_data == 'raw':
            data = raw_df
          else:
            data = smooth_df

          # set up training comps
          training_comps = [1, 2, 3, 4, 5, 6, 7]
          if test_comp != 'none':
            training_comps.remove(test_comp)

          # get input and output arrays
          X, y = get_X_y_arrays_conc(data, training_comps)

          # get ML model to use
          model = model_selector(regressor)

          model_name = regressor + ', ' + training_data + ', test comp = ' + str(test_comp)
          trained_models[model_name] = model.fit(X, y)

    return trained_models

def get_trained_models_slope_6(raw_df, smooth_df):

    trained_models = {}
    training_data_set = ['raw', 'smooth']
    regressor_set = ['gradient boosting', 'random forest', 'support vector', 'neural net', 'lasso']
    test_comp_set = ['none', 1, 2, 3, 4, 5, 6]

    for training_data in training_data_set:
      print(training_data)
      for regressor in regressor_set:
        print(regressor)
        for test_comp in test_comp_set:
          print(training_data + ', ' + regressor + ', comp excluded from training: ' + str(test_comp))

          # set up training set
          if training_data == 'raw':
            data = raw_df
          else:
            data = smooth_df

          # set up training comps
          training_comps = [1, 2, 3, 4, 5, 6]
          if test_comp != 'none':
            training_comps.remove(test_comp)

          # get input and output arrays
          X, y = get_X_y_arrays_slope(data, training_comps)

          # get ML model to use
          model = model_selector(regressor)

          model_name = regressor + ', ' + training_data + ', test comp = ' + str(test_comp)
          trained_models[model_name] = model.fit(X, y)

    return trained_models

def get_trained_models_slope_7(raw_df, smooth_df):

    trained_models = {}
    training_data_set = ['raw', 'smooth']
    regressor_set = ['gradient boosting', 'random forest', 'support vector', 'neural net', 'lasso']
    test_comp_set = ['none', 1, 2, 3, 4, 5, 6, 7]

    for training_data in training_data_set:
      print(training_data)
      for regressor in regressor_set:
        print(regressor)
        for test_comp in test_comp_set:
          print(training_data + ', ' + regressor + ', comp excluded from training: ' + str(test_comp))

          # set up training set
          if training_data == 'raw':
            data = raw_df
          else:
            data = smooth_df

          # set up training comps
          training_comps = [1, 2, 3, 4, 5, 6, 7]
          if test_comp != 'none':
            training_comps.remove(test_comp)

          # get input and output arrays
          X, y = get_X_y_arrays_slope(data, training_comps)

          # get ML model to use
          model = model_selector(regressor)

          model_name = regressor + ', ' + training_data + ', test comp = ' + str(test_comp)
          trained_models[model_name] = model.fit(X, y)

    return trained_models