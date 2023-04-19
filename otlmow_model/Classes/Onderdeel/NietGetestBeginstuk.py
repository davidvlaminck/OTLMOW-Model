# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Beginstuk import Beginstuk
from otlmow_model.Datatypes.KlLEACUitbuigingstype import KlLEACUitbuigingstype


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietGetestBeginstuk(Beginstuk):
    """Een niet-gecertificeerd begin aan een geleideconstructie, aan de stroomopwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank')

        self._uitbuigingstype = OTLAttribuut(field=KlLEACUitbuigingstype,
                                             naam='uitbuigingstype',
                                             label='uitbuigingstype',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk.uitbuigingstype',
                                             definition='Niet getest beginstuk dat uitbuigt weg van de weg in grondplan.',
                                             owner=self)

    @property
    def uitbuigingstype(self) -> str:
        """Niet getest beginstuk dat uitbuigt weg van de weg in grondplan."""
        return self._uitbuigingstype.get_waarde()

    @uitbuigingstype.setter
    def uitbuigingstype(self, value):
        self._uitbuigingstype.set_waarde(value, owner=self)
