from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def train_model(X, y):
    model = RandomForestRegressor(
        n_estimators=200,      # more trees = better learning
        max_depth=10,          # avoid overfitting
        random_state=42
    )
    model.fit(X, y)
    return model

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    score = r2_score(y, predictions)
    return score

def get_feature_importance(model, feature_names):
    importance = model.feature_importances_
    return feature_names, importance