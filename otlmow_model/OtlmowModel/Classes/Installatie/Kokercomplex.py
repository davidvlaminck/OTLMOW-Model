# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kokercomplex(AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een constructie met een gesloten doorsnede dat over de hele lengte doorloopt, continu ondersteund, bestaande uit 1 of meerdere kokers die 2 of meer locaties verbindt, met 1 of meerdere in- en uitgangen, ongeacht de toepassing."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij', direction='i')  # i = direction: incoming

        self._ligtFunderingInOpRandWaterweg = OTLAttribuut(field=BooleanField,
                                                           naam='ligtFunderingInOpRandWaterweg',
                                                           label='ligt fundering in of op de rand van de waterweg',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex.ligtFunderingInOpRandWaterweg',
                                                           usagenote='Attribuut uit gebruik sinds versie 2.11.0 ',
                                                           deprecated_version='2.11.0',
                                                           definition='Geeft aan of de fundering van het landhoofd in of op de rand van de waterweg ligt.',
                                                           owner=self)

        self._ligtFunderingsaanzetOnderBodem = OTLAttribuut(field=BooleanField,
                                                            naam='ligtFunderingsaanzetOnderBodem',
                                                            label='ligt funderingsaanzet onder de bodem',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex.ligtFunderingsaanzetOnderBodem',
                                                            usagenote='Attribuut uit gebruik sinds versie 2.11.0 ',
                                                            deprecated_version='2.11.0',
                                                            definition='Geeft aan of de funderingsaanzet al dan niet onder de bodem ligt.',
                                                            owner=self)

    @property
    def ligtFunderingInOpRandWaterweg(self) -> bool:
        """Geeft aan of de fundering van het landhoofd in of op de rand van de waterweg ligt."""
        return self._ligtFunderingInOpRandWaterweg.get_waarde()

    @ligtFunderingInOpRandWaterweg.setter
    def ligtFunderingInOpRandWaterweg(self, value):
        self._ligtFunderingInOpRandWaterweg.set_waarde(value, owner=self)

    @property
    def ligtFunderingsaanzetOnderBodem(self) -> bool:
        """Geeft aan of de funderingsaanzet al dan niet onder de bodem ligt."""
        return self._ligtFunderingsaanzetOnderBodem.get_waarde()

    @ligtFunderingsaanzetOnderBodem.setter
    def ligtFunderingsaanzetOnderBodem(self, value):
        self._ligtFunderingsaanzetOnderBodem.set_waarde(value, owner=self)
