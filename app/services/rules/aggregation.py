class AggregationRuler(object):
    def __init__(self, prefix=''):
        self.prefix = prefix
        self.__output = {}

    def execute(self, options):
        res = getattr(self, options['typ'])(options)
        self.addFilter(field=res['field'], values=res['filter'])

    def out(self):
        return self.__output

    def addFilter(self, field, values):
        if (field):
            cstr = '%s%s' % (self.getPrefix(), field)
            self.__output[cstr] = values

    def getPrefix(self):
        if self.prefix and isinstance(self.prefix, str):
            return self.prefix + "."

        return ''

    def string(self, kw):
        filter = kw['filter']
        if (kw['comparer'] == 'contain'):
            filter = {'$regex': '%s' % kw['filter']}

        if (kw['comparer'] == 'not contain'):
            filter = {'$ne': kw['filter']}

        return {'field': kw['field'], 'filter': filter}

    def boolean(self, kw):
        filter = kw['filter']
        return {'field': kw['field'], 'filter': filter == 'true'}

    def select(self, kw):
        filter = kw['filter']
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

    def number(self, kw):
        return self.byNumber(kw, 'greater', 'less')

    def date(self, kw):
        return self.byNumber(kw, 'after', 'before')

    def byNumber(self, kw, after, before):
        filter = kw['filter']

        if (kw['comparer'] == after):
            filter = {'$gte': kw['filter']}

        if (kw['comparer'] == before):
            filter = {'$lte': kw['filter']}

        return {'field': kw['field'], 'filter': filter}
