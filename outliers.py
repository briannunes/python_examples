import numpy as np
import pandas as pd
dataset= [10,12,12,13,12,11,14,13,15,10,10,10,188,12,14,13, 12,10, 200, 10,11,12,15,12,13,12,11,14,13,15,10,15,12,10,14,13,15,10,175]
#dataset= [1012,1213,1211,1413,1510,1010,1000000,1001,1002,1413, 1210, 1011,1215,1213,10]
#dataset= [
outliers=[]
total=len(dataset)

def detect_outlier(data_1):
    
    threshold=3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    count=0

    for y in data_1:
        count+=1
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append({"out": y, "count": count})
    return outliers


outlier_datapoints = detect_outlier(dataset)
total_outs=len(outlier_datapoints)
print(outlier_datapoints)
print(f"Records:", total)
print(f"Total Outs:", total_outs)

for y in outlier_datapoints:
    for key in y:
        if key == 'count':
             alert_key = (y[key])
        if key == 'out':
             alert_value = (y[key])
    if alert_key == total:
       print("Alert for Today:") 

sorted(dataset)
q1, q3= np.percentile(dataset,[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr) 
print(f"Lower Bound:", lower_bound)
print(f"Upper Bound:", upper_bound)
