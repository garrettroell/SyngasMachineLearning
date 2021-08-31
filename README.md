# An evaluation of machine learning algorithms in predicting Clostridium syngas fermentation outcomes with limited experimental data

The purpose of this study is to determine the feasibility of using machine learning to model production rates from syngas fermentation. In this study, we transformed time course metabolite concentration data from ten syngas fermentation conditions to calculate production rates of four products: acetate, ethanol, butyrate, and butanol. The data was used to train and test six machine learning algorithms’ ability to predict the rate of production of the four products. We found support vector machine performed the best on unseen testing data when performance across all conditions were considered. We also found that models with relatively few fitted variables, including elastic net and lasso, had the most consistent performance while models with more fitted variables, including neural networks and random forests, had greater variability in their prediction accuracy. Additionally, feature importance analysis was able to reproduce domain knowledge that the most important gas components for producing butyrate and butanol are carbon monoxide and hydrogen gas respectively. 

-   [System Requirements](#system-requirements)
-   [Instructions for use](#instructions-for-use)
-   [Summary of notebooks](#summary-of-notebooks)
-   [Reference](#reference)
-   [License](#license)


## System Requirements
The code was tested using python 3.7

## Instructions for use
To run the code in this repository use the following commands:
git clone https://github.com/garrettroell/Machine-Learning-Clostridium.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Summary of notebooks
Notebook A: Converts experimental data into smoothed data with rows that contain pairs of reactor conditions and production rates
Notebook B: Finds the optimal hyperparameters for the algorithms using a grid search with shuffle/split cross validation
Notebook C: Trains the models with optimal hyperparameters from notebook B and evaluates their performance on training and test data 

## Reference
This project is currently undergoing peer review

## License

This code is distributed under the 3-Clause BSD license specified in the [License][1] file. It is open source and commercially usable.

---

[1]: license