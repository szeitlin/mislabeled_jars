__author__ = 'szeitlin'

##You have 3 jars that are all mislabeled.
##1 has PB beans, another has grape jelly,
## and a third has a mix (any ratio).
##How many beans do you have to pull out to
## fix the labels on the jars?
import random

class BeanJar(object):

    def __init__(self, slot = [], name = [""], beanlist = []):
        self.slots = slot
        self.name = name
        self.beans = beanlist

    def __str__(self):
        msg = str(self.name)
        return msg

    def mix_beans(self):
        self.PB = random.randrange(100)
        self.Jelly = 100 - self.PB
        self.mixed = range(self.PB, 100) + range(0,self.Jelly)
        random.shuffle(self.mixed)

    def sort_slots(self):
        self.slots = [1, 2, 3]
        random.shuffle(self.slots)
        print self.slots

    def fill_jar(self):
        for i in range(len(self.slots)):
            if self.slots[i] == 1:
                self.beans.append("PB")
            elif self.slots[i] == 2:
                self.beans.append(self.mixed)
            else:
                self.beans.append("Jelly")
        print self.beans

    def pick_beans(self):
        """ iterate over beans and identify what to put in namelist
                int or str -> str"""
        #for i in range(len(self.beans)):
        b = 0
        i = 0
        self.picks = []

        for i in self.slots:
            for i in self.beans:
                if type(self.beans[i][0]) == str:
                    self.picks.append(self.beans[i])
                    print self.picks
                    i += 1
                elif type(self.beans[i][b]) == int:
                    if self.beans[i][b] > self.PB:
                        self.picks.append("Jelly")
                        print self.picks
                        b += 1
                    else:
                        self.picks.append("PB")
                        print self.picks
                        b += 1


test = BeanJar()
test.mix_beans()
test.sort_slots()
test.fill_jar()
test.pick_beans()

