# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...Datatypes.KlZuilTGCMerk import KlZuilTGCMerk
from ...Datatypes.KlZuilTGCModelnaam import KlZuilTGCModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ZuilTGC(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een zuil om badgelezers en videofoonposten op te plaatsen. Deze bevinden zich typisch aan slagbomen of automatische poorten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera', direction='u', deprecated='2.9.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IntercomToestel', direction='u')  # u = unidirectional

        self._isGeschiktVoorPersonenvoertuigen = OTLAttribuut(field=BooleanField,
                                                              naam='isGeschiktVoorPersonenvoertuigen',
                                                              label='is geschikt voor personenvoertuigen',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC.isGeschiktVoorPersonenvoertuigen',
                                                              definition='Geeft aan of de zuil een hoogte heeft die het geschikt maakt om te worden benut door chauffeurs van personenvoertuigen. Doorgaans is de zuil dan ook geschikt voor voetgangers.',
                                                              owner=self)

        self._isGeschiktVoorVrachtwagens = OTLAttribuut(field=BooleanField,
                                                        naam='isGeschiktVoorVrachtwagens',
                                                        label='is geschikt voor vrachtwagens',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC.isGeschiktVoorVrachtwagens',
                                                        definition='Geeft aan of de zuil een hoogte heeft die het geschikt maakt om te worden benut door chauffeurs van vrachtwagens.',
                                                        owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC.materiaal',
                                       definition='Het materiaal waaruit de toegangscontrolezuil (voornamelijk) gemaakt is.',
                                       owner=self)

        self._merk = OTLAttribuut(field=KlZuilTGCMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC.merk',
                                  definition='Het merk van de zuil.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlZuilTGCModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC.modelnaam',
                                       definition='De modelnaam van de zuil.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC.technischeFiche',
                                             definition='Documentatie met bijkomende (technische) details van de toegangscontrolezuil.',
                                             owner=self)

    @property
    def isGeschiktVoorPersonenvoertuigen(self) -> bool:
        """Geeft aan of de zuil een hoogte heeft die het geschikt maakt om te worden benut door chauffeurs van personenvoertuigen. Doorgaans is de zuil dan ook geschikt voor voetgangers."""
        return self._isGeschiktVoorPersonenvoertuigen.get_waarde()

    @isGeschiktVoorPersonenvoertuigen.setter
    def isGeschiktVoorPersonenvoertuigen(self, value):
        self._isGeschiktVoorPersonenvoertuigen.set_waarde(value, owner=self)

    @property
    def isGeschiktVoorVrachtwagens(self) -> bool:
        """Geeft aan of de zuil een hoogte heeft die het geschikt maakt om te worden benut door chauffeurs van vrachtwagens."""
        return self._isGeschiktVoorVrachtwagens.get_waarde()

    @isGeschiktVoorVrachtwagens.setter
    def isGeschiktVoorVrachtwagens(self, value):
        self._isGeschiktVoorVrachtwagens.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de toegangscontrolezuil (voornamelijk) gemaakt is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de zuil."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de zuil."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Documentatie met bijkomende (technische) details van de toegangscontrolezuil."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
