# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlPompGroepMerk import KlPompGroepMerk
from ...Datatypes.KlPompGroepModelnaam import KlPompGroepModelnaam
from ...Datatypes.KlPompSoort import KlPompSoort
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PompGroep(AIMNaamObject, PuntGeometrie):
    """Een systeem dat instaat voor het omzetten van elektrische energie in een verplaatsing of drukverhoging van water. In dit geval spreekt men van een pomp. In de omgekeerde situatie spreekt men van een turbine."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PompSchroefEnWaaier', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koppeling', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Overbrenging', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomphuis', direction='i')  # i = direction: incoming

        self._heeftIdentificatieplaat = OTLAttribuut(field=BooleanField,
                                                     naam='heeftIdentificatieplaat',
                                                     label='heeft identificatieplaat',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep.heeftIdentificatieplaat',
                                                     definition='Geeft aan of er ter plekke een identificatieplaat aanwezig is die het object identificeert en beschrijft.',
                                                     owner=self)

        self._kanTurbineren = OTLAttribuut(field=BooleanField,
                                           naam='kanTurbineren',
                                           label='kan turbineren',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep.kanTurbineren',
                                           definition='Geeft aan of de pompgroep ook gebruikt kan worden als turbine.',
                                           owner=self)

        self._merk = OTLAttribuut(field=KlPompGroepMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep.merk',
                                  definition='Het merk van de pompgroep.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPompGroepModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep.modelnaam',
                                       definition='De modelnaam van de pompgroep.',
                                       owner=self)

        self._soort = OTLAttribuut(field=KlPompSoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep.soort',
                                   definition='Bepaalt de aard van de pomp volgens haar werkingsprincipe.',
                                   owner=self)

    @property
    def heeftIdentificatieplaat(self) -> bool:
        """Geeft aan of er ter plekke een identificatieplaat aanwezig is die het object identificeert en beschrijft."""
        return self._heeftIdentificatieplaat.get_waarde()

    @heeftIdentificatieplaat.setter
    def heeftIdentificatieplaat(self, value):
        self._heeftIdentificatieplaat.set_waarde(value, owner=self)

    @property
    def kanTurbineren(self) -> bool:
        """Geeft aan of de pompgroep ook gebruikt kan worden als turbine."""
        return self._kanTurbineren.get_waarde()

    @kanTurbineren.setter
    def kanTurbineren(self, value):
        self._kanTurbineren.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de pompgroep."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de pompgroep."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def soort(self) -> str:
        """Bepaalt de aard van de pomp volgens haar werkingsprincipe."""
        return self._soort.get_waarde()

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)
