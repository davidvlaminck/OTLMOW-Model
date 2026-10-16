# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMeetprincipeDebietmeter import KlMeetprincipeDebietmeter
from ...Datatypes.KlMerkDebietmeter import KlMerkDebietmeter
from ...Datatypes.KlModelnaamDebietmeter import KlModelnaamDebietmeter
from ...Datatypes.KlMontagewijzeDebietmeter import KlMontagewijzeDebietmeter
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Debietmeter(AIMNaamObject, PuntGeometrie):
    """Een meettoestel voor het bepalen van de hoeveelheid vloeistof die per tijdseenheid door een leiding stroomt. De meter zet het meetresultaat om in een uitleesbaar signaal en/of stuurt dat signaal door naar de PLC."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Debietmeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', direction='u')  # u = unidirectional

        self._meetprincipe = OTLAttribuut(field=KlMeetprincipeDebietmeter,
                                          naam='meetprincipe',
                                          label='meetprincipe',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Debietmeter.meetprincipe',
                                          definition='Het fysische principe waarmee de debietmeter de doorstroming bepaalt.',
                                          owner=self)

        self._merk = OTLAttribuut(field=KlMerkDebietmeter,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Debietmeter.merk',
                                  definition='Het merk van de debietmeter.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlModelnaamDebietmeter,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Debietmeter.modelnaam',
                                       definition='De modelnaam/product range van de debietmeter.',
                                       owner=self)

        self._montagewijze = OTLAttribuut(field=KlMontagewijzeDebietmeter,
                                          naam='montagewijze',
                                          label='montagewijze',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Debietmeter.montagewijze',
                                          definition='De wijze waarop de debietmeter op de leiding is aangebracht, in de leiding opgenomen of op de buitenzijde ervan bevestigd.',
                                          owner=self)

    @property
    def meetprincipe(self) -> str:
        """Het fysische principe waarmee de debietmeter de doorstroming bepaalt."""
        return self._meetprincipe.get_waarde()

    @meetprincipe.setter
    def meetprincipe(self, value):
        self._meetprincipe.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de debietmeter."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van de debietmeter."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def montagewijze(self) -> str:
        """De wijze waarop de debietmeter op de leiding is aangebracht, in de leiding opgenomen of op de buitenzijde ervan bevestigd."""
        return self._montagewijze.get_waarde()

    @montagewijze.setter
    def montagewijze(self, value):
        self._montagewijze.set_waarde(value, owner=self)
