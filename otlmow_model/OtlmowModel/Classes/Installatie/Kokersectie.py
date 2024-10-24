# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlBouwmethode import KlBouwmethode
from ...Datatypes.KlGebruikersType import KlGebruikersType
from ...Datatypes.KlTypeOndergrond import KlTypeOndergrond
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kokersectie(AIMObject, VlakGeometrie):
    """Een kokersectie is een deel van een serie elementen waaruit een kokercomplex is opgebouwd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidKoker', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balk', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HorizontaleConstructieplaat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Randprofiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ConstructieSokkel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Funderingspaal', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', direction='i')  # i = direction: incoming

        self._bouwmethode = OTLAttribuut(field=KlBouwmethode,
                                         naam='bouwmethode',
                                         label='bouwmethode',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie.bouwmethode',
                                         definition='Geeft een keuzelijst dat aangeeft hoe het koker element gebouwd en op zijn plek gezet is.',
                                         owner=self)

        self._gebruikersOnderSectie = OTLAttribuut(field=KlGebruikersType,
                                                   naam='gebruikersOnderSectie',
                                                   label='gebruikers onder sectie',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie.gebruikersOnderSectie',
                                                   definition='Geeft aan welk hoofdzakelijk type gebruikers er zich onder de sectie begeven.',
                                                   owner=self)

        self._gebruikersOpSectie = OTLAttribuut(field=KlGebruikersType,
                                                naam='gebruikersOpSectie',
                                                label='gebruikers op sectie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie.gebruikersOpSectie',
                                                definition='Geeft een keuzelijst van gebruikers dat kunnen voorkomen op de desbetreffende sectie.',
                                                owner=self)

        self._typeOndergrond = OTLAttribuut(field=KlTypeOndergrond,
                                            naam='typeOndergrond',
                                            label='type ondergrond',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie.typeOndergrond',
                                            definition='Geeft aan welke ondergrond er de desbetreffende sectie zit.',
                                            owner=self)

    @property
    def bouwmethode(self) -> str:
        """Geeft een keuzelijst dat aangeeft hoe het koker element gebouwd en op zijn plek gezet is."""
        return self._bouwmethode.get_waarde()

    @bouwmethode.setter
    def bouwmethode(self, value):
        self._bouwmethode.set_waarde(value, owner=self)

    @property
    def gebruikersOnderSectie(self) -> str:
        """Geeft aan welk hoofdzakelijk type gebruikers er zich onder de sectie begeven."""
        return self._gebruikersOnderSectie.get_waarde()

    @gebruikersOnderSectie.setter
    def gebruikersOnderSectie(self, value):
        self._gebruikersOnderSectie.set_waarde(value, owner=self)

    @property
    def gebruikersOpSectie(self) -> str:
        """Geeft een keuzelijst van gebruikers dat kunnen voorkomen op de desbetreffende sectie."""
        return self._gebruikersOpSectie.get_waarde()

    @gebruikersOpSectie.setter
    def gebruikersOpSectie(self, value):
        self._gebruikersOpSectie.set_waarde(value, owner=self)

    @property
    def typeOndergrond(self) -> str:
        """Geeft aan welke ondergrond er de desbetreffende sectie zit."""
        return self._typeOndergrond.get_waarde()

    @typeOndergrond.setter
    def typeOndergrond(self, value):
        self._typeOndergrond.set_waarde(value, owner=self)
