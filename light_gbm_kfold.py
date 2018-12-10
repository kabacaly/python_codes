from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import lightgbm as lgb

kf = KFold(n_splits=7, shuffle=False, random_state=47)

lgb_params = {'n_jobs':-1, 'num_leaves':29, 'colsample_bytree':1
             ,'min_child_weight':350, 'metric':'rmse'
             }

oof_lgb = np.zeros(len(X))
preds_lgb = np.zeros(len(test_model))

for i,(train_index, val_index) in enumerate(kf.split(X)):    
    train_data = lgb.Dataset(data=X.iloc[train_index], label=y.iloc[train_index])    
    val_data = lgb.Dataset(data=X.iloc[val_index], label=y.iloc[val_index])
    watchlist = [(train_data, 'train'), (val_data,'valid')]
    print('lgb '+ str(i) + '-'*50)
    model = lgb.train(lgb_params,train_set=train_data, num_boost_round=500, valid_sets=[train_data,val_data]
                     ,early_stopping_rounds=50, verbose_eval=250)
    oof_lgb[val_index] = model.predict(X.iloc[val_index], num_iteration=model.best_iteration)
    preds_lgb += model.predict(test_model, num_iteration=model.best_iteration)/kf.n_splits
  
print("{:.3f}".format(np.sqrt(mean_squared_error(oof_lgb, y))))    
