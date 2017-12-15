# Hackerman || Amstelhaegen || Algorithms
###### Tim Jansen, Jaap Meesters, Christoffel Doorman
------------------------------------------------
 
### filosofie
        
        Als je er vanuit gaat dat elke huis alleen precies op de hele meter kan staan, en 30 meter gemiddeld inneemt, 
        dan zijn er voor de 20-variant grofweg: 360*320 = 115.200 // 115.200 * 115.170 * 115.140 .... * 114.600 =
        +/- 1.6916e101 ofwel 1.691.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000
        -000.000.000.000.000.000.000.000.000.000.000.000.000.000 mogelijkheden. Onvoorstelbaar veel, laat staan 
        het aantal mogelijkheden van de 'echte' vraag, zonder de uitgangspunten die de som vermakkelijken.

        Of wel: 
        - Bruteforce is totaal onhaalbaar, omdat je onmogelijk alle opties af kunt gaan. Maar dat is dan ook
          waarom deze case in het vak Heuristieken zit. 
        - De kans dat je een beetje in de buurt komt bij de beste oplossing met bijvooreeld 1 miljoen keer 
          random is kleiner dan de kans dat je De Lotto wint.
          
         Toch is het niet mogelijk iets ander dan een variatie van random toe tepassen, omdat er geen formule of logica 
         voor dit probleem te bedenken is. Alle algoritmens zullen dus in meer of mindere mate steunen op willekeur. 
         
         We hebben ervoor gekozen te beginnnen met een totaal random algoritme (random_alogrithm), deze hebben we een miljoen
         keer gedraaid, om die optie te overtreffen. De beste van 1 miljoen is een goed uitgangspunt om op door te bouwen. We hebben
         hillclimber laten draaien op die beste, ook hebben we een hill climber laten draaien op de 1 random, om te kijken het 
         uitgangspunt: 'hill climber op de beste van 1 miljoen is beter dan hill climber op een willekeurige' te testen. 
         
         enz enz... 
         ####################################################
         tot nu toe gedaan: 1 miljoen iteraties zie: 'best_random - na 1m.png' in de 'plaatjes' map
         random++ nog niet gemaakt

         Het idee is dat we al een hele goede optie hebben, bijvoorbeeld de beste van 1m randoms. 
         Dan kijken of we die optie nog kunnen optimaliseren. 
         Uitbreiding op randomiser, (soort van Hill climbing)

         Kan ook minder random:
             kiest huis 1 (tot aantal huizen) kijkt of hij kan schuiven 1 meter in een willekeurige richting.
             waarde verhoging? Blijf, en wederom meter willekeurige richting, vermindering? ga terug, andere richting, 
             tot alle richtingen gehad, ga naar volgend huis tot alle huizen gehad.

         vragen:
             - is dit een garantie dat je de beste mogelijkheid vindt? Nee?
             - helpt het als je eerste met de meeste waardevolle huizen gaat schuiven?
          ###############################################
        

## precieze werkingen van de Algoritmen

### random_algorithm

        Bouwt een random huis op een random plek tot alle huizen gebouwd zijn.  
        Berekent de waarde van het totale canvas.
        De meest waardevolle van de, via main.py, opgegeven aantal itteraties geeft hij terug.

### hillclimber_random_algorithm

       Voor een, door de gebruiker in main.py ingevoerde aantal iteraties:
       Pakt een random huis, verplaats hem een random richting van 0.5. 
       Kijkt of het verplaatste huis overlapt met een ander huis, zo ja zet terug.  
       zo nee, append om de waarde te kunnen checken, waarde hoger: blijf daar staan.
       Waarde minder hoog, plaats het huis terug.
       return de nieuwe score en buildings-array aan main.py
       
### hillclimber_algorithm

      Voor een, door de gebruiker in main.py ingevoerde aantal iteraties:
      Voor alle huizen in de map:
      Bekijk alle richtingen van het huis (stap 0.5) kies de richting met hoogste waarde, zonder overlap.
      Return de nieuwe score en buildings-array aan main.py
     
### expanding_universe_algorithm
     
     Stof kan jij deze even in korte pseudocode uitleggen
     
### greedy_algorithm
    
    Plaats een Maison (huis met het meest waarde), random op de map. 
    Plaats een voor een alle andere Maisons, dan Bungalows en dan House's op de plek waar op dat moment de waarde het grootst is.
    
### hillclimber_rotate_move_swap_algorithm

    Voor een, door de gebruiker in main.py ingevoerde aantal iteraties:
    Voor alle huizen in de map:
    Kies random: 
                - verplaats huis in een random richting 0.5 stap 
                - draai het huis 90 graden
                - swap het huis met een random ander huis
    Check de totaal waarde. Als minder dan eerst: zet terug. Als meer: laat staan.
     

    
    
