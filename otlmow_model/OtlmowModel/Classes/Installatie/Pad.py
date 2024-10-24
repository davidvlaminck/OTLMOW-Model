# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlPadNetwerkprotectie import KlPadNetwerkprotectie
from otlmow_model.OtlmowModel.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pad(NaampadObject, GeenGeometrie):
    """Een aaneengesloten reeks van benen die samen een verbinding realiseren over het netwerk, gebruik makende van eenzelfde technologie (vb SDH, OTN...). De verschillende benen binnen een pad volgen bij voorkeur een gescheiden geografisch traject binnen het netwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerkProtectie', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerkProtectie', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Been', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='i')  # i = direction: incoming

        self._netwerkprotectie = OTLAttribuut(field=KlPadNetwerkprotectie,
                                              naam='netwerkprotectie',
                                              label='netwerkprotectie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad.netwerkprotectie',
                                              kardinaliteit_max='*',
                                              definition='Referentie van het pad dat redundantie levert aan dit pad.',
                                              owner=self)

    @property
    def netwerkprotectie(self) -> List[str]:
        """Referentie van het pad dat redundantie levert aan dit pad."""
        return self._netwerkprotectie.get_waarde()

    @netwerkprotectie.setter
    def netwerkprotectie(self, value):
        self._netwerkprotectie.set_waarde(value, owner=self)
