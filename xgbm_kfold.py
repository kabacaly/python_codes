from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import xgboost as xgb

X = train_model.drop('target', axis=1, inplace=False)
y = train_model['target']

kf = KFold(n_splits=11, shuffle=True, random_state=87)

#xgb = XGBRegressor(n_jobs=-1, max_depth=6, n_estimators=200, colsample_bytree=0.65, min_child_weight=12
#                  ,reg_alpha=0.65)
xgb_params = {'n_jobs':-1, 'max_depth':5, 'n_estimators':800
             ,'min_child_weight':12
              
             }

oof_xgb = np.zeros(len(X))
preds_xgb = np.zeros(len(test_model))
train_data_ = np.zeros(len(X))


for i,(train_index, val_index) in enumerate(kf.split(X)):    
    #x_trk, x_tek = X.iloc[train_index], X.iloc[test_index]
    #y_trk, y_tek = y[train_index], y[test_index]
    train_data = xgb.DMatrix(data=X.iloc[train_index], label=y.iloc[train_index])
    val_data = xgb.DMatrix(data=X.iloc[val_index], label=y.iloc[val_index])
    watchlist = [(train_data, 'train'), (val_data,'valid')]
    print('xgb '+ str(i) + '-'*50)
    model = xgb.train(xgb_params, dtrain=train_data , num_boost_round=250, evals=watchlist, early_stopping_rounds=50
                     ,verbose_eval=100)
    oof_xgb[val_index] = model.predict(xgb.DMatrix(X.iloc[val_index]), ntree_limit=model.best_ntree_limit + 50)
    preds_xgb += model.predict(xgb.DMatrix(test_model), ntree_limit=model.best_ntree_limit + 50)/kf.n_splits
        
print("{:.3f}".format(np.sqrt(mean_squared_error(oof_xgb, y))))   
