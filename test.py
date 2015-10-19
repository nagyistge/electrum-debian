class bibi:
    def f(self, receiving=False):
        return "z"

d = {u'receiving':True}

b = bibi()

print b.f, d
print b.f(**d)
