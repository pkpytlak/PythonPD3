1. modul 'beatbox.py' definiuje funkcje 'beatbox()', ktorej argumentem jest sciezka do katalogu zawierajacego 
   definicje danego utworu; funkcja ta tworzy we wspomnianym katalogu plik 'utworX.wav' 

2. modul 'wykres.py' zawiera funkcje 'wykres()', ktora jako argument przyjmuje sciezke do katalogu zawierajacego
   definicje danego utworu; funkcja ta tworzy wykres transformaty Fouriera wczytanej sekwencji sampli

3. modul 'wczytanie.py' definiuje funkcje 'wczytanie()', ktora jako argument przyjmuje sciezke do katalogu zawierajacego
   definicje danego utworu; funkcja ta zapisuje wczytana sekwencje sampli do pliku tekstowego, ktory to nastepnie 
   zapisuje we wspomnianym katalogu jako 'utworX.txt'

4. modul 'zapis.py' definiuje funkcje 'zapis()', ktora jako argument przyjmuje sciezke do katalogu zawierajacego
   definicje danego utworu; funkcja ta wczytuje plik tekstowy zawierajacy sekwencje sampli, a nastepnie zapisuje go
   we wspomnianym katalogu jako plik 'utworX_zapis.wav'