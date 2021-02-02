import json

class lock():
    def __init__(self):
        self._UserDetails = {}
        self._UserRepo = {}
        self.username = ""
        try:
            with open("userdetail.json") as obj:
                 self._UserDetails = json.load(obj)
        except FileNotFoundError:
            with open("userdetail.json","w") as obj:
                json.dump({}, obj)
            with open("userdetail.json") as obj:
                 self._UserDetails = json.load(obj)
        try:
            with open("userepo.json") as obj:
                 self._UserRepo = json.load(obj)
        except FileNotFoundError:
            with open("userepo.json","w") as obj:
                json.dump({}, obj)
            with open("userepo.json") as obj:
                 self._UserRepo = json.load(obj)

    def sign_in(self, username, password):
        if (username, password) in self._UserDetails.items():
            self.username = username
            return True
        else:
            return False

    def sign_up(self, username, password, password1):
        if password == password1:
            with open('userdetail.json', "w") as obj:
                self._UserDetails[username]=password
                json.dump(self._UserDetails, obj)
            with open("userepo.json", "w") as obj:
                self._UserRepo[username]={}
                json.dump(self._UserRepo, obj)
            return True
        else:
            return False
    def addNewAccount(self, accountName, username, password):
        if (accountName == "" or username == "" or password == ""): raise TypeError
        temp = self._UserRepo[self.username]
        #print(temp)
        temp[accountName]=[username, password]
        #print(temp)
        self._UserRepo[self.username] = temp
        with open("userepo.json","w") as obj:
                json.dump(self._UserRepo, obj)
    def viewAccount(self, accountName):
        temp = self._UserRepo[self.username]
        if accountName in temp.keys():
            return accountName, temp[accountName]
        else:
            raise NameError

