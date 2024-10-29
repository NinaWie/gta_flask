import pandas as pd
import os
import json
from sqlalchemy import create_engine
import psycopg2

DBLOGIN_FILE = os.path.join("db_login.json")


def get_mean_value_from_table(col_name):
    """Compute mean_value of column <col_name>"""

    # TODO: load dblogin from json file

    # TODO: initialize database connection

    # TODO: Read column from database

    # TODO: compute mean
    pass  # delete this
