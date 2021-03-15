
def validate_insert(value):
    if isinstance(value, dict):
        if "_id" not in value:
            value.update({"_id": None}) # TODO add id func