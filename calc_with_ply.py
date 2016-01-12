import operator

import ply.lex as lex
import ply.yacc as yacc

tokens = ['NUMBER']

literals = '+-*/()'

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div
}


t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+(:?\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_expr(p):
    'factor :  "(" expression ")"'
    p[0] = p[2]


def p_operators(p):
    '''expression : expression "+' term
                  | expression '-' term
       term       : term '*' factor
                  | term '/' factor
    '''
    p[0] = operators[p[2]](p[1], p[3])


def p_error(p):
    print('Syntax error in input!')


if __name__ == '__main__':
    lexer = lex.lex()
    parser = yacc.yacc()
    while True:
        try:
            s = raw_input('calc> ')
            if not s:
                continue
            print(parser.parse(s))
        except (EOFError, KeyboardInterrupt):
            break
