__author__ = 'szeitlin'

class BeanJar(object):

    def __init__(self, slot = [], name = [""], beanlist = []):
        self.slots = slot
        self.name = name
        self.beans = beanlist
        self.picks = []

    def pick_beans(self):
        """ iterate over beans and identify what to put in namelist
                int or str -> str"""
        b = 0
        i = 0
        foo = True

        self.beans = [[96, 1, 0, 98, 3, 99, 97, 95, 4, 2], 'PB', 'Jelly']

        while foo:

            for i in range(len(self.beans)):
                if type(self.beans[i]) == str:
                    self.picks.append(self.beans[i])
                elif type(self.beans[i][b]) == int:
                    lastbean = None
                    while b < len(self.beans[i]):
                        if self.beans[i][b] > 50:
                            if lastbean == "PB":
                                break
                            self.picks.append("Jelly")
                            b += 1
                            lastbean = "Jelly"
                        else:
                            if lastbean == "Jelly":
                                break
                            self.picks.append("PB")
                            b += 1
                            lastbean = "PB"
                    self.picks.append("PBJ")
                    if b >= len(self.beans[i]):
                        foo = False

        print self.picks

test = BeanJar()
test.pick_beans()

