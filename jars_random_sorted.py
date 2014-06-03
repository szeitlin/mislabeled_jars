__author__ = 'szeitlin'

##You have 3 jars that are all mislabeled.
##1 has PB beans, another has grape jelly,
## and a third has a mix (any ratio).
##How many beans do you have to pull out to
## fix the labels on the jars?
import random

class BeanJar(object):

    def __init__(self, jars = ["PB", "Jelly", "PBJ"]):
        #self.name = name
        self.jars = jars

    def sort_jars(self):
        self.jars = [["PB"], ["Jelly"], ["PBJ"]]
        random.shuffle(self.jars)
        print self.jars

    def mix_beans(self):
        self.PB = random.randrange(100)
        self.Jelly = 100 - self.PB
        self.layers = range(self.PB, 100) + range(0,self.Jelly)
        random.shuffle(self.layers)

    def fill_jars(self):
        for i in range(len(self.jars)):
            # if self.jars[i] == "PB" or "Jelly": #fix this
            #     continue
            if self.jars[i] == ["PBJ"]:
                self.jars[i] = self.layers
        #print self.jars

    def guess_beans(self):
        print "picking first bean"
        i = 0
        #self.bean = [] #numbers
        self.labels = [] #strings
        for i in range(5):
            bean = random.choice(self.jars) #picks a bean from a jar
            print "this bean is " + str(bean)
            if type(bean) == str:
                print bean
                self.labels.append(bean)
            # elif type(bean) == int:
            #     if bean > self.PB:
            #         self.labels.append("Jelly")
            #     else:
            #         self.labels.append("PB")
        print self.labels

    def check_jars(self):
        i = 0
        while self.labels[i] == self.labels[i+1]:
            guess_beans()




# One = BeanJar(30)
# One.sort_jars()
# One.mix_beans()
# print One
# One.get_name()
Mixed = BeanJar()
Mixed.mix_beans()
print Mixed
Mixed.sort_jars()
Mixed.fill_jars()

Mixed.guess_beans()

