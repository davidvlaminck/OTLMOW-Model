# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Communicatieapparatuur import Communicatieapparatuur
from ...Datatypes.KlAntenneConstructieType import KlAntenneConstructieType
from ...Datatypes.KlAntenneFrequentierange import KlAntenneFrequentierange
from ...Datatypes.KlAntenneMerk import KlAntenneMerk
from ...Datatypes.KlAntenneModelnaam import KlAntenneModelnaam
from ...Datatypes.KlAntenneUitvoeringsType import KlAntenneUitvoeringsType
from ...Datatypes.KwantWrdInDecimaleGraden import (
    KwantWrdInDecimaleGraden,
    KwantWrdInDecimaleGradenWaarden,
)
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Antenne(Communicatieapparatuur):
    """Toestel verbonden met een zender of ontvanger ten behoeve van het opvangen of verspreiden van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ASTRIDInstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#RadioheruitzendInstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._constructieType = OTLAttribuut(field=KlAntenneConstructieType,
                                             naam='constructieType',
                                             label='constructie type',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.constructieType',
                                             definition='Het constructie type of de vorm van de antenne, die mee de wijze van ophanging bepaalt.',
                                             owner=self)

        self._frequentierange = OTLAttribuut(field=KlAntenneFrequentierange,
                                             naam='frequentierange',
                                             label='frequentierange',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.frequentierange',
                                             definition='Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlAntenneMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.merk',
                                  definition='Het merk van de antenne.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAntenneModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.modelnaam',
                                       definition='De modelnaam/product range van een antenne.',
                                       owner=self)

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.opstelhoogte',
                                          definition='De opstelhoogte van de antenne t.o.v. het maaiveld.',
                                          owner=self)

        self._stralingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                           naam='stralingshoek',
                                           label='stralingshoek',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.stralingshoek',
                                           definition='Geeft aan over welke hoek de antenne signalen kan uitstralen en ontvangen.',
                                           owner=self)

        self._uitvoeringsType = OTLAttribuut(field=KlAntenneUitvoeringsType,
                                             naam='uitvoeringsType',
                                             label='uitvoeringstype',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.uitvoeringsType',
                                             definition='Het uitvoeringstype betreft de werkwijze van de antenne, die bepaalt onder welke richting(en) de antenne signaal uitstuurt en ontvangt.',
                                             owner=self)

    @property
    def constructieType(self) -> str:
        """Het constructie type of de vorm van de antenne, die mee de wijze van ophanging bepaalt."""
        return self._constructieType.get_waarde()

    @constructieType.setter
    def constructieType(self, value):
        self._constructieType.set_waarde(value, owner=self)

    @property
    def frequentierange(self) -> str:
        """Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden."""
        return self._frequentierange.get_waarde()

    @frequentierange.setter
    def frequentierange(self, value):
        self._frequentierange.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de antenne."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van een antenne."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """De opstelhoogte van de antenne t.o.v. het maaiveld."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)

    @property
    def stralingshoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """Geeft aan over welke hoek de antenne signalen kan uitstralen en ontvangen."""
        return self._stralingshoek.get_waarde()

    @stralingshoek.setter
    def stralingshoek(self, value):
        self._stralingshoek.set_waarde(value, owner=self)

    @property
    def uitvoeringsType(self) -> str:
        """Het uitvoeringstype betreft de werkwijze van de antenne, die bepaalt onder welke richting(en) de antenne signaal uitstuurt en ontvangt."""
        return self._uitvoeringsType.get_waarde()

    @uitvoeringsType.setter
    def uitvoeringsType(self, value):
        self._uitvoeringsType.set_waarde(value, owner=self)
