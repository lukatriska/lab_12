from multiset.multisetll import Multiset

class BigInteger:

    def __init__(self, initValue=0):
        self.initValue = initValue
        self.intSet = Multiset()
        for digit in range(initValue):
            self.intSet.add(digit)

    def toString(self):
        return str(self.initValue)

    def comparable(self, other):
        return self.initValue == other

    def arithmetic(self, rhsInt):
        return self.initValue + rhsInt

    def bitwise_ops(self, rhsInt):
        pass
