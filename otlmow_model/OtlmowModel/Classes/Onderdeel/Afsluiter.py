# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlAfsluiterType import KlAfsluiterType
from ...Datatypes.KlTsklepAfsluiterMateriaal import KlTsklepAfsluiterMateriaal
from ...Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afsluiter(LinkendElement, PuntGeometrie):
    """Een afsluiter dient om leidingen, verbindingen of strengen van aan- en afvoer stelsels (bv. rioolstrengen) af te sluiten bij bv. gebreken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handwiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._actueleHoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                           naam='actueleHoogte',
                                           label='actuele hoogte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.actueleHoogte',
                                           definition='De afstand tussen het vloeipeil van de opening en de laagste positie van de schuif.',
                                           owner=self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.breedte',
                                     definition='De afstand tussen de uiterste zijden van de afsluiter in millimeter.',
                                     owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.hoogte',
                                    definition='De afstand tussen het hoogste en laagste punt van de afsluiter met uitzondering van de spindel in millimeter.',
                                    owner=self)

        self._isContinuRegelbaar = OTLAttribuut(field=BooleanField,
                                                naam='isContinuRegelbaar',
                                                label='is continu regelbaar',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.isContinuRegelbaar',
                                                definition='Geeft aan of de doorstroming vloeiend regelbaar is tussen de geheel gesloten stand (geen stroming) en de volledig geopende stand (maximale stroming).',
                                                owner=self)

        self._materiaal = OTLAttribuut(field=KlTsklepAfsluiterMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.materiaal',
                                       definition='Materiaal waaruit de afsluiter is vervaardigd.',
                                       owner=self)

        self._peil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                  naam='peil',
                                  label='peil',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.peil',
                                  definition='BOK-peil in meter-TAW van de onderkant van de doorlaat van de afsluiter.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlAfsluiterType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiter.type',
                                  definition='Bepaalt het type van de afsluiter.',
                                  owner=self)

    @property
    def actueleHoogte(self) -> KwantWrdInMillimeterWaarden:
        """De afstand tussen het vloeipeil van de opening en de laagste positie van de schuif."""
        return self._actueleHoogte.get_waarde()

    @actueleHoogte.setter
    def actueleHoogte(self, value):
        self._actueleHoogte.set_waarde(value, owner=self)

    @property
    def breedte(self) -> KwantWrdInMillimeterWaarden:
        """De afstand tussen de uiterste zijden van de afsluiter in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInMillimeterWaarden:
        """De afstand tussen het hoogste en laagste punt van de afsluiter met uitzondering van de spindel in millimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def isContinuRegelbaar(self) -> bool:
        """Geeft aan of de doorstroming vloeiend regelbaar is tussen de geheel gesloten stand (geen stroming) en de volledig geopende stand (maximale stroming)."""
        return self._isContinuRegelbaar.get_waarde()

    @isContinuRegelbaar.setter
    def isContinuRegelbaar(self, value):
        self._isContinuRegelbaar.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Materiaal waaruit de afsluiter is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def peil(self) -> KwantWrdInMeterTAWWaarden:
        """BOK-peil in meter-TAW van de onderkant van de doorlaat van de afsluiter."""
        return self._peil.get_waarde()

    @peil.setter
    def peil(self, value):
        self._peil.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Bepaalt het type van de afsluiter."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
