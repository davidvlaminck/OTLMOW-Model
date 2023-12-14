relation_uris = set()
directional_relation_uris = set()


def get_hardcoded_relation_list():
    if len(relation_uris) == 0:
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerkProtectie')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerktoegang')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftToegangsprocedure')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsAdmOnderdeelVan')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsNetwerkECC')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWOnderdeelVan')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt')
        relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd')

    return relation_uris


def get_hardcoded_directional_relation_list():
    if len(directional_relation_uris) == 0:
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBeheer')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerkProtectie')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerktoegang')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftToegangsprocedure')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsAdmOnderdeelVan')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsNetwerkECC')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWOnderdeelVan')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt')
        directional_relation_uris.add('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd')

    return directional_relation_uris
