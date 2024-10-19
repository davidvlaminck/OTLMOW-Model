# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlGraadVanBeweegbaarheid import KlGraadVanBeweegbaarheid
from ...Datatypes.KlGraadVanStatischeBepaaldheid import KlGraadVanStatischeBepaaldheid
from ...Datatypes.KlMateriaalDragendeStructuurBrugdeel import KlMateriaalDragendeStructuurBrugdeel
from ...Datatypes.KlTypeBeweegbaarBrugdeel import KlTypeBeweegbaarBrugdeel
from ...Datatypes.KlTypeBrugdeel import KlTypeBrugdeel
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugdeel(AIMNaamObject, VlakGeometrie):
    """Het deel dat je kan wegnemen van een brug in zijn geheel. Dit kan ook meerdere overspanningen hebben. In het geval van beweegbare bruggen worden de onderdelen die de beweging mogelijk maken zoals balansarmen, tegengewicht, hameipoort,..etc ook gevat in het object brugdeel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorighedenBrug', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreerinrichting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stootblok', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Trillingsvoorziening', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balans', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Boog', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdek', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Damwand', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gewelf', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hameipoort', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hameistijl', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hanger', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Heftoren', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pyloon', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Randprofiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VakwerkElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Windverband', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagkabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RegelbaarTegengewicht', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VastTegengewicht', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vlotplaat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugballast', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij', direction='o')  # o = direction: outgoing

        self._aantalOverspanningen = OTLAttribuut(field=NonNegIntegerField,
                                                  naam='aantalOverspanningen',
                                                  label='aantal overspanningen',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.aantalOverspanningen',
                                                  definition='Aantal overspanningen, van oplegging naar volgende oplegging (bij een isostatisch brugdeel zal dit één overspanning zijn, bij een hyperstatisch brugdeel zijn dit er meerdere).',
                                                  owner=self)

        self._graadVanBeweegbaarheid = OTLAttribuut(field=KlGraadVanBeweegbaarheid,
                                                    naam='graadVanBeweegbaarheid',
                                                    label='graad van beweegbaarheid',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.graadVanBeweegbaarheid',
                                                    definition='De manier waarop het brugdeel beweegt.',
                                                    owner=self)

        self._graadVanStatischeBepaaldheid = OTLAttribuut(field=KlGraadVanStatischeBepaaldheid,
                                                          naam='graadVanStatischeBepaaldheid',
                                                          label='graad van statische bepaaldheid',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.graadVanStatischeBepaaldheid',
                                                          definition='Welke statische bepaaldheid het brugdeel heeft.',
                                                          owner=self)

        self._heeftVoorzieningNegatieveReactie = OTLAttribuut(field=BooleanField,
                                                              naam='heeftVoorzieningNegatieveReactie',
                                                              label='heeft voorziening negatieve reactie',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.heeftVoorzieningNegatieveReactie',
                                                              definition='Geeft aan of het brugdeel een voorziening negatieve reactie bevat, al dan niet.',
                                                              owner=self)

        self._individueleAfstandOverspanningen = OTLAttribuut(field=KwantWrdInMeter,
                                                              naam='individueleAfstandOverspanningen',
                                                              label='individuele afstand overspanningen',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.individueleAfstandOverspanningen',
                                                              kardinaliteit_max='*',
                                                              definition='De individuele afstand tussen opeenvolgende opleggingen, in meter. Dit wordt uitgedrukt gaande van LO naar RO, of in oplopende kilometerpunten. Er kunnen meerdere waarden mogelijk zijn (vb.: voor hyperstatische brugdelen).',
                                                              owner=self)

        self._materiaalDragendeStructuur = OTLAttribuut(field=KlMateriaalDragendeStructuurBrugdeel,
                                                        naam='materiaalDragendeStructuur',
                                                        label='materiaal dragende structuur',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.materiaalDragendeStructuur',
                                                        definition='Het materiaal van de dragende structuur van het brugdeel.',
                                                        owner=self)

        self._totaleBreedteBrugdeel = OTLAttribuut(field=KwantWrdInMeter,
                                                   naam='totaleBreedteBrugdeel',
                                                   label='totale breedte brugdeel',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleBreedteBrugdeel',
                                                   definition='De totale breedte van het brugdeel, uitgedrukt in meter.',
                                                   owner=self)

        self._totaleLengteBrugdeel = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='totaleLengteBrugdeel',
                                                  label='totale lengte brugdeel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleLengteBrugdeel',
                                                  definition='De totale lengte van voeg tot voeg van het brugdeel, uitgedrukt in meter.',
                                                  owner=self)

        self._totaleOppervlakteBrugdeel = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                                       naam='totaleOppervlakteBrugdeel',
                                                       label='totale oppervlakte brugdeel',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleOppervlakteBrugdeel',
                                                       definition='De totale oppervlakte van het gehele brugdeel (van hetzelfde type), uitgedrukt in vierkante meter.',
                                                       owner=self)

        self._totaleSpankracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                              naam='totaleSpankracht',
                                              label='totale spankracht',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleSpankracht',
                                              definition='De totale spankracht van het brugdeel, uitgedrukt in kiloNewton.',
                                              owner=self)

        self._typeBeweegbaarBrugdeel = OTLAttribuut(field=KlTypeBeweegbaarBrugdeel,
                                                    naam='typeBeweegbaarBrugdeel',
                                                    label='type beweegbaar brugdeel',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.typeBeweegbaarBrugdeel',
                                                    definition='Het type van het beweegbaar brugdeel.',
                                                    owner=self)

        self._typeBrugdeel = OTLAttribuut(field=KlTypeBrugdeel,
                                          naam='typeBrugdeel',
                                          label='type brugdeel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.typeBrugdeel',
                                          definition='Het type brugdeel.',
                                          owner=self)

    @property
    def aantalOverspanningen(self) -> int:
        """Aantal overspanningen, van oplegging naar volgende oplegging (bij een isostatisch brugdeel zal dit één overspanning zijn, bij een hyperstatisch brugdeel zijn dit er meerdere)."""
        return self._aantalOverspanningen.get_waarde()

    @aantalOverspanningen.setter
    def aantalOverspanningen(self, value):
        self._aantalOverspanningen.set_waarde(value, owner=self)

    @property
    def graadVanBeweegbaarheid(self) -> str:
        """De manier waarop het brugdeel beweegt."""
        return self._graadVanBeweegbaarheid.get_waarde()

    @graadVanBeweegbaarheid.setter
    def graadVanBeweegbaarheid(self, value):
        self._graadVanBeweegbaarheid.set_waarde(value, owner=self)

    @property
    def graadVanStatischeBepaaldheid(self) -> str:
        """Welke statische bepaaldheid het brugdeel heeft."""
        return self._graadVanStatischeBepaaldheid.get_waarde()

    @graadVanStatischeBepaaldheid.setter
    def graadVanStatischeBepaaldheid(self, value):
        self._graadVanStatischeBepaaldheid.set_waarde(value, owner=self)

    @property
    def heeftVoorzieningNegatieveReactie(self) -> bool:
        """Geeft aan of het brugdeel een voorziening negatieve reactie bevat, al dan niet."""
        return self._heeftVoorzieningNegatieveReactie.get_waarde()

    @heeftVoorzieningNegatieveReactie.setter
    def heeftVoorzieningNegatieveReactie(self, value):
        self._heeftVoorzieningNegatieveReactie.set_waarde(value, owner=self)

    @property
    def individueleAfstandOverspanningen(self) -> List[KwantWrdInMeterWaarden]:
        """De individuele afstand tussen opeenvolgende opleggingen, in meter. Dit wordt uitgedrukt gaande van LO naar RO, of in oplopende kilometerpunten. Er kunnen meerdere waarden mogelijk zijn (vb.: voor hyperstatische brugdelen)."""
        return self._individueleAfstandOverspanningen.get_waarde()

    @individueleAfstandOverspanningen.setter
    def individueleAfstandOverspanningen(self, value):
        self._individueleAfstandOverspanningen.set_waarde(value, owner=self)

    @property
    def materiaalDragendeStructuur(self) -> str:
        """Het materiaal van de dragende structuur van het brugdeel."""
        return self._materiaalDragendeStructuur.get_waarde()

    @materiaalDragendeStructuur.setter
    def materiaalDragendeStructuur(self, value):
        self._materiaalDragendeStructuur.set_waarde(value, owner=self)

    @property
    def totaleBreedteBrugdeel(self) -> KwantWrdInMeterWaarden:
        """De totale breedte van het brugdeel, uitgedrukt in meter."""
        return self._totaleBreedteBrugdeel.get_waarde()

    @totaleBreedteBrugdeel.setter
    def totaleBreedteBrugdeel(self, value):
        self._totaleBreedteBrugdeel.set_waarde(value, owner=self)

    @property
    def totaleLengteBrugdeel(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van voeg tot voeg van het brugdeel, uitgedrukt in meter."""
        return self._totaleLengteBrugdeel.get_waarde()

    @totaleLengteBrugdeel.setter
    def totaleLengteBrugdeel(self, value):
        self._totaleLengteBrugdeel.set_waarde(value, owner=self)

    @property
    def totaleOppervlakteBrugdeel(self) -> KwantWrdInVierkanteMeterWaarden:
        """De totale oppervlakte van het gehele brugdeel (van hetzelfde type), uitgedrukt in vierkante meter."""
        return self._totaleOppervlakteBrugdeel.get_waarde()

    @totaleOppervlakteBrugdeel.setter
    def totaleOppervlakteBrugdeel(self, value):
        self._totaleOppervlakteBrugdeel.set_waarde(value, owner=self)

    @property
    def totaleSpankracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De totale spankracht van het brugdeel, uitgedrukt in kiloNewton."""
        return self._totaleSpankracht.get_waarde()

    @totaleSpankracht.setter
    def totaleSpankracht(self, value):
        self._totaleSpankracht.set_waarde(value, owner=self)

    @property
    def typeBeweegbaarBrugdeel(self) -> str:
        """Het type van het beweegbaar brugdeel."""
        return self._typeBeweegbaarBrugdeel.get_waarde()

    @typeBeweegbaarBrugdeel.setter
    def typeBeweegbaarBrugdeel(self, value):
        self._typeBeweegbaarBrugdeel.set_waarde(value, owner=self)

    @property
    def typeBrugdeel(self) -> str:
        """Het type brugdeel."""
        return self._typeBrugdeel.get_waarde()

    @typeBrugdeel.setter
    def typeBrugdeel(self, value):
        self._typeBrugdeel.set_waarde(value, owner=self)
