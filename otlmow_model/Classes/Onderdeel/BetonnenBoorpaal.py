# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.BetonnenConstructieElement import BetonnenConstructieElement
from otlmow_model.Classes.Onderdeel.Funderingspaal import Funderingspaal
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlUitvoeringswijzeBoorpaal import KlUitvoeringswijzeBoorpaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenBoorpaal(BetonnenConstructieElement, Funderingspaal):
    """Niet-grondverdringend betonnen funderingselement dat in de bodem kan worden aangebracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenBoorpaal'
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
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SecansTangenspalenwand')

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekennota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenBoorpaal.rekennota',
                                       definition='De rekennota van de boorpaal. Deze omvat o.a. het draagvermogen,... De rekennota wordt officieel afgetekend.',
                                       owner=self)

        self._uitvoeringswijze = OTLAttribuut(field=KlUitvoeringswijzeBoorpaal,
                                              naam='uitvoeringswijze',
                                              label='uitvoeringswijze',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenBoorpaal.uitvoeringswijze',
                                              definition='De manier waarop de boorpaal is uitgevoerd.',
                                              owner=self)

    @property
    def rekennota(self) -> DtcDocumentWaarden:
        """De rekennota van de boorpaal. Deze omvat o.a. het draagvermogen,... De rekennota wordt officieel afgetekend."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)

    @property
    def uitvoeringswijze(self) -> str:
        """De manier waarop de boorpaal is uitgevoerd."""
        return self._uitvoeringswijze.get_waarde()

    @uitvoeringswijze.setter
    def uitvoeringswijze(self, value):
        self._uitvoeringswijze.set_waarde(value, owner=self)
