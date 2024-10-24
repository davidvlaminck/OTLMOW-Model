# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Put import Put
from ...Classes.Abstracten.PutRelatie import PutRelatie
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlHuisaansluitputMateriaal import KlHuisaansluitputMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Huisaansluitput(Put, PutRelatie, PuntGeometrie):
    """Het constructieonderdeel (putje of T-stuk) dat de verbinding vormt tussen de private riolering en de huisaansluiting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._aansluitingsfiche = OTLAttribuut(field=DtcDocument,
                                               naam='aansluitingsfiche',
                                               label='aansluitingsfiche',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.aansluitingsfiche',
                                               definition='De aansluitingsfiche van de huisaansluitput.',
                                               owner=self)

        self._heeftStankafsluiter = OTLAttribuut(field=BooleanField,
                                                 naam='heeftStankafsluiter',
                                                 label='heeft stankafsluiter',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.heeftStankafsluiter',
                                                 definition='Aanduiding of een huisaansluitput een stankafsluiter heeft of niet.',
                                                 owner=self)

        self._isInfiltrerend = OTLAttribuut(field=BooleanField,
                                            naam='isInfiltrerend',
                                            label='is infiltrerend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.isInfiltrerend',
                                            definition='Wanneer de wanden van het putje poreus zijn (en het putje dus infiltrerend is), kan een deel van het water het water dat in het putje komt rechtstreeks in de grond infiltreren.',
                                            owner=self)

        self._materiaal = OTLAttribuut(field=KlHuisaansluitputMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Huisaansluitput.materiaal',
                                       definition='Bepaalt het materiaal waaruit de huisaansluitput is vervaardigd.',
                                       owner=self)

    @property
    def aansluitingsfiche(self) -> DtcDocumentWaarden:
        """De aansluitingsfiche van de huisaansluitput."""
        return self._aansluitingsfiche.get_waarde()

    @aansluitingsfiche.setter
    def aansluitingsfiche(self, value):
        self._aansluitingsfiche.set_waarde(value, owner=self)

    @property
    def heeftStankafsluiter(self) -> bool:
        """Aanduiding of een huisaansluitput een stankafsluiter heeft of niet."""
        return self._heeftStankafsluiter.get_waarde()

    @heeftStankafsluiter.setter
    def heeftStankafsluiter(self, value):
        self._heeftStankafsluiter.set_waarde(value, owner=self)

    @property
    def isInfiltrerend(self) -> bool:
        """Wanneer de wanden van het putje poreus zijn (en het putje dus infiltrerend is), kan een deel van het water het water dat in het putje komt rechtstreeks in de grond infiltreren."""
        return self._isInfiltrerend.get_waarde()

    @isInfiltrerend.setter
    def isInfiltrerend(self, value):
        self._isInfiltrerend.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal waaruit de huisaansluitput is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
