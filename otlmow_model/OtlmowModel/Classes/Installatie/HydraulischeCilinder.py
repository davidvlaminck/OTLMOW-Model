# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInBar import KwantWrdInBar, KwantWrdInBarWaarden
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HydraulischeCilinder(AIMNaamObject, PuntGeometrie):
    """Hydraulisch aangedreven actuator waarbij de beweging wordt bewerkstelligd door een inwendige hydraulische druk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderzuiger', direction='i')  # i = direction: incoming

        self._heeftHijsogen = OTLAttribuut(field=BooleanField,
                                           naam='heeftHijsogen',
                                           label='heeft hijsogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.heeftHijsogen',
                                           definition='Geeft aan of de cilinder hijsogen heeft.',
                                           owner=self)

        self._heeftStandmeting = OTLAttribuut(field=BooleanField,
                                              naam='heeftStandmeting',
                                              label='heeft standmeting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.heeftStandmeting',
                                              definition='Geeft aan of de cilinder een inwendige standmeting heeft.',
                                              owner=self)

        self._heeftTegenstang = OTLAttribuut(field=BooleanField,
                                             naam='heeftTegenstang',
                                             label='heeft tegenstang',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.heeftTegenstang',
                                             definition="Geeft aan of de cilinder voorzien is van een tegenstang. In zo'n geval bevindt er zich een stang aan beide kanten van de zuiger.",
                                             owner=self)

        self._maximaleWerkdruk = OTLAttribuut(field=KwantWrdInBar,
                                              naam='maximaleWerkdruk',
                                              label='maximale werkdruk',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.maximaleWerkdruk',
                                              definition='De druk die overeenstemt met de maximale ijkingsdruk van de veiligheidskleppen; is gelijk aan 1,10 maal de grootste waarde van de nominale en van de uitzonderlijke druk.',
                                              owner=self)

        self._nominaleDruk = OTLAttribuut(field=KwantWrdInBar,
                                          naam='nominaleDruk',
                                          label='nominale druk',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.nominaleDruk',
                                          definition='De druk die overeenstemt met de nominale kracht.',
                                          owner=self)

        self._nominaleKracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                            naam='nominaleKracht',
                                            label='nominale kracht',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.nominaleKracht',
                                            definition='De kracht die overeenstemt met belastingsniveau 1, volgend uit de belastingscombinatie 1 van het SB270.',
                                            owner=self)

        self._proefdruk = OTLAttribuut(field=KwantWrdInBar,
                                       naam='proefdruk',
                                       label='proefdruk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HydraulischeCilinder.proefdruk',
                                       definition='De druk die gelijk is aan 1,50 maal de maximale werkdruk.',
                                       owner=self)

    @property
    def heeftHijsogen(self) -> bool:
        """Geeft aan of de cilinder hijsogen heeft."""
        return self._heeftHijsogen.get_waarde()

    @heeftHijsogen.setter
    def heeftHijsogen(self, value):
        self._heeftHijsogen.set_waarde(value, owner=self)

    @property
    def heeftStandmeting(self) -> bool:
        """Geeft aan of de cilinder een inwendige standmeting heeft."""
        return self._heeftStandmeting.get_waarde()

    @heeftStandmeting.setter
    def heeftStandmeting(self, value):
        self._heeftStandmeting.set_waarde(value, owner=self)

    @property
    def heeftTegenstang(self) -> bool:
        """Geeft aan of de cilinder voorzien is van een tegenstang. In zo'n geval bevindt er zich een stang aan beide kanten van de zuiger."""
        return self._heeftTegenstang.get_waarde()

    @heeftTegenstang.setter
    def heeftTegenstang(self, value):
        self._heeftTegenstang.set_waarde(value, owner=self)

    @property
    def maximaleWerkdruk(self) -> KwantWrdInBarWaarden:
        """De druk die overeenstemt met de maximale ijkingsdruk van de veiligheidskleppen; is gelijk aan 1,10 maal de grootste waarde van de nominale en van de uitzonderlijke druk."""
        return self._maximaleWerkdruk.get_waarde()

    @maximaleWerkdruk.setter
    def maximaleWerkdruk(self, value):
        self._maximaleWerkdruk.set_waarde(value, owner=self)

    @property
    def nominaleDruk(self) -> KwantWrdInBarWaarden:
        """De druk die overeenstemt met de nominale kracht."""
        return self._nominaleDruk.get_waarde()

    @nominaleDruk.setter
    def nominaleDruk(self, value):
        self._nominaleDruk.set_waarde(value, owner=self)

    @property
    def nominaleKracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De kracht die overeenstemt met belastingsniveau 1, volgend uit de belastingscombinatie 1 van het SB270."""
        return self._nominaleKracht.get_waarde()

    @nominaleKracht.setter
    def nominaleKracht(self, value):
        self._nominaleKracht.set_waarde(value, owner=self)

    @property
    def proefdruk(self) -> KwantWrdInBarWaarden:
        """De druk die gelijk is aan 1,50 maal de maximale werkdruk."""
        return self._proefdruk.get_waarde()

    @proefdruk.setter
    def proefdruk(self, value):
        self._proefdruk.set_waarde(value, owner=self)
