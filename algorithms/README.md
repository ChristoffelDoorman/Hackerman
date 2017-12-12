
# Algoritmen



**randomiser**
    amstelhaegen_algoritme.py
    
    voor een bepaalde tijd:
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
        
    
    
    
    


