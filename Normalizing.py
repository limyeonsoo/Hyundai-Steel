import pandas as pd

def normalize(df, norm_feature=None):
    if not norm_feature:
        norm_feature = ['tem_loc1', 'hum_loc1', 'coil_loc1', 
                        'tem_loc2', 'hum_loc2', 'coil_loc2', 
                        'tem_loc3', 'hum_loc3', 'coil_loc3', 
                        'tem_out',  'hum_out']
    result = df.copy()
    
    for feature_name in df.columns:
        if feature_name not in norm_feature: continue
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result