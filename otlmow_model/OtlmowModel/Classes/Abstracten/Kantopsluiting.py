# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.LaagProductidentificatiecode import LaagProductidentificatiecode
from ...Classes.Abstracten.LijnvormigElement import LijnvormigElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcKrimpvoeg import DtcKrimpvoeg, DtcKrimpvoegWaarden
from ...Datatypes.KlLEKantopsluitingKleur import KlLEKantopsluitingKleur
from ...Datatypes.KlLEKantopsluitingSoort import KlLEKantopsluitingSoort
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kantopsluiting(LaagProductidentificatiecode, LijnvormigElement, LijnGeometrie):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties voor de kantopsluiting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ReflectorInLijnvormigElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGaafheid', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookAfw', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantAfw', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandAfw', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelAfw', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelAfw', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd', direction='o')  # o = direction: outgoing

        self._isGeprefabriceerd = OTLAttribuut(field=BooleanField,
                                               naam='isGeprefabriceerd',
                                               label='is geprefabriceerd',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.isGeprefabriceerd',
                                               definition='Aanduiding of de kantopsluiting al dan niet is geprefabriceerd.',
                                               owner=self)

        self._kleur = OTLAttribuut(field=KlLEKantopsluitingKleur,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.kleur',
                                   definition='De kleur van kantopsluiting.',
                                   owner=self)

        self._krimpvoeg = OTLAttribuut(field=DtcKrimpvoeg,
                                       naam='krimpvoeg',
                                       label='krimpvoeg',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.krimpvoeg',
                                       definition='Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat.',
                                       owner=self)

        self._leveringsbon = OTLAttribuut(field=DtcDocument,
                                          naam='leveringsbon',
                                          label='leveringsbon',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.leveringsbon',
                                          kardinaliteit_max='*',
                                          definition='Een bon die informatie bevat zoals : tijdstip aanmaak van het mengsel, tijdstip begin lossen van het mengsel, toevoegingen aan het mengsel, eventuele opmerkingen, vrachtgegevens (chauffeur, kentekenplaat, naam van de werf, ...)',
                                          owner=self)

        self._soort = OTLAttribuut(field=KlLEKantopsluitingSoort,
                                   naam='soort',
                                   label='soort',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.soort',
                                   definition='De soort van kantopsluiting.',
                                   owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kantopsluiting.totaleLengte',
                                          definition='De totale lengte van de geplaatste constructie van kantopsluitingen in meter.',
                                          owner=self)

    @property
    def isGeprefabriceerd(self) -> bool:
        """Aanduiding of de kantopsluiting al dan niet is geprefabriceerd."""
        return self._isGeprefabriceerd.get_waarde()

    @isGeprefabriceerd.setter
    def isGeprefabriceerd(self, value):
        self._isGeprefabriceerd.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van kantopsluiting."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def krimpvoeg(self) -> DtcKrimpvoegWaarden:
        """Een gedeeltelijke insnijding in een constructiedeel die uitzetting en krimp in de constructie toelaat."""
        return self._krimpvoeg.get_waarde()

    @krimpvoeg.setter
    def krimpvoeg(self, value):
        self._krimpvoeg.set_waarde(value, owner=self)

    @property
    def leveringsbon(self) -> List[DtcDocumentWaarden]:
        """Een bon die informatie bevat zoals : tijdstip aanmaak van het mengsel, tijdstip begin lossen van het mengsel, toevoegingen aan het mengsel, eventuele opmerkingen, vrachtgegevens (chauffeur, kentekenplaat, naam van de werf, ...)"""
        return self._leveringsbon.get_waarde()

    @leveringsbon.setter
    def leveringsbon(self, value):
        self._leveringsbon.set_waarde(value, owner=self)

    @property
    def soort(self) -> str:
        """De soort van kantopsluiting."""
        return self._soort.get_waarde()

    @soort.setter
    def soort(self, value):
        self._soort.set_waarde(value, owner=self)

    @property
    def totaleLengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de geplaatste constructie van kantopsluitingen in meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)
