# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlAlgInspecteerbaarheid import KlAlgInspecteerbaarheid
from ...Datatypes.KlTypeBallast import KlTypeBallast
from ...Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ballastcompartiment(AIMNaamObject, VlakGeometrie):
    """Waterdichte ruimte in een beweegbare of tijdelijke waterkerende constructie alsook vlottende bolder gevuld met water en/of (pers)lucht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsluik', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsvoorziening', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BeweegbareWaterkerendeConstructie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie', direction='o')  # o = direction: outgoing

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.gewicht',
                                     definition='Het gewicht van de ballast uitgedrukt in ton.',
                                     owner=self)

        self._heeftOntluchtingsgat = OTLAttribuut(field=BooleanField,
                                                  naam='heeftOntluchtingsgat',
                                                  label='heeft ontluchtingsgat',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.heeftOntluchtingsgat',
                                                  definition='Geeft aan of er een ontluchtingsgat aanwezig is.',
                                                  owner=self)

        self._heeftPeilbuis = OTLAttribuut(field=BooleanField,
                                           naam='heeftPeilbuis',
                                           label='heeft peilbuis',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.heeftPeilbuis',
                                           definition='Geeft aan of er een peilbuis aanwezig is.',
                                           owner=self)

        self._isInspecteerbaar = OTLAttribuut(field=KlAlgInspecteerbaarheid,
                                              naam='isInspecteerbaar',
                                              label='is luchtkist of ballastcompartiment inspecteerbaar?',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.isInspecteerbaar',
                                              definition='Geeft de verschillende mogelijkheden aan om te weten of de luchtkisten of ballastcompartimenten inspecteerbaar zijn.',
                                              owner=self)

        self._isRegelbaar = OTLAttribuut(field=BooleanField,
                                         naam='isRegelbaar',
                                         label='is regelbaar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.isRegelbaar',
                                         definition='Geeft aan of de ballast regelbaar is of niet.',
                                         owner=self)

        self._typeBallast = OTLAttribuut(field=KlTypeBallast,
                                         naam='typeBallast',
                                         label='type ballast',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.typeBallast',
                                         definition='Het specifieke materiaal dat wordt gebruikt als ballast in het ballastcompartiment.',
                                         owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ballastcompartiment.volume',
                                    definition='Het maximale (te vullen) volume van de ballastcompartiment uitgedrukt in kubieke meter.',
                                    owner=self)

    @property
    def gewicht(self) -> KwantWrdInTonWaarden:
        """Het gewicht van de ballast uitgedrukt in ton."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def heeftOntluchtingsgat(self) -> bool:
        """Geeft aan of er een ontluchtingsgat aanwezig is."""
        return self._heeftOntluchtingsgat.get_waarde()

    @heeftOntluchtingsgat.setter
    def heeftOntluchtingsgat(self, value):
        self._heeftOntluchtingsgat.set_waarde(value, owner=self)

    @property
    def heeftPeilbuis(self) -> bool:
        """Geeft aan of er een peilbuis aanwezig is."""
        return self._heeftPeilbuis.get_waarde()

    @heeftPeilbuis.setter
    def heeftPeilbuis(self, value):
        self._heeftPeilbuis.set_waarde(value, owner=self)

    @property
    def isInspecteerbaar(self) -> str:
        """Geeft de verschillende mogelijkheden aan om te weten of de luchtkisten of ballastcompartimenten inspecteerbaar zijn."""
        return self._isInspecteerbaar.get_waarde()

    @isInspecteerbaar.setter
    def isInspecteerbaar(self, value):
        self._isInspecteerbaar.set_waarde(value, owner=self)

    @property
    def isRegelbaar(self) -> bool:
        """Geeft aan of de ballast regelbaar is of niet."""
        return self._isRegelbaar.get_waarde()

    @isRegelbaar.setter
    def isRegelbaar(self, value):
        self._isRegelbaar.set_waarde(value, owner=self)

    @property
    def typeBallast(self) -> str:
        """Het specifieke materiaal dat wordt gebruikt als ballast in het ballastcompartiment."""
        return self._typeBallast.get_waarde()

    @typeBallast.setter
    def typeBallast(self, value):
        self._typeBallast.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het maximale (te vullen) volume van de ballastcompartiment uitgedrukt in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
