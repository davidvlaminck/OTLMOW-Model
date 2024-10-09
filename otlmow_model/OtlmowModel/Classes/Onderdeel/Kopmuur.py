# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlHellingshoek import KlHellingshoek
from ...Datatypes.KlKopmuurMateriaal import KlKopmuurMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kopmuur(AIMObject, VlakGeometrie):
    """Een kopmuur is een inrichtingselement van de wegbaan, dat gebruikt wordt voor de geleiding van verkeer bij grachten. Een kopmuur is een keermuur die een functie vervult van afwateringssysteem en is in de regel haaks op de hartlijn van de wegcorridor georiënteerd. Afgeschuinde varianten worden als meer vergevingsgezind gezien bij een aanrijding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WaterdoorvoerendeDuiker', direction='o')  # o = direction: outgoing

        self._hellingshoek = OTLAttribuut(field=KlHellingshoek,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur.hellingshoek',
                                          definition='De hoek tussen de as van de gracht en het vlak van de kopmuur in graden.',
                                          owner=self)

        self._materiaal = OTLAttribuut(field=KlKopmuurMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kopmuur.materiaal',
                                       definition='Bepaalt het materiaal van de kopmuur.',
                                       owner=self)

    @property
    def hellingshoek(self) -> str:
        """De hoek tussen de as van de gracht en het vlak van de kopmuur in graden."""
        return self._hellingshoek.get_waarde()

    @hellingshoek.setter
    def hellingshoek(self, value):
        self._hellingshoek.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de kopmuur."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
