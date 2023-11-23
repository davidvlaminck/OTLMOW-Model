# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from ...Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlTypeCFAPaal import KlTypeCFAPaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class CFAPaal(BetonnenConstructieElement, Funderingspaal):
    """Ook: mortelschroefpaal. Het betreft een schroefpaal met continue schroefboor met holle stam."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CFAPaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel')

        self._heeftVoerbuis = OTLAttribuut(field=BooleanField,
                                           naam='heeftVoerbuis',
                                           label='heeft voerbuis',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CFAPaal.heeftVoerbuis',
                                           definition='Geeft aan of de CFA paal een voerbuis of niet heeft.',
                                           owner=self)

        self._typeCFAPaal = OTLAttribuut(field=KlTypeCFAPaal,
                                         naam='typeCFAPaal',
                                         label='type CFA paal',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CFAPaal.typeCFAPaal',
                                         definition='Keuzelijst om de uitvoering van de CFA paal aan te geven.',
                                         owner=self)

    @property
    def heeftVoerbuis(self) -> bool:
        """Geeft aan of de CFA paal een voerbuis of niet heeft."""
        return self._heeftVoerbuis.get_waarde()

    @heeftVoerbuis.setter
    def heeftVoerbuis(self, value):
        self._heeftVoerbuis.set_waarde(value, owner=self)

    @property
    def typeCFAPaal(self) -> str:
        """Keuzelijst om de uitvoering van de CFA paal aan te geven."""
        return self._typeCFAPaal.get_waarde()

    @typeCFAPaal.setter
    def typeCFAPaal(self, value):
        self._typeCFAPaal.set_waarde(value, owner=self)
