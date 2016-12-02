__author__ = 'Geoge'

from floraparser.TaxaToCharacters import *

fromdb = False
#fromdb = True

if fromdb:

    # query="Select * from AllTaxa where flora_name = 'FZ' and rank = 'species' and genus = 'Salacia' ;"
    # query = "Select * from AllTaxa where flora_name = 'FTEA' and rank = 'species' and genus = 'Salacia' and species = 'erecta' ;"
    # query="Select * from AllTaxa where flora_name = 'FZ' and rank = 'species' and genus = 'Acacia' and species = 'albida'  ;"
    # query="Select * from AllTaxa where flora_name = 'FTEA' and rank = 'species' and genus = 'Allophylus' and species = 'abyssinicus' ;"
    query="Select * from AllTaxa where flora_name = 'FTEA' and rank = 'species' and family = 'Sapindaceae' ;"

    charactersFromDB(query)

else:
    description = '''
    Plant: Much-branched shrub or small tree, dioecious or less commonly monoecious, 1–9 m tall; bark grey, fairly smooth (fide Greenway) to rough (Lynes specimen); branchlets subglabrous (apart from the glands) to tomentellous or occasionally densely pilose further south. Leaves scented; blades linear-oblanceolate to oblanceolate or ± oblong-elliptic, up to 7–12 cm long, 1–3 cm wide (sometimes smaller in South Africa), acute to bluntly pointed at the apex, long-attenuate at the base, subentire to coarsely and rather distantly serrate in the upper half or two-thirds, the margin often becoming somewhat incurved and slightly crenate between the teeth, glabrous to rather inconspicuously pubescent mainly on the midrib towards the base, rarely (not in East Africa) rather densely hairy overall, usually rather densely covered with golden- yellow glands on both surfaces, pock-marked when the glands wither; lateral nerves on either side generally 20–30 or more, inconspicuous beneath, the finer venation obscure; petiole 3–5 mm long. Female flowers borne on the upper part of the catkin. Male catkins dense, 0.5–3 cm long, reddish or purplish-brown when young; bracts broadly ovate-triangular or deltoid in the upper part, abruptly contracted to a narrow base and with cusp- like points either side at the middle, 1–1.5 mm long, glandular, ciliate, rarely with a short pubescence dorsally; stamens 3–4(–5), fewer in the lowermost bracts only; anthers sometimes papillose or hairy. Female catkins usually dense at first, 0.5–1.2 cm long, elongating and up to 3–4 cm long in fruit; bracts ovate-triangular, sometimes broadly so, to transversely rhombic; bracteoles usually 4, ovate, concave, 0.4–0.7 mm long, densely hairy; style-arms slender, long-caudate, 1.5–3 mm long. Fruits ellipsoid-globose, 3–4 mm across.
    '''

    # description = 'lamina cordate or rounded at the base'

    parser = FeatureBottomUpLeftCornerChartParser
    # parser = FeatureEarleyChartParser
    # parser = FeatureTopDownChartParser

    cleantree = False
    cleantree = True
    ttrace = 1
    draw=True
    draw=False
    testphrases = True
    prefixdesc = 'Plant is '
    prefixdesc = None

    trec = defaultdict(lambda: None)
    trec['taxonNo'] = 666
    trec['family'] = 'testfam'
    trec['genus'] = 'Test'
    trec['species'] = 'run'
    trec['rank'] = 'species'
    trec['description'] = description

    trdr = [trec]

    charactersFromText(trdr, ttrace=ttrace, draw=draw, outmode='csv')
    # print (flDescToPhrases(ttrace=0, **trec))