
def getRules(owner_id, prefix=''):
    if not isinstance(prefix, str):
        prefix = ''
      
    if prefix:
        prefix = prefix+"."

    key = '%sroles._id' % prefix
    obj = {key: owner_id}
    return obj
