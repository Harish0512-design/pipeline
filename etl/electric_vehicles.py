def get_columns(data: dict):
    column_list = data.get("meta").get("view").get("columns")
    filtered_column_list = [column.get("name", "Null") for column in column_list if
                            'hidden' not in column.get('flags', "Null") and ':@computed_region' not in column.get(
                                'fieldName', "Null")]
    return filtered_column_list


def get_values(data: dict):
    values_list = data.get("data")
    filtered_values_list = [values[8:26] for values in values_list]
    return filtered_values_list


def map_column_and_values(column_list, value_list):
    record = {}
    for column, value in zip(column_list, value_list):
        record[column] = value
    return record

# print(get_columns())
