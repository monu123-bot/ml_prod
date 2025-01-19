from model.pipeline.preperation import prepare_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pickle as pk
from config.config import session
from loguru import logger


def build_model():
    logger.info("starting up model building pipeline")
    df = prepare_data()
    x, y = get_X_Y(df)
    x_train, x_test, y_train, y_test = split_train_test(x, y)
    rf = train_model(x_train, y_train)
    score = evaluate_model(rf, x_test, y_test)
    save_model(rf)
    pass


def get_X_Y(
    data,
    col_X=[
        "area",
        "constraction_year",
        "bedrooms",
        "garden",
        "balcony_yes",
        "parking_yes",
        "furnished_yes",
        "garage_yes",
        "storage_yes",
    ],
    col_y="rent",
):
    logger.info(f"defining X and Y variables. \nX vars: {col_X}\ny var: {col_y}")

    return data[col_X], data[col_y]


def split_train_test(x, y):
    logger.info("splitting data into train and test sets")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    return x_train, x_test, y_train, y_test


def train_model(x_train, y_train):
    logger.info("training a model with hyperparameters")
    grid_space = {"n_estimators": [100, 200, 300], "max_depth": [3, 6, 9, 12]}
    logger.debug(f"grid_space = {grid_space}")
    grid = GridSearchCV(
        RandomForestRegressor(), param_grid=grid_space, cv=5, scoring="r2"
    )
    mode_grid = grid.fit(x_train, y_train)

    return mode_grid.best_estimator_


def evaluate_model(model, x_test, y_test):
    logger.info(f"evaluating model performance. SCORE={model.score(x_test, y_test)}")
    return model.score(x_test, y_test)


def save_model(model):
    logger.info(
        f"saving a model to a directory: {session.model_path}/{session.model_name}"
    )
    pk.dump(model, open(f"{session.model_path}/{session.model_name}", "wb"))


build_model()
