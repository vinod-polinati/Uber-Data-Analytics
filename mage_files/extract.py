import io
import pandas as pd
import requests

# Check if 'data_loader' is not defined in global namespace and import it if necessary
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

# Check if 'test' is not defined in global namespace and import it if necessary
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from an API.

    This function sends a GET request to a specified URL and retrieves CSV data.
    The data is then converted into a Pandas DataFrame and returned.

    Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    url = 'https://storage.googleapis.com/uber-data-engineering-proj-etl/uber_data.csv'
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of a block.

    This function checks if the output is not None and raises an assertion error if it is.

    Args:
        output: The output to be tested.
        *args: Additional arguments (not used in this function).

    Raises:
        AssertionError: If the output is None.
    """
    assert output is not None, 'The output is undefined'