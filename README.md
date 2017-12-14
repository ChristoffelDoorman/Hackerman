# Hackerman || Amstelhaegen
###### Tim Jansen, Jaap Meesters, Christoffel Doorman
------------------------------------------------

### Een Algoritme draaien:

        1. Start main op: 'python main.py'
        2. Kies de huizenvariant (20,40 of 60)
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
        
**main**
        
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
        
**helpers** 

      helper_functions.py
        Hierin staan alle globale-basis-functies, deze kunnen door elk alogoritme naar wens
        worden aangeroepen. 
        
        def pythagoras:
                berekent de schuine aftand tussen twee huizen
               
        def overlap
                Berekent of een huis overlapt met een ander huis, door te stellen dat hij per
                definitie overlapt, tenzij: een van de 8 if's waar is. deze if's baseren zich
                op het principe dat als gebouw 1 de linkerhoek x-as groter is dan gebouw 2 de
                rechterhoek x-as, deze elkaar nooit kunnen raken, dit checkt hij voor alle hoeken
                zowel x als y, vandaar 8 statements. Dit checkt hij voor alle gebouwen in de array.
              
        def h_build, b_build, m_build
                kent het gevraagde huis een random waarde op de map toe, vraagt aan de functie overlap
                of er overlap is, zo niet dan append hij het huis.
         
        def closest_distance
        
**visualisatie**           
**algoritmes**        

        
    
        





    
    
    
    


