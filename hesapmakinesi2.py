class hesapm(object):
    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def topla(self):
        return self.value1 + self.value2

    def carp(self):
        return self.value1 * self.value2

v1 = int(input("sayı giriniz: "))
v2 = int(input("sayı giriniz: "))
c1 = hesapm(v1, v2)
topla_result = c1.topla()
carp_result = c1.carp()

print("topla {}, çarp {}".format(topla_result, carp_result))












