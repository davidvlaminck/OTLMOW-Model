# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanvaarbeschermingGeleidewerk import AanvaarbeschermingGeleidewerk
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlTypeGeleidewerk import KlTypeGeleidewerk
from ...Datatypes.KlWijzeGeleiding import KlWijzeGeleiding


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleidewerk(AanvaarbeschermingGeleidewerk, AIMNaamObject):
    """Een constructie in een waterweg waarmee schepen worden geleid als ze een kunstwerk zoals een brug of sluis naderen, binnenvaren of passeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Geleidewerk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementAanvaarbeschermingGeleidewerk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fuik', direction='o')  # o = direction: outgoing

        self._isAfmeringMogelijk = OTLAttribuut(field=BooleanField,
                                                naam='isAfmeringMogelijk',
                                                label='is afmering mogelijk',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Geleidewerk.isAfmeringMogelijk',
                                                definition='Geeft aan of afgemeerd kan worden aan het geleidewerk.',
                                                owner=self)

        self._typeGeleidewerken = OTLAttribuut(field=KlTypeGeleidewerk,
                                               naam='typeGeleidewerken',
                                               label='type geleidewerken',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Geleidewerk.typeGeleidewerken',
                                               definition='De verschillende types van geleidewerk.',
                                               owner=self)

        self._wijzeGeleiding = OTLAttribuut(field=KlWijzeGeleiding,
                                            naam='wijzeGeleiding',
                                            label='wijze van geleiding',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Geleidewerk.wijzeGeleiding',
                                            definition='De wijze van de geleiding.',
                                            owner=self)

    @property
    def isAfmeringMogelijk(self) -> bool:
        """Geeft aan of afgemeerd kan worden aan het geleidewerk."""
        return self._isAfmeringMogelijk.get_waarde()

    @isAfmeringMogelijk.setter
    def isAfmeringMogelijk(self, value):
        self._isAfmeringMogelijk.set_waarde(value, owner=self)

    @property
    def typeGeleidewerken(self) -> str:
        """De verschillende types van geleidewerk."""
        return self._typeGeleidewerken.get_waarde()

    @typeGeleidewerken.setter
    def typeGeleidewerken(self, value):
        self._typeGeleidewerken.set_waarde(value, owner=self)

    @property
    def wijzeGeleiding(self) -> str:
        """De wijze van de geleiding."""
        return self._wijzeGeleiding.get_waarde()

    @wijzeGeleiding.setter
    def wijzeGeleiding(self, value):
        self._wijzeGeleiding.set_waarde(value, owner=self)
