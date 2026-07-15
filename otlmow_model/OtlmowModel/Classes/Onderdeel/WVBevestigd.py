# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.EMDraagconstructie import EMDraagconstructie
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcAfmetingBxlInMm import DtcAfmetingBxlInMm, DtcAfmetingBxlInMmWaarden
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVBevestigd(EMDraagconstructie, NaampadObject, PuntGeometrie):
    """Een draagconstructie,anders dan een WVLichtmast of WVConsole,waarbij verlichting (vlak) tegen een (tunnel)wand,bekleding … kan worden gehangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityAppurtenance', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WegverlichtingGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast', direction='i')  # i = direction: incoming

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd.afmeting',
                                      definition='De breedte en lengte van de montageplaat in millimeter.',
                                      owner=self)

        self._isDraaibaar = OTLAttribuut(field=BooleanField,
                                         naam='isDraaibaar',
                                         label='is draaibaar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd.isDraaibaar',
                                         definition='Aanduiding of de bevestiging onder een hoek ingesteld kan worden.',
                                         owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVBevestigd.materiaal',
                                       definition='Het materiaal waaruit de bevestiging bestaat.',
                                       owner=self)

    @property
    def afmeting(self) -> DtcAfmetingBxlInMmWaarden:
        """De breedte en lengte van de montageplaat in millimeter."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def isDraaibaar(self) -> bool:
        """Aanduiding of de bevestiging onder een hoek ingesteld kan worden."""
        return self._isDraaibaar.get_waarde()

    @isDraaibaar.setter
    def isDraaibaar(self, value):
        self._isDraaibaar.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de bevestiging bestaat."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
