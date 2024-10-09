# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlVWCTypeNivelleringssysteem import KlVWCTypeNivelleringssysteem
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VasteWaterbouwkundigeConstructie(AIMNaamObject, VlakGeometrie):
    """Statische bouwkundige constructie in of aan een waterloop al dan niet in combinatie met een beweegbare waterkerende constructie, om grond en een waterpeilverschil te keren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw', direction='o')  # o = direction: outgoing

        self._heeftPompput = OTLAttribuut(field=BooleanField,
                                          naam='heeftPompput',
                                          label='heeft pompput',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie.heeftPompput',
                                          definition='Geeft aan of de vaste waterbouwkundige constructie een pompput heeft.',
                                          owner=self)

        self._heeftWoelkamer = OTLAttribuut(field=BooleanField,
                                            naam='heeftWoelkamer',
                                            label='heeft woelkamer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie.heeftWoelkamer',
                                            definition='Geeft aan of er al dan niet een woelkamer aanwezig is in de vaste waterbouwkundige constructie.',
                                            owner=self)

        self._typeNivelleringssysteem = OTLAttribuut(field=KlVWCTypeNivelleringssysteem,
                                                     naam='typeNivelleringssysteem',
                                                     label='type nivelleringssysteem',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie.typeNivelleringssysteem',
                                                     definition='Verwijst naar het type systeem dat gebruikt wordt voor de nivellering in vaste waterbouwkundige constructies.',
                                                     owner=self)

    @property
    def heeftPompput(self) -> bool:
        """Geeft aan of de vaste waterbouwkundige constructie een pompput heeft."""
        return self._heeftPompput.get_waarde()

    @heeftPompput.setter
    def heeftPompput(self, value):
        self._heeftPompput.set_waarde(value, owner=self)

    @property
    def heeftWoelkamer(self) -> bool:
        """Geeft aan of er al dan niet een woelkamer aanwezig is in de vaste waterbouwkundige constructie."""
        return self._heeftWoelkamer.get_waarde()

    @heeftWoelkamer.setter
    def heeftWoelkamer(self, value):
        self._heeftWoelkamer.set_waarde(value, owner=self)

    @property
    def typeNivelleringssysteem(self) -> str:
        """Verwijst naar het type systeem dat gebruikt wordt voor de nivellering in vaste waterbouwkundige constructies."""
        return self._typeNivelleringssysteem.get_waarde()

    @typeNivelleringssysteem.setter
    def typeNivelleringssysteem(self, value):
        self._typeNivelleringssysteem.set_waarde(value, owner=self)
