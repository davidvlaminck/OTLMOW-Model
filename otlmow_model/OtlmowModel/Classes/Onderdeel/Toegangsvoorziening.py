# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangsvoorziening(AIMNaamObject, PuntGeometrie):
    """Een toegangsschouw of ruimte dat is ontworpen om personen in staat te stellen componenten van de sluis of stuw te bereiken, te inspecteren en eraan te werken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder', direction='u')  # u = unidirectional

        self._afmetingen = OTLAttribuut(field=StringField,
                                        naam='afmetingen',
                                        label='afmetingen toegangsvoorziening',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening.afmetingen',
                                        definition='De afmetingen van de toegangsschouw en ruimte, uitgedrukt in centimeter.',
                                        owner=self)

        self._isVeiligheidsvoorzieningAanwezig = OTLAttribuut(field=BooleanField,
                                                              naam='isVeiligheidsvoorzieningAanwezig',
                                                              label='is veiligheidsvoorziening aanwezig',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening.isVeiligheidsvoorzieningAanwezig',
                                                              definition='Geeft aan of er een veiligheidsvoorziening aanwezig is',
                                                              owner=self)

    @property
    def afmetingen(self) -> str:
        """De afmetingen van de toegangsschouw en ruimte, uitgedrukt in centimeter."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def isVeiligheidsvoorzieningAanwezig(self) -> bool:
        """Geeft aan of er een veiligheidsvoorziening aanwezig is"""
        return self._isVeiligheidsvoorzieningAanwezig.get_waarde()

    @isVeiligheidsvoorzieningAanwezig.setter
    def isVeiligheidsvoorzieningAanwezig(self, value):
        self._isVeiligheidsvoorzieningAanwezig.set_waarde(value, owner=self)
