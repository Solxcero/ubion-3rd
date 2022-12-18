from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

class ScoreALL():

    def as_(self, y_test, pred):
            self.accuracy_score = accuracy_score(y_test, pred)
            return(print(f'accuracy_score : {self.accuracy_score:.4f}'))

    def ps_(self, y_test, pred):
            self.precision_score = precision_score(y_test,pred)
            return(print(f'precision_score : {self.precision_score:.4f}'))

    def rs_(self, y_test, pred):
            self.recall_score = recall_score(y_test,pred)
            return(print(f'recall_score : {self.recall_score:.4f}'))

    def f1_(self, y_test, pred):
            self.f1_score = f1_score(y_test,pred)
            return(print(f'f1_score : {self.f1_score:.4f}'))

    def r2_(self, y_test, pred):
            self.r2_score = r2_score(y_test,pred)
            return(print(f'r2_score : {self.r2_score:.4f}'))
    
    def evs_(self, y_test, pred):
            self.explained_variance_score = explained_variance_score(y_test,pred)
            return(print(f'explained_variance_score : {self.explained_variance_score:.4f}'))

    # def rc_(self, y_test, pred):
    #         self.f1_score = f1_score(y_test,pred)
    #         return(print(f'f1_score : {f1_score:.4f}'))            
 

    #         self.roc_curve = roc_curve(y_test,pred)
    #         self.roc_auc_score = roc_auc_score(y_test,pred)
    #