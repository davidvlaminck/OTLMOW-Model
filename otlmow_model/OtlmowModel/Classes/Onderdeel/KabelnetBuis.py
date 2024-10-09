# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from otlmow_model.OtlmowModel.BaseClasses.URIField import URIField
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelnetBuis(AIMNaamObject, LijnGeometrie):
    """Koppeling met het corresponderend object in Kabelnet die toegang geeft tot de informatie die in Kabelnet bewaard wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftNetwerktoegang', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', direction='i')  # i = direction: incoming

        self._kabelnetBuisId = OTLAttribuut(field=IntegerField,
                                            naam='kabelnetBuisId',
                                            label='kabelnetbuis ID',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis.kabelnetBuisId',
                                            definition='Uniek nummer uit de Kabelnet toepassing dat de betrokken beschermbuis identificeert.',
                                            owner=self)

        self._kabelnetURL = OTLAttribuut(field=URIField,
                                         naam='kabelnetURL',
                                         label='kabelnet URL',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KabelnetBuis.kabelnetURL',
                                         definition='De URL waarmee het corresponderend object in Kabelnet rechtstreeks gevonden kan worden in de Kabelnet-toepassing.',
                                         owner=self)

    @property
    def kabelnetBuisId(self) -> int:
        """Uniek nummer uit de Kabelnet toepassing dat de betrokken beschermbuis identificeert."""
        return self._kabelnetBuisId.get_waarde()

    @kabelnetBuisId.setter
    def kabelnetBuisId(self, value):
        self._kabelnetBuisId.set_waarde(value, owner=self)

    @property
    def kabelnetURL(self) -> str:
        """De URL waarmee het corresponderend object in Kabelnet rechtstreeks gevonden kan worden in de Kabelnet-toepassing."""
        return self._kabelnetURL.get_waarde()

    @kabelnetURL.setter
    def kabelnetURL(self, value):
        self._kabelnetURL.set_waarde(value, owner=self)
