import cli
from ast import BinOp, Number


NUM, ADD, SUB, MUL, DIV, LPAREN, RPAREN, EOF = (
    'NUM', 'ADD', 'SUB', 'MUL', 'DIV', 'LPAREN', 'RPAREN', 'EOF'
)


class Token(object):

    def __init__(self, type, value=None):
        self.type = type
        self.value = value or type

    def __str__(self):
        return '<Token {0.type}={0.value}>'.format(self)

    def __repr__(self):
        return str(self)


class Lexer(object):

    literals = {
        '+': Token(ADD, '+'),
        '-': Token(SUB, '-'),
        '*': Token(MUL, '*'),
        '/': Token(DIV, '/'),
        '(': Token(LPAREN, '('),
        ')': Token(RPAREN, ')'),
    }

    def __init__(self, text=None, ignore=None):
        self.pos = 0
        self.text = text or ''
        self.ignore = ignore or [' ', '\t']
        self.current_char = None

    def input(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise ValueError('Invalid character "%s"' % self.current_char)

    def get_next_token(self):

        while self.current_char is not None:

            if self.current_char in self.ignore:
                self.skip()
                continue

            if self.current_char.isdigit():
                token = Token(NUM, self.number())
            elif self.current_char in self.literals:
                token = self.literals[self.current_char]
                self.step()
            else:
                self.error()
            break
        else:
            token = Token(EOF)

        return token

    def number(self):
        result = ''
        while self.current_char is not None and (
                self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.step()
        return float(result) if '.' in result else int(result)

    def skip(self):
        while self.current_char is not None and self.current_char in self.ignore:
            self.step()

    def step(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]


class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def parse(self, text):
        self.lexer.input(text)
        self.current_token = self.lexer.get_next_token()

        node = self.expr()
        if self.current_token.type != EOF:
            self.error()
        return node

    def expr(self):
        '''expr   : term ((ADD|SUB) term)*
           term   : factor ((MUL|DIV) factor)*
           factor : NUM | LPAREN factor RPAREN
        '''
        expr = self.term()
        while self.current_token.type in (ADD, SUB):
            token = self.current_token
            self.consume(token.type)
            expr = BinOp(expr, token.value, self.term())
        return expr

    def term(self):
        term = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            self.consume(token.type)
            term = BinOp(term, token.value, self.factor())
        return term

    def factor(self):
        if self.current_token.type == NUM:
            factor = Number(self.current_token.value)
            self.consume(NUM)
        elif self.current_token.type == LPAREN:
            self.consume(LPAREN)
            factor = self.expr()
            self.consume(RPAREN)
        else:
            self.error()
        return factor

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def error(self):
        raise ValueError('Invalid syntax. Unexpected token %s' % self.current_token)


if __name__ == '__main__':
    parser = Parser(Lexer())
    cli.run(parser)
