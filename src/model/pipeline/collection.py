import pandas as pd
from config.config import session
from loguru import logger

from config.config import engine
from database.db_model import RentApartments
from sqlalchemy import select

# def load_data(path=f'{session.data_file_path}/{session.data_file_name}'):
#     logger.info(f"loading csv file at path {path}")
#     return pd.read_csv(path)

# df = load_data()


def load_data_from_db():
    logger.info('extracting data from database table')
    query = select(RentApartments)
    return pd.read_sql(query,engine)

