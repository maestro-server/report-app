
class Ruler(object):
    __output = {}

    def exec(self, options):
        res = getattr(self, options['typ'])(options)
        self.addFilter(field=res['field'], values=res['filter'])

    def out(self):
        return self.__output

    def addFilter(self, field, values):
        if (values and field):
            self.__output[field] = values




    # Filters rules, using in getattr by exec function
    # ===================================================

    def string(self, kw):
        filter = kw['filter']

        if (kw['comparer'] == 'contain'):
            filter = {'$regex': '%s' % kw['filter']}

        if (kw['comparer'] == 'not contain'):
            filter = {'$ne': kw['filter']}

        return {'field': kw['field'], 'filter': filter}

    def number(self, kw):
        filter = kw['filter']

        if (kw['comparer'] == 'greater'):
            filter = {'$gte': kw['filter']}

        if (kw['comparer'] == 'less'):
            filter = {'$lte': kw['filter']}

        return {'field': kw['field'], 'filter': filter}

    def object(self, kw):
        field = '%s.%s' % (kw['field'], kw['subfield'])
        return {'field': field, 'filter': kw['subfilter']}

    def array(self, kw):
        field = kw['field']

        if field in self.__output:
            filter = self.__output[field]

        else:
            filter = {"$elemMatch": {}}

        filter["$elemMatch"].update({kw['subfield']: kw['subfilter']})

        return {'field': kw['field'], 'filter': filter}

    def date(self, kw):
        filter = kw['filter']

        if (kw['comparer'] == 'after'):
            filter = {'$gte': kw['filter']}

        if (kw['comparer'] == 'before'):
            filter = {'$lte': kw['filter']}

        return {'field': kw['field'], 'filter': filter}
