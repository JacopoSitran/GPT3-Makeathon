prompt = """Determine types given ids using data from the text:

Text: Endrechnungskennzeichen. Bitte in folgenden Bestellungen das Endrechnungskennzeichen setzen.

9704530974
9704679737
 
Vielen Dank!

Ids:
9704530974
9704679737

Types:
['erk']
['erk']

###

Text: Endlieferkennzeichen entfernen. bitte bei folgenden PO Nummern die Endlieferkennzeichen entfernen.
 
9703924315
9703951260
 
$PERSON Dank für Ihre Mühe.

Ids:
9703924315
9703951260

Types:
 ['elk']
 ['elk']

###

Text: Endliefer- und Endrechnungskennzeichen - PV2054. bitte ein Endliefer- und Endrechnungskennzeichen setzen
 
9704397649
9704576212
9704813477 (Endrechnungskennzeichen)

Ids:
9704397649
9704576212
9704813477

Types:
['elk', 'erk']
['elk', 'erk']
['erk']

###
Text: Endliefer- und Endrechnungskennzeichen. bitte ein Endliefer- und Endrechnungskennzeichen setzen.
 
9704192220 Endliefer- und Endrechnungskennzeichen
 
9704187821 Pos. 1 und Pos. 2 Endrechnungskennzeichen
 
9704162452 Endliefer- und Endrechnungskennzeichen
 
9704513807 Endliefer- und Endrechnungskennzeichen
 
9704600263 Pos.3 Endrechnungskennzeichen
 
9704247345 Pos. 6 Endrechnungskennzeichen
 
9704613085 alle Positionen $PERSON 9704131664 Pos. 1 Endliefer- und Endrechnungskennzeichen
 
9704439738 Endliefer- und Endrechnungskennzeichen
 
9704503485 Endlieferungskennzeichen
 
9704540086
Endliefer- und Endrechnungskennzeichen

Ids:
9704192220: 
9704187821: 
9704162452: 
9704513807: 
9704600263:
9704247345: 
9704613085: 
9704131664:
9704439738: 
9704503485: 
9704540086: 
Types:
['elk', 'erk']
['erk']
['elk', 'erk']
['elk', 'erk']
['erk']
['erk']
['elk', 'erk']
['elk', 'erk']
['elk', 'erk']
['elk']
['elk', 'erk']

###

Text: Bestellungen schließen - PV2053. bitte bei diesen Bestellungen (bitte Bestellpositionen beachten!) ein Endrechnungskennzeichen setzen.
 
9704247345 1
9704247345 2
9704247345 3
9704247345 4
9704247345 5
Position 6 bitte nicht schließen, da kommen noch Kosten!
 
9704281131 1
9704281131 2
 
9704600263 1
9704600263 2
Position 3 bitte nicht schließen, da kommen noch Kosten!
 
 
 
Bei diesen Bestellungen bitte ein Endliefer- und Endrechnungskennzeichen setzen
 
9704314518 1
9704376340 1
 
Vielen Dank

Ids:
9704247345: 
9704281131: 
9704600263:
9704314518: 
9704376340:

Types:
['erk']
['erk']
['erk']
['elk', 'erk']
['elk', 'erk']

###
"""

text_prompt = """

        WG: Endliefer- und Endrechnungskennzeichen - PV2050. hier nochmal unverschlüsselt…
        -----
        Endliefer- und Endrechnungskennzeichen - PV2050
        
        
        bitte bei folgenden Bestellungen ein Endliefer- und Endrechnungskennzeichen setzen.
        
        9704187851 Pos. 1 und 2 (Endrechnungskennzeichen)
        
        9704612454 Pos. 1 und 2 (Endrechnungskennzeichen)
        
        9704114442 Pos. 1 und 2 (Endrechnungs- und Endlieferkennzeichen)
        
        9703784941 Pos. 1 und 2 (Endrechnungs- und Endlieferkennzeichen)
        
        9704187708 Pos. 1 und 2 (Endrechnungskennzeichen)
        
        9704613098 Pos. 1 und 2 (Endrechnungskennzeichen)
        
        9704242380 Pos. 1 (Endrechnungskennzeichen)
        
        9704634083 Pos. 1 und 2 (Endrechnungskennzeichen)
        
        9704187710 Pos. 1 und 2 (Endrechnungskennzeichen)
        
        9704616065 Pos. 1 und 2 (Endrechnungskennzeichen)"""

extracted_ids = """

Ids:
9704187851
9704612454
9704114442
9703784941
9704187708
9704613098
9704242380
9704634083
9704187710
9704616065
"""