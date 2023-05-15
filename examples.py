#estos son algunos ejemplos generados por chatgpt

# installing lex and yacc 
# pip install ply



#primera parte se crear un lexer

import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
)

# Definición de tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios en blanco y saltos de línea
t_ignore = ' \n'

# Error de token
def t_error(t):
    print(f"Token desconocido: {t.value[0]}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()




#segunda parte
#definir el sintactico yacc
import ply.yacc as yacc
from lexer import tokens

# Reglas de la gramática
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_multiply(p):
    'term : term MULTIPLY factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()



#ingresarlo en un main donde se analice el lexico y sintactico
from lexer import lexer
from parser import parser

while True:
    try:
        s = input('> ')
    except EOFError:
        break
    lexer.input(s)
    result = parser.parse(s)
    print(result)
