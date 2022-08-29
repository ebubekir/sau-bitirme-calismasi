import os
import pandas as pd


class DataManager:

    @staticmethod
    def read_data(file_name: str, column_list: list = None) -> pd.DataFrame:
        try:
            path = f"{os.getcwd()}/app/data/{file_name}.csv"
            if not os.path.exists(path):
                raise FileNotFoundError("File not found.")
            df = pd.read_csv(f"{os.getcwd()}/app/data/{file_name}.csv")
            if column_list:
                df = df[column_list]
            return df
        except Exception as e:
            raise e
