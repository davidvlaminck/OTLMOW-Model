relation_uris = set()


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
