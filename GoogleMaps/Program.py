import webbrowser as web
address = input('Inserisci la località:')
web.open('https://www.google.com/maps/place/' + address)
