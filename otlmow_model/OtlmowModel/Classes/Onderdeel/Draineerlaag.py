# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereLaag import AndereLaag
from ...Classes.Abstracten.LaagDikte import LaagDikte
from ...Datatypes.KlMateriaalDraineerlaag import KlMateriaalDraineerlaag


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draineerlaag(AndereLaag, LaagDikte):
    """Materiaal onder constructies om overdrukken of water af te voeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerlaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer')

        self._materiaalDraineerlaag = OTLAttribuut(field=KlMateriaalDraineerlaag,
                                                   naam='materiaalDraineerlaag',
                                                   label='materiaal draineerlaag',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerlaag.materiaalDraineerlaag',
                                                   definition='Het type van materiaal van de draineerlaag.',
                                                   owner=self)

    @property
    def materiaalDraineerlaag(self) -> str:
        """Het type van materiaal van de draineerlaag."""
        return self._materiaalDraineerlaag.get_waarde()

    @materiaalDraineerlaag.setter
    def materiaalDraineerlaag(self, value):
        self._materiaalDraineerlaag.set_waarde(value, owner=self)
