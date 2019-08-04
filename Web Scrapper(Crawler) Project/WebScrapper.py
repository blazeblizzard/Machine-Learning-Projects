# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 02:20:50 2019

@author: pawan
"""
"""problems faced 
                1. No classes for different elements ,so I had to use index for every 'find_all(tag)'.
                2. The website design is shitty.
                3. Nidorans Name (male symbol), Other such type pokes too
                4. Used re.sub() to remove male symbol 
                5. Promblem with Shyamin's page
                6. Last two pokes left because of shity design(Meltan's page)"""
                




from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)').text
soup = BeautifulSoup(source, 'lxml')

csv_file=open('PokemonDataFinal.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Name','Ability','DexColor','Type'])

link=soup.find('div', id='mw-content-text').find('table').find_all('tr')[4].find_all('td')[2].a.get('href')

for link in range(493):      
    link=soup.find('div', id='mw-content-text').find('table').find_all('tr')[4].find_all('td')[2].a.get('href')
    test='https://bulbapedia.bulbagarden.net'+link
    
    pokename= soup.find('h1', class_='firstHeading')
    PokeInfo= soup.find('div', id='mw-content-text')
    infoPoke=PokeInfo.find('table', class_='roundy')
   
    
    try:
        namePoke= pokename.text.split('(')[0]
        namePoke_simple=re.sub(r'[^\w]','',namePoke)      
    except Exception as e:
        namePoke_simple=None
           
    try:
        typePoke=infoPoke.find_all('tr')[8].td.table.tr.td.table.tr.td.a.span.b.text
        
    except Exception as e:
        typePoke=None
        
    try:
        abilityPoke=infoPoke.find_all('tr')[16].td.table.tr.td.a.span.text
    
    except Exception as e:
        abilityPoke=None
        
    try:
        pokedexColor=infoPoke.find_all('tr')[66].td.table.tr.td.text.strip()
    
    except Exception as e:
        pokedexColor=None
       
    """for dual typings use this #typePoke=typePoke.td.table.tr.td.table.tr.td.a.span.b.text + '+' + typePoke.td.table.tr.td.table.tr.find_all('td')[1].a.span.b.text"""

    print(namePoke)
    """print(typePoke)
    print(abilityPoke)
    print(pokedexColor) #strip() to remove extra space in the string"""
    
    csv_writer.writerow([namePoke_simple,abilityPoke,pokedexColor,typePoke])
  
    soup = BeautifulSoup(requests.get(test).text, 'lxml')


source = requests.get('https://bulbapedia.bulbagarden.net/wiki/Victini_(Pok%C3%A9mon)').text
soup = BeautifulSoup(source, 'lxml')    
for link in range(314):      
    link=soup.find('div', id='mw-content-text').find('table').find_all('tr')[3].find_all('td')[2].a.get('href')

    test='https://bulbapedia.bulbagarden.net'+link
    
    pokename= soup.find('h1', class_='firstHeading')
    PokeInfo= soup.find('div', id='mw-content-text')
    infoPoke=PokeInfo.find('table', class_='roundy')
   
    
    try:
        namePoke= pokename.text.split('(')[0]
        namePoke_simple=re.sub(r'[^\w]','',namePoke)      
    except Exception as e:
        namePoke_simple=None
           
    try:
        typePoke=infoPoke.find_all('tr')[8].td.table.tr.td.table.tr.td.a.span.b.text
        
    except Exception as e:
        typePoke=None
        
    try:
        abilityPoke=infoPoke.find_all('tr')[16].td.table.tr.td.a.span.text
    
    except Exception as e:
        abilityPoke=None
        
    try:
        pokedexColor=infoPoke.find_all('tr')[66].td.table.tr.td.text.strip()
    
    except Exception as e:
        pokedexColor=None
       
    """for dual typings use this #typePoke=typePoke.td.table.tr.td.table.tr.td.a.span.b.text + '+' + typePoke.td.table.tr.td.table.tr.find_all('td')[1].a.span.b.text"""

    print(namePoke)
    """print(typePoke)
    print(abilityPoke)
    print(pokedexColor) #strip() to remove extra space in the string"""
    
    csv_writer.writerow([namePoke_simple,abilityPoke,pokedexColor,typePoke])
    
    soup = BeautifulSoup(requests.get(test).text, 'lxml')


source = requests.get('https://bulbapedia.bulbagarden.net/wiki/Meltan_(Pok%C3%A9mon)').text
soup = BeautifulSoup(source, 'lxml') 
    
csv_file.close()


