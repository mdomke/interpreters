import re
import operator

INT, ADD, SUB, MUL, DIV, EOF = 'INT', 'ADD', 'SUB', 'MUL', 'DIV', 'EOF'


class Token(object):

    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return '<Token {0.type}={0.value}>'.format(self)

    def __repr__(self):
        return str(self)


class Interpreter(object):

    operators = {
        '+': (ADD, operator.add),
        '-': (SUB, operator.sub),
        '*': (MUL, operator.mul),
        '/': (DIV, operator.div),
    }

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def parse(self):
        left, op, right = None, None, None
        while True:
            if self.current_token and self.current_token.type == EOF:
                break
            if left is None:
                left = self.eat(INT, EOF)
            elif op is None:
                op = self.eat(ADD, SUB, MUL, DIV, EOF)
            elif right is None:
                right = self.eat(INT)
                left = Token(INT, op.value(left.value, right.value))
                op, right = None, None
        return left.value

    def eat(self, *token_types):
        self.current_token = self.get_next_token()
        if self.current_token.type not in token_types:
            self.error('Invalid token type {} (expect: {})'.format(
                self.current_token.type, token_types))
        return self.current_token

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            token = Token(EOF)
        else:
            token = self._match_int() or self._match_op()
        if not token:
            self.error('Failed to get next token')
        return token

    def _match_int(self):
        match = self._match(r'\d+')
        if match:
            return Token(INT, int(match.group(1)))

    def _match_op(self):
        token = None
        match = self._match(r'[-+*/]')
        if match:
            type, value = self.operators.get(match.group(1), (None, None))
            if type and value:
                token = Token(type, value)
        return token

    def _match(self, regexp):
        text = self.text[self.pos:]
        regexp = r'\s*({})\s*'.format(regexp)
        match = re.match(regexp, text)
        if match:
            self.pos += match.end()
            return match

    def error(self, message=None):
        raise Exception('Error parsing expression: {}.'.format(message))


if __name__ == '__main__':
    while True:
        try:
            text = raw_input('calc> ')
        except (EOFError, KeyboardInterrupt):
            break
        interpreter = Interpreter(text)
        result = interpreter.parse()
        if result is not None:
            print(result)
