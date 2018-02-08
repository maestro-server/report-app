
def getRules(owner_id, active=False):
    obj = {'roles._id': owner_id}
    if active:
        obj.update({'active': True})

    return obj
