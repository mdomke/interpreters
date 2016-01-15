import operator


class Node(object):
    pass


class BinOp(Node):

    _methods = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div
    }

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.method = self._methods[op]


class Number(Node):

    def __init__(self, number):
        self.value = number


class Visitor(object):

    def visit(self, node):
        if node is None:
            return
        method_name = 'visit_{}'.format(node.__class__.__name__)
        method = getattr(self, method_name, self._default)
        return method(node)

    def _default(self, node):
        raise NotImplementedError('No method for node type %s' % node.__class__.__name__)
