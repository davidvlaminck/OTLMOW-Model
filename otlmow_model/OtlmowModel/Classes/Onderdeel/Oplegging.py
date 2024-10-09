# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlBewegingsvrijheidInVlakBijOplegging import KlBewegingsvrijheidInVlakBijOplegging
from ...Datatypes.KlTypeOplegging import KlTypeOplegging
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegging(AIMNaamObject, PuntGeometrie):
    """Een oplegging of steunpunt is een element dat is vastgemaakt aan de vaste ondergrond (vb. aan het landhoofd) of aan een ander constructiedeel. Een oplegging beperkt hier de beweging van het bewegend lichaam (vb. van de brugklap). Een oplegging kan ook een dempend effect hebben bij het sluiten van een bewegend lichaam."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij', direction='o')  # o = direction: outgoing

        self._bewegingsvrijheidInHetVlak = OTLAttribuut(field=KlBewegingsvrijheidInVlakBijOplegging,
                                                        naam='bewegingsvrijheidInHetVlak',
                                                        label='bewegingsvrijheid in het vlak',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.bewegingsvrijheidInHetVlak',
                                                        kardinaliteit_max='*',
                                                        definition='De bewegingsvrijheid in het vlak. Er kunnen meerdere mogelijkheden zijn.',
                                                        owner=self)

        self._type = OTLAttribuut(field=KlTypeOplegging,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.type',
                                  definition='De soort oplegging.',
                                  owner=self)

        self._zijnNegatieveSteunpuntreactiesAanwezig = OTLAttribuut(field=BooleanField,
                                                                    naam='zijnNegatieveSteunpuntreactiesAanwezig',
                                                                    label='zijn negatieve steunpuntreacties aanwezig',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.zijnNegatieveSteunpuntreactiesAanwezig',
                                                                    definition='Geeft aan of er negatieve steunpuntreacties aanwezig zijn, al dan niet.',
                                                                    owner=self)

    @property
    def bewegingsvrijheidInHetVlak(self) -> List[str]:
        """De bewegingsvrijheid in het vlak. Er kunnen meerdere mogelijkheden zijn."""
        return self._bewegingsvrijheidInHetVlak.get_waarde()

    @bewegingsvrijheidInHetVlak.setter
    def bewegingsvrijheidInHetVlak(self, value):
        self._bewegingsvrijheidInHetVlak.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """De soort oplegging."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def zijnNegatieveSteunpuntreactiesAanwezig(self) -> bool:
        """Geeft aan of er negatieve steunpuntreacties aanwezig zijn, al dan niet."""
        return self._zijnNegatieveSteunpuntreactiesAanwezig.get_waarde()

    @zijnNegatieveSteunpuntreactiesAanwezig.setter
    def zijnNegatieveSteunpuntreactiesAanwezig(self, value):
        self._zijnNegatieveSteunpuntreactiesAanwezig.set_waarde(value, owner=self)
