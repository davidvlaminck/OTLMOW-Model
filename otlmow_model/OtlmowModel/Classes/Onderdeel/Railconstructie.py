# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ...Datatypes.KlTypeBevestigingRail import KlTypeBevestigingRail
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Railconstructie(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Doorlopend metalen profiel met klemmen en tussenplaten waarop of waartegen iets rijdt of glijdt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', direction='o')  # o = direction: outgoing

        self._aantalVoegen = OTLAttribuut(field=IntegerField,
                                          naam='aantalVoegen',
                                          label='aantal voegen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.aantalVoegen',
                                          definition='Het aantal voegen.',
                                          owner=self)

        self._heeftLangsblokkeringrail = OTLAttribuut(field=BooleanField,
                                                      naam='heeftLangsblokkeringrail',
                                                      label='heeft langsblokkeringrail',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.heeftLangsblokkeringrail',
                                                      definition='Geeft aan of de rail langsblokkeringrail heeft of niet.',
                                                      owner=self)

        self._heeftOnderlegmat = OTLAttribuut(field=BooleanField,
                                              naam='heeftOnderlegmat',
                                              label='heeft onderlegmat',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.heeftOnderlegmat',
                                              definition='Geeft aan of de railconstructie een onderlegmat heeft.',
                                              owner=self)

        self._heeftTussenplaat = OTLAttribuut(field=BooleanField,
                                              naam='heeftTussenplaat',
                                              label='heeft tussenplaat',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.heeftTussenplaat',
                                              definition='Geeft aan of de railconstructie een tussenplaat heeft.',
                                              owner=self)

        self._heeftVoegen = OTLAttribuut(field=BooleanField,
                                         naam='heeftVoegen',
                                         label='heeft voegen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.heeftVoegen',
                                         definition='Geeft aan of de bovenrolwagen voegen heeft of niet.',
                                         owner=self)

        self._typeBevestiging = OTLAttribuut(field=KlTypeBevestigingRail,
                                             naam='typeBevestiging',
                                             label='type bevestiging rail',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.typeBevestiging',
                                             definition='Het type bevestiging van een rail.',
                                             owner=self)

        self._typeKlem = OTLAttribuut(field=StringField,
                                      naam='typeKlem',
                                      label='type klem',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie.typeKlem',
                                      definition='Het type klem gebruikt in de railconstructie.',
                                      owner=self)

    @property
    def aantalVoegen(self) -> int:
        """Het aantal voegen."""
        return self._aantalVoegen.get_waarde()

    @aantalVoegen.setter
    def aantalVoegen(self, value):
        self._aantalVoegen.set_waarde(value, owner=self)

    @property
    def heeftLangsblokkeringrail(self) -> bool:
        """Geeft aan of de rail langsblokkeringrail heeft of niet."""
        return self._heeftLangsblokkeringrail.get_waarde()

    @heeftLangsblokkeringrail.setter
    def heeftLangsblokkeringrail(self, value):
        self._heeftLangsblokkeringrail.set_waarde(value, owner=self)

    @property
    def heeftOnderlegmat(self) -> bool:
        """Geeft aan of de railconstructie een onderlegmat heeft."""
        return self._heeftOnderlegmat.get_waarde()

    @heeftOnderlegmat.setter
    def heeftOnderlegmat(self, value):
        self._heeftOnderlegmat.set_waarde(value, owner=self)

    @property
    def heeftTussenplaat(self) -> bool:
        """Geeft aan of de railconstructie een tussenplaat heeft."""
        return self._heeftTussenplaat.get_waarde()

    @heeftTussenplaat.setter
    def heeftTussenplaat(self, value):
        self._heeftTussenplaat.set_waarde(value, owner=self)

    @property
    def heeftVoegen(self) -> bool:
        """Geeft aan of de bovenrolwagen voegen heeft of niet."""
        return self._heeftVoegen.get_waarde()

    @heeftVoegen.setter
    def heeftVoegen(self, value):
        self._heeftVoegen.set_waarde(value, owner=self)

    @property
    def typeBevestiging(self) -> str:
        """Het type bevestiging van een rail."""
        return self._typeBevestiging.get_waarde()

    @typeBevestiging.setter
    def typeBevestiging(self, value):
        self._typeBevestiging.set_waarde(value, owner=self)

    @property
    def typeKlem(self) -> str:
        """Het type klem gebruikt in de railconstructie."""
        return self._typeKlem.get_waarde()

    @typeKlem.setter
    def typeKlem(self, value):
        self._typeKlem.set_waarde(value, owner=self)
