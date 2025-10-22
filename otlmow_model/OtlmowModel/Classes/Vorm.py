# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkObjectSV import LinkObjectSV
from ...Datatypes.DtcDimensie import DtcDimensie, DtcDimensieWaarden
from ...Datatypes.KlVormType import KlVormType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vorm(LinkObjectSV):
    """De vorm of omtrek van iets"""

    typeURI = 'https://w3id.org/tribont/core#Shape'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept.heeftStandaardVorm', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://w3id.org/isCharacterisedBy#isCharacterisedBy', target='https://data.vlaanderen.be/ns/mobiliteit#Verkeerstekenconcept', direction='u')  # u = unidirectional

        self._dimensie = OTLAttribuut(field=DtcDimensie,
                                      naam='dimensie',
                                      label='dimensie',
                                      objectUri='https://w3id.org/tribont/core#Shape.dimensie',
                                      definition='Registreert de afmetingen van de vorm.',
                                      owner=self)

        self._vormType = OTLAttribuut(field=KlVormType,
                                      naam='vormType',
                                      label='vorm type',
                                      objectUri='https://w3id.org/tribont/core#Shape.vormType',
                                      definition='Type van de vorm: cirkel, driehoek, rechthoek,...',
                                      owner=self)

    @property
    def dimensie(self) -> DtcDimensieWaarden:
        """Registreert de afmetingen van de vorm."""
        return self._dimensie.get_waarde()

    @dimensie.setter
    def dimensie(self, value):
        self._dimensie.set_waarde(value, owner=self)

    @property
    def vormType(self) -> str:
        """Type van de vorm: cirkel, driehoek, rechthoek,..."""
        return self._vormType.get_waarde()

    @vormType.setter
    def vormType(self, value):
        self._vormType.set_waarde(value, owner=self)
