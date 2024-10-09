# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInKilogram import KwantWrdInKilogram, KwantWrdInKilogramWaarden
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hijsinstallatie(AIMNaamObject, PuntGeometrie):
    """Het geheel van werktuig met aandrijving bestemd voor het verticaal verplaatsen van vrij zware lasten of componenten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schakelketting', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing

        self._hijskracht = OTLAttribuut(field=KwantWrdInKilogram,
                                        naam='hijskracht',
                                        label='hijskracht',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie.hijskracht',
                                        definition='De maximale hijskracht in kilogram waarvoor de hijsinstallatie gekeurd is.',
                                        owner=self)

        self._maximaalNiveauverschil = OTLAttribuut(field=KwantWrdInMeter,
                                                    naam='maximaalNiveauverschil',
                                                    label='maximaal niveauverschil',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hijsinstallatie.maximaalNiveauverschil',
                                                    definition='Het verticaal bereik van de hijsinstallatie.',
                                                    owner=self)

    @property
    def hijskracht(self) -> KwantWrdInKilogramWaarden:
        """De maximale hijskracht in kilogram waarvoor de hijsinstallatie gekeurd is."""
        return self._hijskracht.get_waarde()

    @hijskracht.setter
    def hijskracht(self, value):
        self._hijskracht.set_waarde(value, owner=self)

    @property
    def maximaalNiveauverschil(self) -> KwantWrdInMeterWaarden:
        """Het verticaal bereik van de hijsinstallatie."""
        return self._maximaalNiveauverschil.get_waarde()

    @maximaalNiveauverschil.setter
    def maximaalNiveauverschil(self, value):
        self._maximaalNiveauverschil.set_waarde(value, owner=self)
