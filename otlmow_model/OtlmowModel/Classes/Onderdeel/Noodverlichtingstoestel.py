# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Binnenverlichtingstoestel import Binnenverlichtingstoestel
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlNominaleSpanning import KlNominaleSpanning
from ...Datatypes.KlNoodverlichtingTypeBatterij import KlNoodverlichtingTypeBatterij
from ...Datatypes.KwantWrdInMinuut import KwantWrdInMinuut, KwantWrdInMinuutWaarden
from ...Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Noodverlichtingstoestel(Binnenverlichtingstoestel):
    """Een verlichtingstoestel als combinatie van de lamp en de armatuur dat ingeschakeld is in een systeem voor noodverlichting en daarom moet voldoen aan bijkomende vereisten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalLampen = OTLAttribuut(field=NonNegIntegerField,
                                          naam='aantalLampen',
                                          label='aantal lampen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.aantalLampen',
                                          definition='Het aantal individueel vervangbare ampen in de armatuur van toestel.',
                                          owner=self)

        self._autonomie = OTLAttribuut(field=KwantWrdInMinuut,
                                       naam='autonomie',
                                       label='autonomie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.autonomie',
                                       definition='Geeft aan hoe lang de noodverlichting kan branden op de eigen batterij zonder voeding van een externe bron.',
                                       owner=self)

        self._getestViaAutomaat = OTLAttribuut(field=BooleanField,
                                               naam='getestViaAutomaat',
                                               label='getest via afleggen automaat',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.getestViaAutomaat',
                                               definition='Geeft aan of de werking van het noodverlichtingstoestel moet getest worden door het uitschakelen van de automaat waarlangs de netvoeding voor het toestel passeert.',
                                               owner=self)

        self._heeftAfstandsbewaking = OTLAttribuut(field=BooleanField,
                                                   naam='heeftAfstandsbewaking',
                                                   label='heeft afstandsbewaking',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.heeftAfstandsbewaking',
                                                   definition='Geeft aan of de correcte werking van het noodverlichtingstoestel al dan niet van op afstand bewaakt wordt.',
                                                   owner=self)

        self._spanning = OTLAttribuut(field=KlNominaleSpanning,
                                      naam='spanning',
                                      label='spanning',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.spanning',
                                      definition='De vereiste spanning voor (de lampen in) het verlichtingstoestel.',
                                      owner=self)

        self._typeBatterij = OTLAttribuut(field=KlNoodverlichtingTypeBatterij,
                                          naam='typeBatterij',
                                          label='type batterij',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.typeBatterij',
                                          definition='Typering van de batterij van een noodverlichtingstoestel.',
                                          owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodverlichtingstoestel.vermogen',
                                      definition='Geeft het gecombineerd vermogen in watt aan van alle lampen van het noodverlichtingstoestel.',
                                      owner=self)

    @property
    def aantalLampen(self) -> int:
        """Het aantal individueel vervangbare ampen in de armatuur van toestel."""
        return self._aantalLampen.get_waarde()

    @aantalLampen.setter
    def aantalLampen(self, value):
        self._aantalLampen.set_waarde(value, owner=self)

    @property
    def autonomie(self) -> KwantWrdInMinuutWaarden:
        """Geeft aan hoe lang de noodverlichting kan branden op de eigen batterij zonder voeding van een externe bron."""
        return self._autonomie.get_waarde()

    @autonomie.setter
    def autonomie(self, value):
        self._autonomie.set_waarde(value, owner=self)

    @property
    def getestViaAutomaat(self) -> bool:
        """Geeft aan of de werking van het noodverlichtingstoestel moet getest worden door het uitschakelen van de automaat waarlangs de netvoeding voor het toestel passeert."""
        return self._getestViaAutomaat.get_waarde()

    @getestViaAutomaat.setter
    def getestViaAutomaat(self, value):
        self._getestViaAutomaat.set_waarde(value, owner=self)

    @property
    def heeftAfstandsbewaking(self) -> bool:
        """Geeft aan of de correcte werking van het noodverlichtingstoestel al dan niet van op afstand bewaakt wordt."""
        return self._heeftAfstandsbewaking.get_waarde()

    @heeftAfstandsbewaking.setter
    def heeftAfstandsbewaking(self, value):
        self._heeftAfstandsbewaking.set_waarde(value, owner=self)

    @property
    def spanning(self) -> str:
        """De vereiste spanning voor (de lampen in) het verlichtingstoestel."""
        return self._spanning.get_waarde()

    @spanning.setter
    def spanning(self, value):
        self._spanning.set_waarde(value, owner=self)

    @property
    def typeBatterij(self) -> str:
        """Typering van de batterij van een noodverlichtingstoestel."""
        return self._typeBatterij.get_waarde()

    @typeBatterij.setter
    def typeBatterij(self, value):
        self._typeBatterij.set_waarde(value, owner=self)

    @property
    def vermogen(self) -> KwantWrdInWattWaarden:
        """Geeft het gecombineerd vermogen in watt aan van alle lampen van het noodverlichtingstoestel."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
