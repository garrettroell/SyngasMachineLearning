# Machine-Learning-Clostridium

A machine learning project written in python that predicts time course concentrations of biofuel production from syngas fermentations with Clostridium carboxyidivorans.

The goal of this project is to measure the effects of training data augmentation and machine learning algorithm selection.

The training data was augmented by polynomial smoothing and kinetic modeling. Machine learning models were developed to predict production rates and product concentrations. The two machine learning algorithms that were used were 

The code should be read in this order:
1) data_analysis.ipynb
2) ml_conc.ipynb
3) ml_slope.ipynb

The folders in lib/ contain .py files that have functions that are used in the notebooks.
