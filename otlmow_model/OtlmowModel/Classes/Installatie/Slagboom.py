# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboom(NaampadObject, VlakGeometrie):
    """Een afsluitingsmechanisme met slagboomarmen dat dient om controle uit te kunnen oefenen over het gebruik van een doorgang of een toegang."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeOpslagplaats', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom', direction='i')  # i = direction: incoming

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
