__author__ = 'szeitlin'

##You have 3 jars that are all mislabeled.
##1 has PB beans, another has grape jelly,
## and a third has a mix (any ratio).
##How many beans do you have to pull out to
## fix the labels on the jars?
import random

class BeanJar(object):

    def __init__(self, jars = ["PB", "J", "PBJ"]):
        #self.name = name
        self.jars = jars
        # self.PB = PB
        # self.Jelly = Jelly

    def __str__(self):
        msg = str(self.PB) + " PB " + "and " + str(self.Jelly) + " Jelly"
        return msg

    def sort_jars(self):
        self.jars = ["PB", "Jelly", "PBJ"]
        random.shuffle(self.jars)

    def mix_beans(self):
        self.PB = random.randrange(100)
        self.Jelly = 100 - self.PB
        self.layers = range(self.PB, 100) + range(0,self.Jelly)
        print self.layers
        random.shuffle(self.layers)
        print self.layers

    def get_name(self):
        i = 0
        for i in range(len(self.jars)):
            self.name = self.jars[i]
            print self.name + " jar"

    def guess_beans(self):
        print "picking first bean"
        i = 0
        beanlist = []
        for i in range(len(self.jars)):
            if self.jars[i] == "PB":
                print "PB"
            elif self.jars[i] == "Jelly":
                print "Jelly"
            elif self.jars[i] == "PBJ":
                self.bean = random.sample(xrange(100), 1)
                #print "this bean is number " + str(self.bean)
                if self.bean > self.PB:
                    print "Jelly"
                else:
                    print "PB"
            beanlist.append(self.jars[i])
        print beanlist

    def check_jars(self):
        while self.jars[i] == self.jars[i+1]:
            guess_beans()



# One = BeanJar(30)
# One.sort_jars()
# One.mix_beans()
# print One
# One.get_name()
Mixed = BeanJar()
Mixed.mix_beans()
print Mixed
Mixed.get_name()
Mixed.guess_beans()
Mixed.check_jars()

