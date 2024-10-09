# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from ...Datatypes.KlOnderwaterkruisingAanlegWijze import KlOnderwaterkruisingAanlegWijze
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderwaterkruising(AbstracteAanvullendeGeometrie, LijnGeometrie):
    """Gebruikt voor de registratie van kenmerken en geometrie van een ruimte waar kabels en leidingen onder een waterweg door gaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Leiding', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel', direction='i')  # i = direction: incoming

        self._aanlegWijze = OTLAttribuut(field=KlOnderwaterkruisingAanlegWijze,
                                         naam='aanlegWijze',
                                         label='aanleg wijze',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising.aanlegWijze',
                                         definition='De manier waarop de onderwaterkruising gerealiseerd is volgens een vaste lijst met mogelijkheden.',
                                         owner=self)

        self._buitendiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='buitendiameter',
                                            label='buitendiameter',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising.buitendiameter',
                                            definition='De buitendiameter van de onderwaterkruising. Indien de kruising niet cirkelvormig is, gaat het hier om de diameter van de omgeschreven cirkel.',
                                            owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising.lengte',
                                    definition='De effectieve lengte van de onderwaterkruising, rekening houdend met eventuele curves en dus niet als projectie op een vlak.',
                                    owner=self)

    @property
    def aanlegWijze(self) -> str:
        """De manier waarop de onderwaterkruising gerealiseerd is volgens een vaste lijst met mogelijkheden."""
        return self._aanlegWijze.get_waarde()

    @aanlegWijze.setter
    def aanlegWijze(self, value):
        self._aanlegWijze.set_waarde(value, owner=self)

    @property
    def buitendiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitendiameter van de onderwaterkruising. Indien de kruising niet cirkelvormig is, gaat het hier om de diameter van de omgeschreven cirkel."""
        return self._buitendiameter.get_waarde()

    @buitendiameter.setter
    def buitendiameter(self, value):
        self._buitendiameter.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De effectieve lengte van de onderwaterkruising, rekening houdend met eventuele curves en dus niet als projectie op een vlak."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)
