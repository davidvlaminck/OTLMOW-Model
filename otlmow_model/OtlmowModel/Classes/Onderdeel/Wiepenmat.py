# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereLaag import AndereLaag
from ...Classes.Abstracten.ElementSpecificatie import ElementSpecificatie
from ...Datatypes.KlSoortVoegmateriaal import KlSoortVoegmateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wiepenmat(AndereLaag, ElementSpecificatie):
    """Een wiepenmat is een specifieke vorm van een bodembescherming die bestaat uit een houten gevlochten mat in combinatie met een geotextiel waarboven nadien stortsteen (breuksteen) wordt aangebracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiepenmat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='i')  # i = direction: incoming

        self._voegmateriaal = OTLAttribuut(field=KlSoortVoegmateriaal,
                                           naam='voegmateriaal',
                                           label='voegmateriaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiepenmat.voegmateriaal',
                                           definition='De verschillende mogelijkheden voor materiaal dat wordt gebruikt voor de voegen',
                                           owner=self)

    @property
    def voegmateriaal(self) -> str:
        """De verschillende mogelijkheden voor materiaal dat wordt gebruikt voor de voegen"""
        return self._voegmateriaal.get_waarde()

    @voegmateriaal.setter
    def voegmateriaal(self, value):
        self._voegmateriaal.set_waarde(value, owner=self)
