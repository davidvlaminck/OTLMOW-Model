# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcZelfsluiterSluitkracht import DtcZelfsluiterSluitkracht, DtcZelfsluiterSluitkrachtWaarden
from ...Datatypes.KlZelfsluiterUitvoeringswijze import KlZelfsluiterUitvoeringswijze
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zelfsluiter(AIMNaamObject, PuntGeometrie):
    """Mechanisme voor oa. deuren en poorten dat er voor zorgt dat de gekoppelde deur of poort sluit zonder verdere tussenkomst."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zelfsluiter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', direction='u')  # u = unidirectional

        self._sluitkracht = OTLAttribuut(field=DtcZelfsluiterSluitkracht,
                                         naam='sluitkracht',
                                         label='sluitkracht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zelfsluiter.sluitkracht',
                                         definition='Geeft de mogelijkheden en instelling van het zelfsluitend mechanische aan.',
                                         owner=self)

        self._uitvoeringswijze = OTLAttribuut(field=KlZelfsluiterUitvoeringswijze,
                                              naam='uitvoeringswijze',
                                              label='uitvoeringswijze',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zelfsluiter.uitvoeringswijze',
                                              definition='Geeft de stand van de deursluiter in het dagelijks gebruik aan.',
                                              owner=self)

    @property
    def sluitkracht(self) -> DtcZelfsluiterSluitkrachtWaarden:
        """Geeft de mogelijkheden en instelling van het zelfsluitend mechanische aan."""
        return self._sluitkracht.get_waarde()

    @sluitkracht.setter
    def sluitkracht(self, value):
        self._sluitkracht.set_waarde(value, owner=self)

    @property
    def uitvoeringswijze(self) -> str:
        """Geeft de stand van de deursluiter in het dagelijks gebruik aan."""
        return self._uitvoeringswijze.get_waarde()

    @uitvoeringswijze.setter
    def uitvoeringswijze(self, value):
        self._uitvoeringswijze.set_waarde(value, owner=self)
