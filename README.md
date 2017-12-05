# Hackerman
Amstelhaegen

# TODO:
laatst aangepast: 5-12, na aanleiding van tech-assist 

    .gitignore ??
    
    Ook een Algoritmen map aanmaken, met daarin alle algoritmen + een readme daarover.
    
    visualiser.py maken,
    
    overlap in helpers gooien 
    
    main moet het algoritmen aanroepen, dan krijg je een gevulde map, die je dan weer in visualiser kan gooien om een png bestand te 
    krijgen, dus echt alles opdelen. 
    
    link naar je github voor punten aanvraag
    
    nog een 'map'-class maken, daarin sla je de locaties op. Kan in een Array. hierin H_build enz. want nu zijn het een soort van losse 
    functies. 
    
    datastructuur: niet te veel data opslaan, doen we al niet, maar let erop!
    
    inheritance?
    
    Kijk naar het algoritme: greedy, ik zet een plek neer waar de map het meeste waard is, dan weer een huis waar de map het meeste 
    waard is. 
    
    water: bij zestig huizen, gewoon x aantal lichamen neerzetten en dan pas de random laten lopen. volgens techt-assist is dit het beste.
    
    punten aanvraag advies tech-assist:
    datastructuur voor 4 gaan.
    infrastructuur ook 4.
    algoritmen, nu 1 punt, want we hebben er pas 1
    
# Opdracht

**requirements voor de wijk**

    Stuk land:
    
            160x180 meter. // 320x360
    
    woningen:
    
        - Eengezinswoningen:
            60% van aantal huizen
            groote: 8x8 + 2m verplichte vrijstand =  10x10 // 20x20
            waarde: 285.000,- + 3% per vrije-vrije meter
            
        - Bungalow:
            25% van aantal huizen
            groote: 10x7.5 + 3m verplichte vrijstand = 13x10.5 // 26x21
            waarde: 399.000,- + 4% per vrije-vrije meter
            
        - Maison:
            15% van aantal huizen
            groote: 11x10.5 + 6m verplichte vrijstand = 17x16.5 // 34x33
            waarde: 610.000,- + 6% per vrije-vrije meter
            
    water:
    
        20% van de wijk moet uit oppervlkatewater bestaan, opgedeeld in maximaal 4 lichamen.
        hoogte-breedteverhoudingen moet tussen de 1 en 4 liggen.
    
**interpretatie**
    
        - De verplichte vrijstand mag niet gedeeld worden, dus kan bij de huizen opgetelt worden
        - De vrije-vrije ruimte mag wel gedeeld worden
        - Het einde van de kaart is ook een grens voor de Vrije-vrije ruimte, kan hier dus niet buiten vallen
    
**opmerkingen**

        Voor nu nog geen rekening houden met het water, die plaatsen we er later wel zelf in, alleen bij de 6o-huizen variant wordt dit een probleem.
        
        Om van de halve meters af te kome: verdubbel het speelveld en alle huizen, dit maakt voor de berekening van de waarde niks uit, gewoon niet per 1 maar 2 meter vrije-vrije ruimte prijsverbetering. alles achter // is de verdubbelaar
        

# Github

**classes.py**

    Meest recente classes bestand,
    length en width houses, is plus de meegerekende vrije ruimte.

**amstelhaegen.py**

    bevat alle standaard functies.
    - overlap: berekent of de huizen overlappen.
    - build: schrijft huis zoalang ze niet overlappen
    - closest_distance: berekend hoeveel vrij-vrije ruimte elk huis heeft
    - drawBuilding: tekent het huis in png, voor de visualisatie
        
    In Total_houses, de versien (20,40,60) invoeren, de rest werkt dan automatisch

**amstelhaegen_algoritme.py**

    bestaat uit amstelhaegen.py + randomiser. gedurende een zelf ingevoerde tijd, blijft
    hij random 'parken' maken waarvan hij de beste opslaat in een png bestand.

**Extra bestanden**

    Aantekeningen: Bevat alle aantekeningen colleges + tech assist, niet direct van belang voor opdracht
    Plaatjes: Alle oude 'parken' die misschien handig zijn voor eindpresentatie.
    Presentatie's: Alle presentatie tijdens de werkgroep.
    Amstelhaegen oude versie's: Bevat alle oude versie's Amstelhaegen.
    

# Algoritmen

**randomiser**
    amstelhaegen_algoritme.py
    
    voor een bepaald tijd:
        bouwt een random huis op een random plek, tot alle huizen gebouwd
        dan berekent hij de waarden
        meest waardevole tot dan toe slaat hij op
        
        tot nu toe gedaan: 1 miljoen iteraties zie: 'best_random - na 1m.png' in de 'plaatjes' map
        
**random++**
    nog niet gemaakt
    
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
        - wellicht 'Simulated annealing'?? dus 1 stap zetten, dan nog een stap zetten en dan pas checken op waarde vermeerdering?, wellicht wel met drie stappen of vier of vijf??
        
    
    
    
    


