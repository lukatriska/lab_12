# Implementation of the Polynomial ADT using a sorted linked list.

class Polynomial :
    # Create a new polynomial object.
    def __init__(self, degree = None, coefficient = None):
        if degree is None :
            self._polyHead = None
        else :
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None :
            return -1
        else :
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree > degree :
            curNode = curNode.next

        if curNode is None or curNode.degree != degree :
            return 0.0
        else :
            return curNode.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None :
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    # Polynomial addition: newPoly = self + rhsPoly.
    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, "Addition only allowed on non -empty polynomials."
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        # Add corresponding terms until one list is empty.
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        # If self list contains more terms append them.
        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        # Or if rhs contains more terms append them.
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    # Polynomial subtraction: newPoly = self - rhsPoly.
    def __sub__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, "Addition only allowed on non -empty polynomials."
        newPoly = Polynomial()
        nodeSelf = self._polyHead
        nodeRhs = rhsPoly._polyHead

        while nodeSelf is not None and nodeRhs is not None:
            if nodeSelf.degree > nodeRhs.degree:
                degree = nodeSelf.degree
                value = nodeSelf.coefficient
                nodeSelf = nodeSelf.next
            elif nodeSelf.degree < nodeRhs.degree:
                degree = nodeRhs.degree
                value = nodeRhs.coefficient
                nodeRhs = nodeRhs.next
            else:
                degree = nodeSelf.degree
                value = nodeSelf.coefficient - nodeRhs.coefficient
                nodeSelf = nodeSelf.next
                nodeRhs = nodeRhs.next
            newPoly._appendTerm(degree, value)

        while nodeSelf is not None:
            newPoly._appendTerm(nodeSelf.degree, nodeSelf.coefficient)
            nodeSelf = nodeSelf.next

        while nodeRhs is not None:
            newPoly._appendTerm(nodeRhs.degree, nodeRhs.coefficient)
            nodeRhs = nodeRhs.next

        return newPoly

    # Polynomial multiplication: newPoly = self * rhsPoly.
    def __mul__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, "Multiplication only allowed on non -empty polynomials."
        nodeSelf = self._polyHead
        newPoly = rhsPoly.termMul(nodeSelf)

        nodeSelf = nodeSelf.next
        while nodeSelf is not None:
            tempPoly = rhsPoly.termMul(nodeSelf)
            newPoly = newPoly + tempPoly
            nodeSelf = nodeSelf.next

        return newPoly

    # This a helper function for the function above.
    def termMul(self, node):
        newPoly = Polynomial()
        curr = self._polyHead
        while curr is not None:
            tempDegree = curr.degree + node.degree
            tempValue = curr.coefficient * node.coefficient
            newPoly._appendTerm(tempDegree, tempValue)
            curr = curr.next
        return newPoly

    def simple_add(self, rhsPoly):
        newPoly = Polynomial()
        if self.degree() > rhsPoly.degree():
            maxDegree = self.degree()
        else:
            maxDegree = rhsPoly.degree()

        i = maxDegree
        while i >= 0:
            value = self[i] + rhsPoly[i]
            newPoly._appendTerm(i, value)
            i += 1
        return newPoly

    # Helper method for appending terms to the polynomial.
    def _appendTerm(self, degree, coefficient) :
        if coefficient != 0.0 :
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None :
                self._polyHead = newTerm
            else :
                self._polyTail.next = newTerm
            self._polyTail = newTerm

    def __str__(self):
        curHead = self._polyHead
        stri = ''
        while curHead is not None:
            if round(curHead.coefficient) == curHead.coefficient:
                stri += str(int(curHead.coefficient))
            else:
                stri += str(curHead.coefficient)
            stri += 'x^'
            if round(curHead.degree) == curHead.degree:
                stri += str(int(curHead.degree))
            else:
                stri += str(curHead.degree)
            stri += ' + '
            curHead = curHead.next
        if stri[-2:] == '+ ':
            stri = stri[:-2]
        return stri


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
