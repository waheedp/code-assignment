import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
import sys
import json

def load_data(learner_file, learner_workspace):
   y_learner = pd.read_csv(learner_file)
   y_actual = pd.read_csv(learner_workspace + 'actual.csv')
   return y_learner,y_actual

def validate_submission(y_learner):
   error = 0
   msg = "No error"
   if(list(y_learner.columns) != list(y_actual.columns)):
       msg = "The column names of the submission file do not match the submission format."
       error = 1
   if(y_learner.shape[0] != y_actual.shape[0]):
       msg = "The submission file should contain {} records".format(y_actual.shape[0])
       error = 1
   if(y_learner.shape[1] != y_actual.shape[1]):
       msg = "The submission file should contain {} columns".format(y_actual.shape[1])
       error = 1
   return error,msg

def score_submission(y_learner,y_actual):
   score =accuracy_score(y_learner.Cover_Type,y_actual.Cover_Type)
   if score > 0.83:
        points=1.0
   elif score <0.83 and score > 0.80 :
        points=0.80
   elif score < 0.80 and score > 0.75:
        points=0.70
   else:
        points=0
   
   return score,points
if __name__ == "__main__":
   learner_file = sys.argv[1]
   learner_workspace = sys.argv[2]
   y_learner,y_actual = load_data(learner_file, learner_workspace)
   err,msg = validate_submission(y_learner)
   if(err == 1):
       print(msg, end='')
   else:
       score,points = score_submission(y_learner,y_actual)
       result = json.dumps({'raw_score': score, 'multiplier': points})
       print(result, end='')