
from pydash import get, py_

class Inventory:
    def __init__(self, item):
        self.__result = ''
        self.__chain = py_(item)
        
    def maker(self):
        self.makeHost()
        self.makeUser()
        self.makeKeyFile()
        self.makePort()
        return self

    def output(self):
        return self.__result

    def makeHost(self):
        options = ['dns_internal', 'ipv4_private', 'ipv4_public', 'hostname']
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
        
    def factoryAnsibleVars(self, options, var):
        for item in options:
            rs = self.__chain.get(item).value()
            if rs:
                self.__result += ' %s=%s' % (var, rs)
                return self