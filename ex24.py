print "Let's practice everything."
print 'You\'d need to konw \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "_________________"
print poem
print "_________________"


five = 10 - 2 + 3 - 6
print "This should be five:%s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates =jars / 100
    return jelly_beans,jars,crates


starte_point = 10000
beans, jars, crates = secret_formula(starte_point)

print "With a strating point of:%d" % starte_point
print "We'd have %d beans, %d jars, and %d crates." %(beans, jars, crates)

starte_point = starte_point / 10
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(starte_point)
