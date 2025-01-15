# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.Abstracten.AanhorigheidSluisStuw import AanhorigheidSluisStuw
from ...Classes.Abstracten.DetaiplanObject import DetaiplanObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAfwerkingstypeLeuning import KlAfwerkingstypeLeuning
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...Datatypes.KlVormLeuning import KlVormLeuning
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Leuning(AanhorighedenBrug, AanhorigheidKoker, AanhorigheidSluisStuw, DetaiplanObject, AIMNaamObject, LijnGeometrie):
    """Een leuning is een constructie waaraan men met een hand steun of stabiliteit kan vinden om niet in de diepte te vallen. Ze kan bestaan uit een stevige balk, strip of touw maar ook uit een boven- en onderregel en stijlen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Loopvloer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trap', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED', direction='u')  # u = unidirectional

        self._afwerkingstype = OTLAttribuut(field=KlAfwerkingstypeLeuning,
                                            naam='afwerkingstype',
                                            label='afwerkingstype',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.afwerkingstype',
                                            definition='Het type afwerking van de leuning.',
                                            owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.hoogte',
                                    definition='De hoogte van de leuning.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.lengte',
                                    definition='De lengte van de leuning.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.materiaal',
                                       definition='Het materiaal waaruit de leuning is vervaardigd.',
                                       owner=self)

        self._professioneelGebruik = OTLAttribuut(field=BooleanField,
                                                  naam='professioneelGebruik',
                                                  label='professioneel gebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.professioneelGebruik',
                                                  definition='Geeft aan of het gebruik enkel voor professionelen is of ook publiekeliGeeft aan of het gebruik enkel voor professionelen is of ook publiekelijk gebruikt wordt.',
                                                  owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.technischeFiche',
                                             definition='De technische fiche van de leuning.',
                                             owner=self)

        self._vorm = OTLAttribuut(field=KlVormLeuning,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning.vorm',
                                  definition='De vorm van de leuning',
                                  owner=self)

    @property
    def afwerkingstype(self) -> str:
        """Het type afwerking van de leuning."""
        return self._afwerkingstype.get_waarde()

    @afwerkingstype.setter
    def afwerkingstype(self, value):
        self._afwerkingstype.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte van de leuning."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de leuning."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de leuning is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def professioneelGebruik(self) -> bool:
        """Geeft aan of het gebruik enkel voor professionelen is of ook publiekeliGeeft aan of het gebruik enkel voor professionelen is of ook publiekelijk gebruikt wordt."""
        return self._professioneelGebruik.get_waarde()

    @professioneelGebruik.setter
    def professioneelGebruik(self, value):
        self._professioneelGebruik.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de leuning."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De vorm van de leuning"""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
