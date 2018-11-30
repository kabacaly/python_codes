def find_best_weight(preds, target):
    from scipy.optimize import minimize
    def _validate_func(weights):
        
        final_prediction = 0
        for weight, prediction in zip(weights, preds):
                final_prediction += weight * prediction
        return np.sqrt(mean_squared_error(final_prediction, target))

    starting_values = [0.5]*len(preds)
    cons = ({'type':'eq','fun':lambda w: 1-sum(w)})
    bounds = [(0, 1)] * len(preds)
    
    res = minimize(_validate_func, starting_values, method='Nelder-Mead', bounds=bounds, constraints=cons)
    
    print('Ensemble Score: {best_score}'.format(best_score=(1-res['fun'])))
    print('Best Weights: {weights}'.format(weights=res['x']))
    
    return res
