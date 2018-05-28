from pydash import py_


class Inventory:
    def __init__(self, item):
        self.__result = ''
        self.__chain = py_(item)
        self._id = self.makeId()

    def maker(self):
        self.makeHostname()
        self.makeHost()
        self.makeUser()
        self.makeKeyFile()
        self.makePort()
        return self

    def output(self):
        return self.__result

    def makeId(self):
        options = ['servers._id', '_id']
        return self.chainVars(options)

    def getId(self):
        return self._id

    def makeHostname(self):
        options = ['hostname', 'servers.hostname']
        self.factoryAnsibleVars(options, '', '', '')

    def makeHost(self):
        options = ['dns_internal', 'ipv4_private', 'ipv4_public', 'hostname', 'servers.ipv4_private',
                   'servers.ipv4_public', 'servers.hostname']
        self.factoryAnsibleVars(options, 'ansible_host')

    def makePort(self):
        options = ['ansible.port']
        self.factoryAnsibleVars(options, 'ansible_port')

    def makeUser(self):
        options = ['ansible.user', 'auth[0].username']
        self.factoryAnsibleVars(options, 'ansible_user')

    def makeKeyFile(self):
        options = ['ansible.key']
        self.factoryAnsibleVars(options, 'ansible_ssh_private_key_file')

    def factoryAnsibleVars(self, options, var, separator='=', prefix=' '):
        rs = self.chainVars(options)
        if rs:
            self.__result += '%s%s%s%s' % (prefix, var, separator, rs)
            return self

    def chainVars(self, options):
        for item in options:
            rs = self.__chain.get(item).value()
            if rs:
                return rs
