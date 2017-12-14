# Hackerman || Amstelhaegen || Algorithms
###### Tim Jansen, Jaap Meesters, Christoffel Doorman
------------------------------------------------
 
### filosofie
        
        Als je er vanuit gaat dat elke huis alleen precies op de hele meter kan staan, en 30 meter gemiddeld inneemt, 
        dan zijn er voor de 20-variant grofweg: 360*320 = 115.200 // 115.200 * 115.170 * 115.140 .... * 114.600 =
        +/- 1.6916e101 ofwel 1.691.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000
        -000.000.000.000.000.000.000.000.000.000.000.000.000.000 mogelijkheden. Onvoorstelbaar veel, laat staan het aantal mogelijkheden 
        van de 'echte' vraag, zonder de uitgangspunten die de som vermakkelijken.

        Of wel: 
        - Bruteforce is totaal onhaalbaar, omdat je onmogelijk alle opties af kunt gaan. Maar dat is dan ook
          waarom deze case in het vak Heuristieken zit. 
        - De kans dat je een beetje in de buurt komt bij de beste oplossing met bijvooreeld 1 miljoen keer 
          random is kleiner dan de kans dat je De Lotto wint.


### random_algorithm

        Bouwt een random huis op een random plek tot alle huizen gebouwd zijn.  
        Berekent de waarde van het totale canvas.
        De meest waardevolle van de, via main.py, opgegeven aantal itteraties geeft hij terug.

randomiser amstelhaegen_algoritme.py

voor een bepaalde tijd:
    bouwt een random huis op een random plek, tot alle huizen gebouwd
    dan berekent hij de waarden
    meest waardevole tot dan toe slaat hij op
    
    tot nu toe gedaan: 1 miljoen iteraties zie: 'best_random - na 1m.png' in de 'plaatjes' map
random++ nog niet gemaakt

Het idee is dat we al een hele goede optie hebben, bijvoorbeeld de beste van 1m randoms. Dan kijken of we die optie nog kunnen optimaliseren.

uitbreiding op randomiser, (soort van Hill climbing)
na beste randomiser na x iteraties:
    kies een random huis, probeer die random op een beter plek te plaatsen, waarde verhoging? houd deze daar, waardevermindering? plaats huis terug,
        volgende random huis.

Kan ook minder random:
    kiest huis 1 (tot aantal huizen) kijkt of hij kan schuiven 1 meter in een willekeurige richting.
    waarde verhoging? Blijf, en wederom meter willekeurige richting, vermindering? ga terug, andere richting, tot alle richtingen gehad, ga naar volgend huis tot alle huizen gehad.

vragen:
    - is dit een garantie dat je de beste mogelijkheid vindt? Nee?
    - helpt het als je eerste met de meeste waardevolle huizen gaat schuiven?
