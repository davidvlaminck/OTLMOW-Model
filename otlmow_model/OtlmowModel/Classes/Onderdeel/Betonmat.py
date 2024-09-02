# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereLaag import AndereLaag
from ...Classes.Abstracten.ElementSpecificatie import ElementSpecificatie
from ...Datatypes.KlSoortVoegmateriaal import KlSoortVoegmateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Betonmat(AndereLaag, ElementSpecificatie):
    """De betonmat is een specifieke vorm van een bodembescherming die kan bestaan uit betonnen platen, panelen of segmenten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming')

        self._voegmateriaal = OTLAttribuut(field=KlSoortVoegmateriaal,
                                           naam='voegmateriaal',
                                           label='voegmateriaal',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmat.voegmateriaal',
                                           definition='De verschillende mogelijkheden voor materiaal dat wordt gebruikt voor de voegen.',
                                           owner=self)

    @property
    def voegmateriaal(self) -> str:
        """De verschillende mogelijkheden voor materiaal dat wordt gebruikt voor de voegen."""
        return self._voegmateriaal.get_waarde()

    @voegmateriaal.setter
    def voegmateriaal(self, value):
        self._voegmateriaal.set_waarde(value, owner=self)
