from commons import commons
from configuration.read_config import get_electric_vehicles_configuration, get_mongodb_configuration
from electric_vehicles import get_columns, map_column_and_values
from etl.electric_vehicles import get_values


def migrate_data_to_mongodb(url, connection_string, database, collection):
    # fetch data
    semi_structured_data = commons.fetch_data(url)

    # fetch columns
    columns = get_columns(semi_structured_data)
    # print(columns)

    # fetch values
    values = get_values(semi_structured_data)
    # print(values)

    # generate records to insert
    records = [map_column_and_values(columns, value_list) for value_list in values]
    # print(records)

    # # connecting to mongodb
    commons.connect_to_mongodb(connection_string)

    client = commons.get_client()
    database = commons.connect_to_database(client, database)
    collection = commons.connect_to_collection(database, collection)
    commons.insert_data_into_mongodb(collection, records)

    # closing mongodb connection
    commons.close_mongodb_connection()


if __name__ == "__main__":
    ele_veh_conf = get_electric_vehicles_configuration()
    mongo_conf = get_mongodb_configuration()

    migrate_data_to_mongodb(ele_veh_conf.get('URL'), mongo_conf.get('CONNECTION_STRING'), mongo_conf.get('DATABASE'),
                            ele_veh_conf.get('COLLECTION'))
