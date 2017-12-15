# Hackerman
Amstelhaegen

# TODO:

     #kan 'olap = True' hier niet weg? (regel 108 van helper.py)
	olap = True
	for building in buildings:
		olap = overlap(maison, building)

Na les 12, 12:

     Presentatie, (10min)
      
     Case uitleg duidelijk maken,
      
     Eigenlijk alles wat je in requirements moet uitleggen ook in de presentatie uitleggen.
     
     Algoritme uitleggen, bijv Hill climber, dan hoef je niet het principe uit te leggen, maar wel hoe je het hebt toegepast, wat het 
     betekent voor jouw case
     
     Geen code in je presentatie verwerken!!! 
     
     Veel duidelijk uitleggen, waaorm bepaalde keuzes gemaakt zijn. 
     
     Tabellen, diagrammen met resultaten laten zien. <----- HIER GEWOON LEKKER VEEL VAN zoals:
     - wat is max waarde 100.000x random?
     - wat is max waarde 1x random dan 100.000x Hill Climber?
     - wat is max waarde 100.000x random + dan 100.000x Hill Climber?
          En dat voor alle algoritmen + alle combinaties. 
     
     Future work, inzicht daarin laten zien, van; 'deze algoritmen geen tijd meer voor, maar is veelbelovend want dit en dat...
     
   Opmerkingen docent:
     
       Vergelijk hill climber op 1random, met 1000 random, welke is beter welke conclusie's kunnen we daaruit trekken?
       
       Plant: ook slechte pakken, want je weet dat je daar in iedergeval niet moet zijn, dus lekker grote stap maken, 
            10 mappen, maken beste krijgen veel kinderen die lijken op ouder, slechtste weinig kinderen die er erg niet op lijken, dan  
            daaruit weer tien beste kiezen en nog een keer enz. enz. enz. Kinderen is de oudermap met kleine veranderingen (1 huis swap)  
            of grote veranderingen (veel huis-swaps, grote stappen naar de andere kant van de map, tien huizen weer helemaal random                   
            neerzetten enz.)
            
       Bij Greedy als twee waardes hetzelfde zijn, zet hij op de laatste waarde.
       
       Als Hill Climber zegt kan geen stappen meer maken, dan simulated annealing (dus tien huizen een stap laten zetten) en kijken of je 
       weer verder kan met Hill Climber, want soms kun je geen huizen meer een stap zetten zonder in waarde omhoog te gaan, terwijl er 
       wel betere mappen zijn, daar kun je dan uitbreken met simulated annealing. Check bij simulated annealing wel de temperatuur (aan 
       de hand van een temperatuur functie, die checkt hoeveel stappen er nog zijn en hoeveel achteruitgang hij dus voor lief neemt, 
       weinig stappen over? wil je geen achteruitgang meer accepteren, want maak je dat nog wel goed? anders gezegd: dat de grote van 
       de verslechtering een overweging is om deze stap wel of niet te accepteren.
   
   
     

Na tech-assist 12-12:

      Maak een map: class, Idee: om zwevende date te voorkomen (pas dan 5punten data-structuur mogelijk)

      requirements files maken? requirements.txt

      Experimentatie: Wat we missen is het laten zien van resultaten, wat krijgen we bij welk algoritme, is dat een verbetering? enz... 
      vergelijk ze, trek conclusie's. bijv. random x aantal keer, wat is je beste? dan hillclimber hoeveel verbetering levert dit op? bij
      alle algoritme minimaal 10.000 iteraties.

      Als we nog creedy maken, hebben we opzich genoeg algoritmen. 


# TODO:
   laatst aangepast: 5-12, 

Naar aanleiding van de les:

    Sommige vrije-vrije-ruimte wordt niet benut, bijvoobeeld als een huis links 10 meter vrij heeft maar rechts maar 5, dan wordt er 5
    dan wordt er 5 meter niet gebruikt. Probeer alle vrije vrije ruimte te benutten! 
    
    De Docent kwam met intresant idee voor een algortime: de huizen als magneten (atomen) die elkaar afstoten op basis van een kracht. 
    Waarbij bijvoorbeeld de Maison's harder stoten dan de Eengezinswoningen. 

Naar aanleiding van tech-assist 

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
    
    water: bij zestig huizen, gewoon x aantal lichamen neerzetten en dan pas de random laten lopen. volgens techt-assist is 2 lichamn het
    beste.
    
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
    
**algoritme**

    alle algoritmen + readme uitleg

**Extra bestanden**

    Aantekeningen: Bevat alle aantekeningen colleges + tech assist, niet direct van belang voor opdracht
    Plaatjes: Alle oude 'parken' die misschien handig zijn voor eindpresentatie.
    Presentatie's: Alle presentatie tijdens de werkgroep.
    Amstelhaegen oude versie's: Bevat alle oude versie's Amstelhaegen.
    



    
    
    
    


