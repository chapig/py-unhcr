import pandas as pd


# Decorator to return data as a DataFrame
def dataframe(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if response is not None:
            return pd.DataFrame(response)
        return None

    return wrapper

