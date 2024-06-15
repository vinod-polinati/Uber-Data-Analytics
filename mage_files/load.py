from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.

    This function exports data to a BigQuery warehouse using the Mage AI framework.
    It relies on the 'mage_ai.io.bigquery.BigQuery' class for the export operation.

    Args:
        data (dict): A dictionary containing data frames to be exported. The keys represent table names,
                     and the values are pandas DataFrame objects containing the corresponding data.
        **kwargs: Additional keyword arguments (not used in this function).

    Returns:
        None

    Raises:
        None

    Example:
        data = {
            'table1': DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']}),
            'table2': DataFrame({'col3': [4, 5, 6], 'col4': ['D', 'E', 'F']})
        }
        export_data_to_big_query(data)
    """
    # Path to the 'io_config.yaml' file
    config_path = path.join(get_repo_path(), 'io_config.yaml')

    # Configuration profile to use
    config_profile = 'default'

    # Export each data frame to BigQuery
    for key, value in data.items():
        # Construct the table_id using the key
        table_id = 'fabled-essence-389307.uber_data_engineering_yt.{}'.format(key)

        # Export the data frame to BigQuery
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists='replace'  # Specify resolution policy if table name already exists
        )