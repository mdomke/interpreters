import logging

import ply.lex as lex
import ply.yacc as yacc

from ast import BinOp, Number
import cli

tokens = ['NUMBER']

literals = '+-*/()'

t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+(:?\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
)


def p_expr(p):
    '''expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr
    '''
    p[0] = BinOp(p[1], p[2], p[3])


def p_expr_paren(p):
    'expr : "(" expr ")"'
    p[0] = p[2]


def p_expr_number(p):
    'expr : NUMBER'
    p[0] = Number(p[1])


def p_error(p):
    print('Syntax error')


if __name__ == '__main__':
    logging.basicConfig(filename='debug.log', filemode='w', level='DEBUG', format='%(message)s')
    lexer = lex.lex()
    parser = yacc.yacc()
    cli.run(parser, debug=logging.getLogger())
