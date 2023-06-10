from flask import Flask
from datetime import datetime

# Wszystko co jest potrzebne do utworzenia aplikacji webowej w podstawowej konfiguracji
app = Flask(__name__)


@app.route('/')     # Przekazywanie dodatkowych parametrów w dekoratorze
def hello_world():  # put application's code here
    return 'Hello World!'

# Jeżeli my uruchamiamy ten program z tego pliku należy uruchomić metodę run()
if __name__ == '__main__':
    app.run()

@app.route('/date')
def current_date():
    return f'Response time: {str(datetime.now())}'

# End Point - to URL, czyli ciąg znaków wskazujący na jakiś "zasób" który jest osadzony na stronie internetowej
# End Point to adres do zasobow

# Lokal host: http://127.0.0.1:5000 dostęp tylko z tego komputera
# żeby aplikacja była dostępna na zewnatrz trzeba byłoby ja zainstalowac na jakims serwerze zewnetrznym
# na Azurze na wirtualnej maszynie na przklad

counter = int()

@app.route('/counter')
def current_counter():
    global counter  # bez tego nie da sie incrementowac zmiennej
    counter += 1
    return f'Liczba wywołan to: {counter}'






