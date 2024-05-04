from Lexer.lexer import Lexer

if __name__ == '__main__':
    with open('TOFLPLY/sample2.hp7', 'r') as file:
        data = file.read()

    program = Lexer(data)
    program.run()