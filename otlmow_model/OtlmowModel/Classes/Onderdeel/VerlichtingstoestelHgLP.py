# coding=utf-8
from ...Classes.Abstracten.Verlichtingstoestel import Verlichtingstoestel
from ...Classes.Abstracten.VerlichtingstoestelConnector import VerlichtingstoestelConnector


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelHgLP(Verlichtingstoestel, VerlichtingstoestelConnector):
    """Het geheel van de lagedruk kwik lamp (of fluorescentielamp) (HgLP),, voorschakelapparatuur en de behuizing die werden samengesteld met als doel: * de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen; * de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt; * het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelHgLP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', direction='u')  # u = unidirectional
