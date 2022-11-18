# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboom(NaampadObject, VlakGeometrie):
    """Een afsluitingsmechanisme met slagboomarmen dat dient om controle uit te kunnen oefenen over het gebruik van een doorgang of een toegang."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite')

        self._isManueel = OTLAttribuut(field=BooleanField,
                                       naam='isManueel',
                                       label='is manueel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom.isManueel',
                                       usagenote='Voor een manuele slagboom zijn geen instanties van de onderliggende onderdelen Slagboomkolom en Slagboomarm vereist.',
                                       definition='Geeft aan of de slagboom (uitsluitend) manueel bediend wordt of door een aangestuurde motor in de slagboomkolom.',
                                       owner=self)

    @property
    def isManueel(self) -> bool:
        """Geeft aan of de slagboom (uitsluitend) manueel bediend wordt of door een aangestuurde motor in de slagboomkolom."""
        return self._isManueel.get_waarde()

    @isManueel.setter
    def isManueel(self, value):
        self._isManueel.set_waarde(value, owner=self)
