# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.Abstracten.Voedingspunt import Voedingspunt
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcAfmetingBxhInMm import DtcAfmetingBxhInMm, DtcAfmetingBxhInMmWaarden
from ...Datatypes.KlBatterijMateriaal import KlBatterijMateriaal
from ...Datatypes.KlBatterijMerk import KlBatterijMerk
from ...Datatypes.KlBatterijModelnaam import KlBatterijModelnaam
from ...Datatypes.KwantWrdInAmpereUur import KwantWrdInAmpereUur, KwantWrdInAmpereUurWaarden
from ...Datatypes.KwantWrdInVolt import KwantWrdInVolt, KwantWrdInVoltWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Batterij(SerienummerObject, Voedingspunt, PuntGeometrie):
    """Element bestaande uit meerdere elektrochemische cellen voor het leveren van elektriciteit,die ontstaat door de omzetting van opgeslagen chemische energie in elektrische energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanningsomvormer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterijlader', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PMU', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel', direction='i')  # i = direction: incoming

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxhInMm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.afmetingen',
                                        definition='De afmetingen van de batterij in millimeter.',
                                        owner=self)

        self._fabricatiedatum = OTLAttribuut(field=DateField,
                                             naam='fabricatiedatum',
                                             label='fabricatiedatum',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.fabricatiedatum',
                                             definition='De datum waarop de batterij geproduceerd is.',
                                             owner=self)

        self._lading = OTLAttribuut(field=KwantWrdInAmpereUur,
                                    naam='lading',
                                    label='lading',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.lading',
                                    usagenote='Het gaat om de lading van de batterij vlak na productie wanneer de batterij volledig opgeladen is. De maximale lading dus.',
                                    definition='Wordt ook wel capaciteit of autonomie genoemd. Geeft aan hoe veel energie de batterij kan leveren in volledig opgeladen staat.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlBatterijMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.materiaal',
                                       definition='Het materiaal waaruit de batterij gemaakt is. Het gaat hier om het materiaal waarin de lading opgeslagen is.',
                                       owner=self)

        self._merk = OTLAttribuut(field=KlBatterijMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.merk',
                                  definition='Merk van de batterij.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBatterijModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.modelnaam',
                                       definition='Modelnaam van de batterij.',
                                       owner=self)

        self._spanning = OTLAttribuut(field=KwantWrdInVolt,
                                      naam='spanning',
                                      label='spanning',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.spanning',
                                      definition='De spanning die de batterij kan leveren. Wordt ook wel het werkingsvoltage genoemd.',
                                      owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxhInMmWaarden:
        """De afmetingen van de batterij in millimeter."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def fabricatiedatum(self) -> date:
        """De datum waarop de batterij geproduceerd is."""
        return self._fabricatiedatum.get_waarde()

    @fabricatiedatum.setter
    def fabricatiedatum(self, value):
        self._fabricatiedatum.set_waarde(value, owner=self)

    @property
    def lading(self) -> KwantWrdInAmpereUurWaarden:
        """Wordt ook wel capaciteit of autonomie genoemd. Geeft aan hoe veel energie de batterij kan leveren in volledig opgeladen staat."""
        return self._lading.get_waarde()

    @lading.setter
    def lading(self, value):
        self._lading.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de batterij gemaakt is. Het gaat hier om het materiaal waarin de lading opgeslagen is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merk van de batterij."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de batterij."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def spanning(self) -> KwantWrdInVoltWaarden:
        """De spanning die de batterij kan leveren. Wordt ook wel het werkingsvoltage genoemd."""
        return self._spanning.get_waarde()

    @spanning.setter
    def spanning(self, value):
        self._spanning.set_waarde(value, owner=self)
