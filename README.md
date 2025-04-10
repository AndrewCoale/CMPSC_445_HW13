# CMPSC_445_HW13

0 = low life expectancy (<60 yrs)  
1 = medium life expectancy (60-75 yrs)  
2 = high life expectancy (>75 yrs)  

## Logistic Regression Results  
Accuracy: 0.8469  
Classification Report:  

              precision    recall  f1-score   support    
           0       0.87      0.79      0.83       165  
           1       0.90      0.80      0.85       121  
           2       0.82      0.90      0.86       302  
           
    accuracy                           0.85       588  
    macro avg      0.86      0.83      0.84       588  
    weighted avg   0.85      0.85      0.85       588  


## BaggingClassifier Results
Accuracy: 0.9252  
Classification Report:  
  
              precision    recall  f1-score   support  
           0       0.94      0.88      0.91       165  
           1       0.93      0.94      0.93       121  
           2       0.92      0.94      0.93       302  
           
    accuracy                           0.93       588  
    macro avg      0.93      0.92      0.93       588  
    weighted avg   0.93      0.93      0.93       588  


## GradientBoostingClassifier Results
Accuracy: 0.9320  
Classification Report:  
  
              precision    recall  f1-score   support  
           0       0.95      0.88      0.91       165  
           1       0.95      0.95      0.95       121  
           2       0.92      0.95      0.94       302  
  
    accuracy                           0.93       588  
    macro avg      0.94      0.93      0.93       588  
    weighted avg   0.93      0.93      0.93       588  


## XGBClassifier Results
Accuracy: 0.9490  
Classification Report:  
  
              precision    recall  f1-score   support  
           0       0.97      0.89      0.93       165  
           1       0.97      0.97      0.97       121  
           2       0.93      0.97      0.95       302  
  
    accuracy                           0.95       588  
    macro avg      0.96      0.94      0.95       588  
    weighted avg   0.95      0.95      0.95       588  


# Preprocessing Discussion:
The preprocessing here was nothing too special, I just renamed the life expectancy column (the space annoyed me), dropped unnecessary columns (country and year), filled in missing columns, encoded the status column, standardized features, and made the life expectancy categorical, in 3 bins. This last one is because we needed to test classifiers, when life expectancy was a continuous value.

# Setting up Classifiers & Results:
The classifiers were very simple to use, the process was similar enough that I could declare all of them and loop through the same fitting/evaluation process. They happened to end up in order of accuracy, with logistic regression the worst performing, at 84%, and XGB the best, approaching 95%. 
