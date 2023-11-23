# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlKopmuurMateriaal import KlKopmuurMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kopmuur(AIMObject, VlakGeometrie):
    """Een kopmuur is een inrichtingselement van de wegbaan, dat gebruikt wordt voor de geleiding van verkeer bij grachten. Een kopmuur is een keermuur die een functie vervult van afwateringssysteem en is in de regel haaks op de hartlijn van de wegcorridor georiënteerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker')

        self._materiaal = OTLAttribuut(field=KlKopmuurMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur.materiaal',
                                       definition='Bepaalt het materiaal van de kopmuur.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de kopmuur."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
