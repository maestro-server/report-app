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
            "unwind": {"path": '$applications', "includeArrayIndex": 'servers', "preserveNullAndEmptyArrays": True}
        },
        "servers": {
            "localField": "{prev}servers",
            "foreignField": "_id",
            "unwind": {"path": "$servers", "preserveNullAndEmptyArrays": True}
        }
    }
    return query
