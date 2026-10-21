# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeAandrijvingTakel import KlTypeAandrijvingTakel
from ...Datatypes.KlTypeTakel import KlTypeTakel
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Takel(AIMNaamObject, PuntGeometrie):
    """Een hijsmiddel dat instaat voor het verticaal verplaatsen van een last via onder andere een staalkabel, ketting of hijsband."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DraagstructuurBWCTWC', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijspunt', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopkat', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HijsEnHefwerktuig', direction='o')  # o = direction: outgoing

        self._hijshoogte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='hijshoogte',
                                        label='hijshoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel.hijshoogte',
                                        definition='De maximale verticale afstand waarover een last door de takel kan worden verplaatst in meter.',
                                        owner=self)

        self._massa = OTLAttribuut(field=KwantWrdInTon,
                                   naam='massa',
                                   label='massa',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel.massa',
                                   definition='De massa van de takel als object, exclusief de hijslast, in ton.',
                                   owner=self)

        self._maximaleWerklast = OTLAttribuut(field=KwantWrdInKiloNewton,
                                              naam='maximaleWerklast',
                                              label='maximale werklast',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel.maximaleWerklast',
                                              definition='De maximaal toegelaten belasting die door de takel veilig kan worden gehesen in kilonewton.',
                                              owner=self)

        self._typeAandrijvingTakel = OTLAttribuut(field=KlTypeAandrijvingTakel,
                                                  naam='typeAandrijvingTakel',
                                                  label='type aandrijving takel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel.typeAandrijvingTakel',
                                                  definition='De aard van het mechanisme waarmee de takel wordt aangedreven om de hijsbeweging te realiseren.',
                                                  owner=self)

        self._typeTakel = OTLAttribuut(field=KlTypeTakel,
                                       naam='typeTakel',
                                       label='type takel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Takel.typeTakel',
                                       definition='De classificatie van de takel op basis van constructie en werkingsprincipe.',
                                       owner=self)

    @property
    def hijshoogte(self) -> KwantWrdInMeterWaarden:
        """De maximale verticale afstand waarover een last door de takel kan worden verplaatst in meter."""
        return self._hijshoogte.get_waarde()

    @hijshoogte.setter
    def hijshoogte(self, value):
        self._hijshoogte.set_waarde(value, owner=self)

    @property
    def massa(self) -> KwantWrdInTonWaarden:
        """De massa van de takel als object, exclusief de hijslast, in ton."""
        return self._massa.get_waarde()

    @massa.setter
    def massa(self, value):
        self._massa.set_waarde(value, owner=self)

    @property
    def maximaleWerklast(self) -> KwantWrdInKiloNewtonWaarden:
        """De maximaal toegelaten belasting die door de takel veilig kan worden gehesen in kilonewton."""
        return self._maximaleWerklast.get_waarde()

    @maximaleWerklast.setter
    def maximaleWerklast(self, value):
        self._maximaleWerklast.set_waarde(value, owner=self)

    @property
    def typeAandrijvingTakel(self) -> str:
        """De aard van het mechanisme waarmee de takel wordt aangedreven om de hijsbeweging te realiseren."""
        return self._typeAandrijvingTakel.get_waarde()

    @typeAandrijvingTakel.setter
    def typeAandrijvingTakel(self, value):
        self._typeAandrijvingTakel.set_waarde(value, owner=self)

    @property
    def typeTakel(self) -> str:
        """De classificatie van de takel op basis van constructie en werkingsprincipe."""
        return self._typeTakel.get_waarde()

    @typeTakel.setter
    def typeTakel(self, value):
        self._typeTakel.set_waarde(value, owner=self)
