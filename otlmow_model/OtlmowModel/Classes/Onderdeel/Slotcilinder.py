# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcMaatSlotcilinder import DtcMaatSlotcilinder, DtcMaatSlotcilinderWaarden
from ...Datatypes.KlSleutelplan import KlSleutelplan
from ...Datatypes.KlSlotcilinderBeveiligingsfactor import KlSlotcilinderBeveiligingsfactor
from ...Datatypes.KlSlotcilinderMerk import KlSlotcilinderMerk
from ...Datatypes.KlSlotcilinderModelnaam import KlSlotcilinderModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slotcilinder(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Onderdeel van het slotmechanisme waarin de sleutel wordt gestoken. Het slot kan enkel worden geopend door de juiste sleutel in de cilinder te steken en deze te draaien in de behuizing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot', direction='u')  # u = unidirectional

        self._beveiligingsfactor = OTLAttribuut(field=KlSlotcilinderBeveiligingsfactor,
                                                naam='beveiligingsfactor',
                                                label='beveiligingsfactor',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder.beveiligingsfactor',
                                                definition='Indicatie voor de inbraakweerstand.',
                                                owner=self)

        self._maat = OTLAttribuut(field=DtcMaatSlotcilinder,
                                  naam='maat',
                                  label='maat',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder.maat',
                                  definition='Geeft de maat van de cilinder langs beide kanten aan. Dit attribuut bestaat dan ook uit twee delen: de maat aan de binnenkant en de maat aan de buitenkant. Wordt ook wel centerafstand genoemd.',
                                  owner=self)

        self._merk = OTLAttribuut(field=KlSlotcilinderMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder.merk',
                                  definition='Het merk van de slotcilinder.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSlotcilinderModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder.modelnaam',
                                       definition='De modelnaam van de slotcilinder.',
                                       owner=self)

        self._sleutelplan = OTLAttribuut(field=KlSleutelplan,
                                         naam='sleutelplan',
                                         label='steutelplan',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slotcilinder.sleutelplan',
                                         definition='De sluetel die past op de slotcilinder.',
                                         owner=self)

    @property
    def beveiligingsfactor(self) -> str:
        """Indicatie voor de inbraakweerstand."""
        return self._beveiligingsfactor.get_waarde()

    @beveiligingsfactor.setter
    def beveiligingsfactor(self, value):
        self._beveiligingsfactor.set_waarde(value, owner=self)

    @property
    def maat(self) -> DtcMaatSlotcilinderWaarden:
        """Geeft de maat van de cilinder langs beide kanten aan. Dit attribuut bestaat dan ook uit twee delen: de maat aan de binnenkant en de maat aan de buitenkant. Wordt ook wel centerafstand genoemd."""
        return self._maat.get_waarde()

    @maat.setter
    def maat(self, value):
        self._maat.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de slotcilinder."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de slotcilinder."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def sleutelplan(self) -> str:
        """De sluetel die past op de slotcilinder."""
        return self._sleutelplan.get_waarde()

    @sleutelplan.setter
    def sleutelplan(self, value):
        self._sleutelplan.set_waarde(value, owner=self)
