""""Script para probar el Pipeline"""


def main():
    """"Funcion principal"""
    print("Iniciando programita de prueba")
    # Creating the HTML file
    with open("build/index.html", "w", encoding="utf-8") as file_html:
        # Adding the input data to the HTML file
        file_html.write('''<html>
        <head>
        <title>Pagina</title>
        </head>
        <body>
        <h1>Welcome</h1>
        <p>Nuevo archivo html</p>
        </body>
        </html>''')


if __name__ == '__main__':
    main()
