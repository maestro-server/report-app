
from pydash import has

def validate(item):
    return item and len(item) > 0 and has(item, '_id')