import random
from nltk.corpus import words


class absgeneratorclass:
    def generator(self):
        print("error generator is not defined in the related class")


class Random_Password(absgeneratorclass):
    def __init__(self, length, state):
        self.password = ""
        self.length = length
        self.state = state

    def generator(self):
        if self.state == "both":
            for i in range(0, self.length):
                self.password += chr(random.randint(33, 126))
        elif self.state == "numbers":
            for i in range(0, self.length):
                self.password += str(random.randint(0, 9))
        elif self.state == "symbols":
            while self.length > len(self.password):
                temp = str(chr(random.randint(33, 126)))
                if not temp.isdigit():
                    self.password += temp


class Memorable_Password(absgeneratorclass):
    wordlist = words.words()

    def __init__(self, length, seperator, capitalize):
        self.password = ""
        self.length = length
        self.seperator = seperator
        self.capitalize = capitalize

    def generator(self):
        randomselectedwords = random.sample(self.wordlist, self.length)
        self.password = self.seperator.join(randomselectedwords)
        if self.capitalize:
            self.password = self.password.title()

        pass


class Pin_password(absgeneratorclass):
    def __init__(self, length):
        self.password = ""
        self.length = length

    def generator(self):
        for i in range(self.length):
            temp = str(random.randint(0, 9))
            self.password += temp


while True:
    input1 = input(
        "what type of password do you want ?  (help:Random,Memorable,PIN)    ").lower()
    if input1 == "random":
        random1 = input("do you want numbers,symbols or both ? ").lower()
        random2 = int(input("whats the length of the password? "))
        q = Random_Password(random2, random1)
        q.generator()
        print(q.password)
        break
    elif input1 == "memorable":
        mem1 = int(input("whats the length? "))
        mem2 = input("whats the seperator ? ")
        mem3 = input("do you want them capitalized? ").lower()
        capflag = True if mem3 == "yes" else False
        m = Memorable_Password(mem1, mem2, capflag)
        m.generator()
        print(m.password)
        break
    elif input1 == "pin":
        pin1 = int(input("whats the length of the pin ? "))
        r = Pin_password(pin1)
        r.generator()
        print(r.password)
        break
    else:
        print("invalid input try again")

