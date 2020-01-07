# -*- coding: utf-8 -*-
"""
@brief : 配置文件，主要用于配置机器学习模型使用哪种特征和机器学习算法
@How to use : 修改features_path用于选择使用哪种特征；修改clf_name用于选择使用哪种学习算法；可在clfs_dict中对学习算法的超参数进行修改；
@author: Jian
"""
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
import xgboost as xgb
import lightgbm as lgb

"""是否开启验证集模式"""
status_vali = True

"""特征存储的路径"""
#features_path = '../features/data_ensemble_spar.pkl'

"""修改clf_name可对学习算法进行选择；修改base_clf改变集成学习的基分类器"""
clf_name = 'lr'

base_clf = LinearSVC()


clfs = {
    'lr': LogisticRegression(C=9, penalty='l2'),
    'svm': LinearSVC(penalty='l2', dual=True, random_state=1),
    'bagging': BaggingClassifier(base_estimator=base_clf, n_estimators=60, max_samples=1.0, max_features=1.0, random_state=1,
                        n_jobs=1, verbose=1),
    'rf': RandomForestClassifier(n_estimators=100, criterion='gini'),
    'adaboost': AdaBoostClassifier(base_estimator=base_clf, n_estimators=50),
    'gbdt': GradientBoostingClassifier(),
    'xgb': xgb.XGBClassifier(max_depth=6, learning_rate=0.1, n_estimators=100, silent=True, objective='multi:softmax',
                        nthread=1, gamma=0, min_child_weight=1, max_delta_step=0, subsample=1, colsample_bytree=1,
                        colsample_bylevel=1, reg_alpha=0, reg_lambda=1, scale_pos_weight=1, base_score=0.5, seed=0,
                        missing=None),
    
    #'lgb': lgb.LGBMClassifier(boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=1000,
    #                          max_bin=255, subsample_for_bin=200000, objective=None, min_split_gain=0.0, min_child_weight=0.001,
    #                          min_child_samples=20, subsample=1.0, subsample_freq=1, colsample_bytree=1.0, reg_alpha=0.0,
    #                          reg_lambda=0.5, random_state=None, n_jobs=-1, silent=True)
    
    'lgb': lgb.LGBMClassifier(boosting='gbdt', num_classes=3, num_leaves=2**5, learning_rate=0.1, n_estimators=1000, subsample=0.9, colsample_bytree=0.8, random_state=3)
}
clf = clfs[clf_name]
