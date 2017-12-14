# Hackerman || Amstelhaegen
###### Tim Jansen, Jaap Meesters, Christoffel Doorman
------------------------------------------------

### Een Algoritme draaien:

        1. Start main: 'python main.py'
        2. Kies de huizenvariant (20, 40 of 60)
        3. Kies een algoritme
        4. Afhankelijk van je keuze: kies hoe vaak het algoritme te draaien
        
     *Alle mogelijken combinaties van verschilende algoritmen zijn ook in het keuzesmenu te vinden.
    
### Om de uitkomst (data) van je algoritme te zien:

        1. ga naar het mapje output
        2. kies het algortime dat je hebt gedraaid
        3. kies de huizenvariant
        4. zoek op datum de uitkomst
        
### infrastructuur:
        
   Alle algoritmen zijn aan te roepen vanaf main.py. Deze algoritmen schakkelen op hun beurt de hulp in van: classes, helpers en
   visualisatie. Hier volgt een korte uitleg van deze files.
        
**Main**
        
      main.py
        Vraagt om de huizenvariant: 20, 40 of 60.
        Bevat een keuzemenu van alle algoritmen.
        Vraagt hoevaak hij het algoritme moet laten draaien.
        Roept Visualisation op om de verkregen data op te slaan. 
                   
**Classes**
        
      my_classes.py
        Bevat alle classes: House, Bungalow, Maison, Water.
                De x,y coordinaten die ze krijgen bepalen waar de linker-bodem-hoek staat
                Bevatten een functie (def update) waarmee ze verplaatst kunnen worden.
                Bevattten de functie score, die hun persoonlijke waarde kan berekenen.
        
**Helpers** 

      helper_functions.py
        Hierin staan alle globale-basis-functies, deze kunnen door elk alogoritme naar wens
        worden aangeroepen. 
        
        def pythagoras:
                berekent de schuine aftand tussen twee huizen
               
        def overlap
                Berekent of een huis overlapt met een ander huis, door te stellen dat hij per
                definitie overlapt tenzij: een van de 8 if's waar is. deze if's baseren zich
                op het principe dat als gebouw 1 de linkerhoek x-as groter is dan gebouw 2 de
                rechterhoek x-as, deze elkaar nooit kunnen raken, dit checkt hij voor alle hoeken
                zowel x als y, vandaar 8 statements. Dit checkt hij voor alle gebouwen in de array.
              
        def h_build, b_build, m_build
                Kent het gevraagde huis een random plek op de map toe, vraagt aan de functie overlap
                of er overlap is, zo niet dan append hij het huis.
         
        def closest_distance
                Kijkt voor alle gebouwen in de array, welk gebouw het dichtst in de buurt staat
                of te wel hoeveel vrije ruimte dat gebouw heeft. Met behulp van def pythagoras
                
        def calculate_score
                Zegt voor alle gebouwen in de array:
                Met hulp van closest_distance bereken de vrij-vrije ruimte van dat gebouw.
                Met hulp van de score functie in classes bereken de waarde van dat gebouw.
                Tel alle waardes van alle gebouwen bij elkaar op voor de totaalwaarde.
                
        def move
                Beweegt het gevraagde gebouw, in de gevraagde richting, voor het gevraagde aantal stappen.
                1 step is 1 meter.
                direction 1 == naar rechts.
                direction -1 == naar links.
                direction 2 == naar boven.
                direction -2 == naar beneden.
        
**Visualisatie**    
        
      canvas.visualisation.py
        Is puur voor de visualisatie van de data. 
        
        def draw_canvas
                Tekent de map.
                Met een groote van X 0 tot 360
                En een groote van  Y 0 tot 320
                
        def drawBuilding
                tekent 1 gebouw.
                Op zijn x,y-coordinaat (de linkeronder-hoek).  
                Met zijn lengte en breedte en een lijn-dikte van 1.
                De kleur is afhankelijk van wat hij meekrijgt.
       
       Def main
                De hoofdfunctie van visualisation. Deze roept main.py op.       
                Roept draw_canvas op om de map te maken. 
                Roept voor alle gebouwen in de list drawBuilding op, geeft kleur mee.
                Voor een House de kleur rood, een Bungalow de kleur zwart en een Maison de kleur groen.
                Slaat het getekende plaatje op in een png bestand in de bijbehorende map (afhankelijk van het
                algoritme en de huizenvariant) geeft een datum + tijd van printen mee. 
              
**Algoritmes**        

        Hierin bevinden zich alle algoritmen, deze kunnen via main worden opgeroepen, en gecombineert worden.
        
        random_algorithm.py
        hillclimber_algorithm.py
        hillclimber_random.py
        hillclimber_rotate_move_swap_algorithm.py
        expanding_universe_algorithm.py
        greedy_algorithm.py     
        
        Voor meer informatie over de Algoritmen, zie in mapje algorithms: readme.md.
    
        





    
    
    
    


