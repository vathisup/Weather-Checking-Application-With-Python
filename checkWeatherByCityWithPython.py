import requests

print(f'Welcome to weather checking APP.\n')

loop=True
loop2=True
while(loop):
    while(loop2):
        city = input(f'Enter your search location: ')

        # Insert your api into here and add "city" variable to the query part of API
        # This program uses Open Weather Map api.
        apiWeather = ''

        weather = requests.get(f'').json()

        
        if(weather=={'cod': '404', 'message': 'city not found'}):
            print(f"city not found")
            break
        
        weathertype=weather["weather"]
        weatherTypeInside=weathertype[0]
        
        
        print(f"The weather in {city} is {weatherTypeInside['main']} with the temperature of {weather['main']['temp']}°C")

        loop2=False
    
    conti=input(f"Do you want to continue? Y/N: ")
    if(conti=="Y" or conti=="y"):
        loop2=True
        
    elif(conti=="N" or conti=="n"):
        
        loop=False


