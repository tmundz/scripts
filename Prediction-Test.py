import pandas as pd
from stpredict import stpredict




# Spatial data
#-------------

 

# Temporal data 
#--------------


dict = {'temporal id level 1': 'Week',
        'spatial id level 1': 'Sector',

        'temporal covariates':['TotalArrests',
                               'Unarmed',
                               'Armed',
                               'DrugRelated',
                               'Male',
                               'Female',
                               'White',
                               'Black',
                               'Hispanic or Latino',
                               'PUBLIC INTOXICATION',
                               'DRUG/ NARCOTIC VIOLATIONS',
                               'DUI',
                               'ALL OTHER OFFENSES'
                               ],
        
        
        'spatial covariates':['Population'],
        
        'target':'TotalArrests',}

df1 = pd.read_csv('Database-16week.csv')
df2 = pd.read_csv('Spatial_data.csv')

#pandas correlation

def main ():
    stpredict(data = {'temporal_data':df1,'spatial_data':df2},
              forecast_horizon = 12,
              history_length = {('TotalArrests',
                               'Unarmed',
                               'Armed',
                               'DrugRelated',
                               'Male',
                               'Female',
                               'White',
                               'Black',
                               'Hispanic or Latino',
                               'PUBLIC INTOXICATION',
                               'DRUG/ NARCOTIC VIOLATIONS',
                               'DUI',
                               'ALL OTHER OFFENSES'):1},

              column_identifier = dict, #default is None
              feature_sets = {'covariate': 'mRMR'},
              models = [{'knn':{'n_neighbors':[20], 'metric':'minkowski'}}], #['knn'] or models = [{'knn':{'n_neighbors':[10], 'metric':'minkowski'}}]
              model_type = 'regression',
              test_type = 'one-by-one', # one-by-one, whole-as-one
              mixed_models = [],
              performance_benchmark = 'MAPE', #{'MAE', 'MAPE', 'MASE', 'MSE', 'R2_score', 'AUC','AUPR', 'likelihood', 'AIC', 'BIC'}
              performance_measures = ['MAPE'],
              performance_mode = 'normal', #Cumulative
              splitting_type = 'training-validation',
              instance_testing_size = 0.2, #default 0.2
              instance_validation_size = 0.3, #default 0.3
              instance_random_partitioning = False,
              fold_total_number = 5,
              imputation = True,
              target_mode = 'normal', #same as performance mode
              feature_scaler = None,
              target_scaler = None,
              forced_covariates = [],
              futuristic_covariates = None,
              scenario = 'current', # max, min, mean, current, None
              future_data_table = None,
              temporal_scale_level = 1,
              spatial_scale_level = 1,
              spatial_scale_table = None,
              aggregation_mode = 'mean',
              augmentation = False,
              validation_performance_report = True,
              testing_performance_report = True,
              save_predictions = True,
              save_ranked_features = True,
              plot_predictions = False,
              verbose = 1)
if __name__ == '__main__':
    main()