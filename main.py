#>  <
import click

@click.group()
def main():
    pass


@main.command()
def manda():
    print("ktmr")

@main.command()
def saluda_usuarios():
    print('hola mundo ')

@main.command()
def despedida_usuarios():
    print('chau mundo ')

@main.command()
def despedida():
    print('chau mundo ')

@main.command()
def calculadora():
    a = int(input("ingresa 1 numero "))
    b = int(input("ingresa otro numero "))
    c = a + b
    print( " el resultado de la suma es ", c)

if __name__ == '__main__':
    main()