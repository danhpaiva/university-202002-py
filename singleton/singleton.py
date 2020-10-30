class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GerenciadorConfiguracao(metaclass=SingletonMeta):
    def __init__(self):
        self._serverName = ''
        self._serverPriority = 1
        self._serverActive = False

    @ property
    def serverName(self):
        return self._serverName

    @ serverName.setter
    def serverName(self, serverName):
        self._serverName = serverName

    @ property
    def serverPriority(self):
        return self._serverPriority

    @ serverPriority.setter
    def serverPriority(self, serverPriority):
        self._serverPriority = serverPriority

    @ property
    def serverActive(self):
        return self._serverActive

    @ serverActive.setter
    def serverActive(self, serverActive):
        self._serverActive = serverActive

    def __str__(self):
        return "Name: "+str(self._serverName) + "\nPrio: "+str(self._serverPriority) + "\nActv: "+str(self._serverActive)+"\n"


def my_other_method():
    conf = GerenciadorConfiguracao()
    conf.serverName = "other"
    conf.serverPriority = 5
    conf.serverActive = False
    print(conf)


conf = GerenciadorConfiguracao()
conf.serverName = "main"
conf.serverPriority = 10
conf.serverActive = True

print(conf)
#
# ...
#
my_other_method()
#
# ...
#
conf.serverActive = True
print(conf)
