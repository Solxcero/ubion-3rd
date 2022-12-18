from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from xgboost import XGBRegressor

class RegALL():
    def Logreg(self, X_train, X_test, y_train, pred=False, score=False):
        self.logr = LogisticRegression()
        self.logr.fit(X_train, y_train.astype(int))
        self.pred = self.logr.predict(X_test)
        self.score_logr = self.logr.score(X_train, y_train.astype(int)).round(4)
        if pred == True & score == True:
            return self.pred, self.score_logr
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_logr
        else :
            return print('pred 혹은 score 값을 지정해주세요')

    def Linreg(self, X_train, X_test, y_train, pred=False, score=False):
        self.linr = LinearRegression()
        self.linr.fit(X_train, y_train)
        self.pred = self.linr.predict(X_test)
        self.score_linr = self.linr.score(X_train, y_train).round(4)
        if pred == True & score == True:
            return self.pred, self.score_linr
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_linr
        else :
            return print('pred 혹은 score 값을 지정해주세요')
    
    def Rid(self, X_train, X_test, y_train, pred=False, score=False):
        self.rid = Ridge()
        self.rid.fit(X_train, y_train)
        self.pred = self.rid.predict(X_test)
        self.score_rid = self.rid.score(X_train, y_train).round(4)
        if pred == True & score == True:
            return self.pred, self.score_rid
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_rid
        else :
            return print('pred 혹은 score 값을 지정해주세요')
    
    def Las(self, X_train, X_test, y_train, pred=False, score=False):
        self.las = Lasso()
        self.las.fit(X_train, y_train)
        self.pred = self.las.predict(X_test)
        self.score_las = self.las.score(X_train, y_train).round(4)
        if pred == True & score == True:
            return self.pred, self.score_las
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_las
        else :
            return print('pred 혹은 score 값을 지정해주세요')

    def Elastic(self, X_train, X_test, y_train, pred=False, score=False):
        self.elar = ElasticNet()
        self.elar.fit(X_train, y_train)
        self.pred = self.elar.predict(X_test)
        self.score_elar = self.elar.score(X_train, y_train).round(4)
        if pred == True & score == True:
            return self.pred, self.score_elar
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_elar
        else :
            return print('pred 혹은 score 값을 지정해주세요')

    def RFR(self, X_train, X_test, y_train, pred=False, score=False, feature_importances_=False, n_estimators=100, *, criterion='squared_error', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, ccp_alpha=0.0, max_samples=None):
        self.rfr = RandomForestRegressor(n_estimators=n_estimators,criterion=criterion, max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf, min_weight_fraction_leaf=min_weight_fraction_leaf, max_features=max_features, max_leaf_nodes=max_leaf_nodes, min_impurity_decrease=min_impurity_decrease, bootstrap=bootstrap, oob_score=oob_score, n_jobs=n_jobs, random_state=random_state, verbose=verbose, warm_start=warm_start, ccp_alpha=ccp_alpha, max_samples=max_samples)
        self.fit_rfr = self.rfr.fit(X_train, y_train)
        self.pred = self.rfr.predict(X_test)
        self.score_RFR = self.rfr.score(X_train, y_train).round(4)
        if pred == True & score == True:
            return self.pred, self.score_RFR
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_RFR
        elif feature_importances_ == True:
            return self.fit_rfr            
        else :
            return print('pred 혹은 score 값을 지정해주세요')

    
    def XGBR(self, X_train, X_test, y_train, pred=False, score=False, feature_importances_=False):
        self.xgbr = XGBRegressor()
        self.fit_xgbr = self.xgbr.fit(X_train, y_train)
        self.pred = self.xgbr.predict(X_test)
        self.score_XGBR = self.xgbr.score(X_train, y_train).round(4)
        if pred == True & score == True:
            return self.pred, self.score_XGBR
        elif pred == True:
            return self.pred
        elif score == True:
            return self.score_XGBR
        elif feature_importances_ == True:
            return self.fit_xgbr
        else :
            return print('pred 혹은 score 값을 지정해주세요')




