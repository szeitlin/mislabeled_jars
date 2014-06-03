__author__ = 'szeitlin'

##You have 3 jars that are all mislabeled.
##1 has PB beans, another has grape jelly,
## and a third has a mix (any ratio).
##How many beans do you have to pull out to
## fix the labels on the jars?

from random import randrange

## create names & labels
jars = ["PB", "J", "PBJ"]
print jars

## create random number generator to put mixed beans in PBJ jar
PB = randrange (100)
J = 100 - PB      #let's just say some are PB, the rest are J

## create random sort to assign identities to jars
random.shuffle(jars)
print jars

## create bean-picker to check
print "picking first bean"
bean = random.sample(range(1, PB))

for bean in range(6):

    if bean < PB:
        print "this is a PB bean"
    elif bean > PB:
        print "this is a Jelly bean"


    ###need to hook up beans with jars somehow & check sequential beans from the same jar

for i in mix:

    if jar[0] = "PB":
        print "this is the PB jar"
    elif jar[0] = "J":
        print "this is the J jar"
    elif jar[0] = "PBJ":
        if bean < mix:
            print


## print out the answer & reset



