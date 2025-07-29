# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlBinnenverlichtingGroepVerlichtGebied import KlBinnenverlichtingGroepVerlichtGebied
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BinnenverlichtingGroep(NaampadObject, PuntGeometrie):
    """Een groep voor het groeperen van objecten van het type Binnenverlichtingstoestel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BinnenverlichtingGroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ActivityComplex', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelTL', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='i')  # i = direction: incoming

        self._verlichtGebied = OTLAttribuut(field=KlBinnenverlichtingGroepVerlichtGebied,
                                            naam='verlichtGebied',
                                            label='verlicht gebied',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BinnenverlichtingGroep.verlichtGebied',
                                            definition='Het gebied dat verlicht wordt door de binnenverlichtingstoestellen die deel uitmaken van de groep.',
                                            owner=self)

    @property
    def verlichtGebied(self) -> str:
        """Het gebied dat verlicht wordt door de binnenverlichtingstoestellen die deel uitmaken van de groep."""
        return self._verlichtGebied.get_waarde()

    @verlichtGebied.setter
    def verlichtGebied(self, value):
        self._verlichtGebied.set_waarde(value, owner=self)
