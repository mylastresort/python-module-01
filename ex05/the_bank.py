class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def is_corrupted(self):
        return len(self.__dict__) % 2 == 1 \
            or any([k.startswith('b') for k in self.__dict__.keys()]) \
            or not any([k.startswith('zip')
                        | k.startswith('addr') for k in self.__dict__.keys()])\
            or not hasattr(self, 'name') or not hasattr(self, 'id') \
            or not hasattr(self, 'value') or type(self.name) is not str \
            or type(self.id) is not int or type(self.value) not in (int, float)


class Bank(object):
    def __init__(self):
        self.accounts: [Account] = []

    def add(self, new_account):
        if not isinstance(new_account, Account) or \
                any([acc.name == new_account.name for acc in self.accounts]):
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin: str, dest: str, amount: float):
        if type(origin) is not str or type(dest) is not str \
                or type(amount) not in (float, int) or amount < 0:
            return False
        origin_acc: Account = None
        dest_acc: Account = None
        for ac in self.accounts:
            if ac.name == origin:
                origin_acc = ac
            if ac.name == dest:
                dest_acc = ac
            if origin_acc and dest_acc:
                break
        if not origin_acc or not dest_acc or origin_acc.is_corrupted() \
                or dest_acc.is_corrupted() or origin.value < amount:
            return False
        dest_acc.transfer(amount)
        origin_acc.value -= amount
        return True

    def fix_account(self, name):
        if type(name) is not str:
            return False
        acc: Account = None
        for ac in self.accounts:
            if ac.name == name:
                acc = ac
            if acc:
                break
        if not acc:
            return False
        if not any([k.startswith('zip')
                    | k.startswith('addr') for k in self.__dict__.keys()]):
            acc.zip = ''
        for key in filter(lambda k: k.startswith('b'), self.__dict__.keys()):
            self.__delattr__(key)
        if not hasattr(self, 'name'):
            self.name = ''
        if not hasattr(self, 'value'):
            self.value = 0
        if not hasattr(self, 'id'):
            self.id = ''
        if type(self.name) is not str:
            self.name = ''
        if type(self.id) is not str:
            self.id = ''
        if type(self.value) not in (int, float):
            self.value = 0
        return True
