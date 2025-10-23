# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StalenProfiel import StalenProfiel
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietStandaardStalenProfiel(StalenProfiel):
    """Een stalen constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. Niet-standaard stalen profiel omvat alle speciale,op maat gemaakte en/of niet vaak voorkomende profielen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MVPaal', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#StalenFunderingsprofiel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._detailDwarsdoorsnede = OTLAttribuut(field=DtcDocument,
                                                  naam='detailDwarsdoorsnede',
                                                  label='detail dwarsdoorsnede',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.detailDwarsdoorsnede',
                                                  definition='Details van de afmetingen en van de dwarsdoorsnedes.',
                                                  owner=self)

        self._profielbreedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='profielbreedte',
                                            label='profielbreedte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielbreedte',
                                            usagenote='Attribuut uit gebruik sinds versie 2.5.0 ',
                                            deprecated_version='2.5.0',
                                            definition='De korte afmeting in millimeter van het profiel.',
                                            owner=self)

        self._profielhoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='profielhoogte',
                                           label='profielhoogte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietStandaardStalenProfiel.profielhoogte',
                                           usagenote='Attribuut uit gebruik sinds versie 2.5.0 ',
                                           deprecated_version='2.5.0',
                                           definition='De langste afmeting in millimeter van het profiel.',
                                           owner=self)

    @property
    def detailDwarsdoorsnede(self) -> DtcDocumentWaarden:
        """Details van de afmetingen en van de dwarsdoorsnedes."""
        return self._detailDwarsdoorsnede.get_waarde()

    @detailDwarsdoorsnede.setter
    def detailDwarsdoorsnede(self, value):
        self._detailDwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def profielbreedte(self) -> KwantWrdInMillimeterWaarden:
        """De korte afmeting in millimeter van het profiel."""
        return self._profielbreedte.get_waarde()

    @profielbreedte.setter
    def profielbreedte(self, value):
        self._profielbreedte.set_waarde(value, owner=self)

    @property
    def profielhoogte(self) -> KwantWrdInMillimeterWaarden:
        """De langste afmeting in millimeter van het profiel."""
        return self._profielhoogte.get_waarde()

    @profielhoogte.setter
    def profielhoogte(self, value):
        self._profielhoogte.set_waarde(value, owner=self)
