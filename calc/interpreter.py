from ast import Visitor


class Calculator(Visitor):

    def __init__(self, ast):
        self.ast = ast

    def __call__(self):
        return self.visit(self.ast)

    def visit_BinOp(self, node):
        return node.method(self.visit(node.left), self.visit(node.right))

    def visit_Number(self, node):
        return node.value
