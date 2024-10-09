# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AfmetingenDiepCBWand import AfmetingenDiepCBWand
from ...Datatypes.DtcBetonspecificaties import DtcBetonspecificaties, DtcBetonspecificatiesWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Diepwand(AfmetingenDiepCBWand):
    """Paneelsgewijs opgebouwde wand, met behulp van specifieke graafmachines in de grond gevormd. Hierbij stabiliseert een steunvloeistof (meestal een bentonietsuspensie) de sleuf."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Diepwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._betonspecificaties = OTLAttribuut(field=DtcBetonspecificaties,
                                                naam='betonspecificaties',
                                                label='betonspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Diepwand.betonspecificaties',
                                                definition='Specificaties van het beton.',
                                                owner=self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekennota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Diepwand.rekennota',
                                       definition='Document dat berekeningen bijhoudt.',
                                       owner=self)

        self._wapeningsplan = OTLAttribuut(field=DtcDocument,
                                           naam='wapeningsplan',
                                           label='wapeningsplan',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Diepwand.wapeningsplan',
                                           definition='Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters).',
                                           owner=self)

    @property
    def betonspecificaties(self) -> DtcBetonspecificatiesWaarden:
        """Specificaties van het beton."""
        return self._betonspecificaties.get_waarde()

    @betonspecificaties.setter
    def betonspecificaties(self, value):
        self._betonspecificaties.set_waarde(value, owner=self)

    @property
    def rekennota(self) -> DtcDocumentWaarden:
        """Document dat berekeningen bijhoudt."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)

    @property
    def wapeningsplan(self) -> DtcDocumentWaarden:
        """Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters)."""
        return self._wapeningsplan.get_waarde()

    @wapeningsplan.setter
    def wapeningsplan(self, value):
        self._wapeningsplan.set_waarde(value, owner=self)
