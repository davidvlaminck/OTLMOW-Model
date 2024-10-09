# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlBypassSchakelaarLocatie import KlBypassSchakelaarLocatie
from ...Datatypes.KlBypassSchakelaarMerk import KlBypassSchakelaarMerk
from ...Datatypes.KlBypassSchakelaarModelnaam import KlBypassSchakelaarModelnaam
from ...Datatypes.KlSchakelaarUitvoering import KlSchakelaarUitvoering
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BypassSchakelaar(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een schakelaar die toelaat om de stroomtoevoer naar afnemende technieken via het geschakeld toestel zoals een UPS, te omzeilen en te isoleren om veilig te kunnen werken aan dat toestel terwijl de stroomtoevoer voor afnemende technieken verzekerd blijft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BypassSchakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='u')  # u = unidirectional

        self._locatie = OTLAttribuut(field=KlBypassSchakelaarLocatie,
                                     naam='locatie',
                                     label='locatie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BypassSchakelaar.locatie',
                                     definition='De locatie van de bypasschakelaar geeft aan of deze zich op de UPS of op het laagspanningsbord bevindt.',
                                     owner=self)

        self._merk = OTLAttribuut(field=KlBypassSchakelaarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BypassSchakelaar.merk',
                                  definition='De merknaam van de schakelaar volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBypassSchakelaarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BypassSchakelaar.modelnaam',
                                       definition='De modelnaam van de bypass schakelaar volgens de fabrikant.',
                                       owner=self)

        self._uitvoering = OTLAttribuut(field=KlSchakelaarUitvoering,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BypassSchakelaar.uitvoering',
                                        definition='De uitvoering van de schakelaar.',
                                        owner=self)

    @property
    def locatie(self) -> str:
        """De locatie van de bypasschakelaar geeft aan of deze zich op de UPS of op het laagspanningsbord bevindt."""
        return self._locatie.get_waarde()

    @locatie.setter
    def locatie(self, value):
        self._locatie.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de schakelaar volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de bypass schakelaar volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def uitvoering(self) -> str:
        """De uitvoering van de schakelaar."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
