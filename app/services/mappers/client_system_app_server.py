def mapperI():
    query = {
        "clients": {},
        "systems": {
            "localField": "{prev}_id",
            "foreignField": "clients._id",
            "unwind": {"path": "$systems", "preserveNullAndEmptyArrays": True}
        },
        "applications": {
            "localField": "{prev}_id",
            "foreignField": "system._id",
            "unwind": {"path": '$applications', "preserveNullAndEmptyArrays": True}
        },
        "servers": {
            "localField": "{prev}_id",
            "foreignField": "applications._id",
            "unwind": {"path": "$servers", "preserveNullAndEmptyArrays": True}
        }
    }
    return query
