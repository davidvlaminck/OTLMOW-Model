# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereLaag import AndereLaag
from ...Classes.Abstracten.LaagDikte import LaagDikte
from ...BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class DrukspreidendeConstructie(AndereLaag, LaagDikte):
    """Een ondergrondse constructieve laag, geplaatst tussen verharding en groeimedium of ondergrond (bv. doorwortelbare fundering), bedoeld om belastingen te spreiden, bodemverdichting te beperken en opdruk van de verharding door wortelgroei te voorkomen, meestal uitgevoerd met sandwichpanelen of gelijkaardige prefab-units."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DrukspreidendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', direction='i')  # i = direction: incoming

        self._heeftBoomkratsubstraat = OTLAttribuut(field=BooleanField,
                                                    naam='heeftBoomkratsubstraat',
                                                    label='heeft boomkratsubstraat',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DrukspreidendeConstructie.heeftBoomkratsubstraat',
                                                    definition='Duidt aan of de prefab-units al dan niet opgevuld zijn met boomkratsubstraat.',
                                                    owner=self)

    @property
    def heeftBoomkratsubstraat(self) -> bool:
        """Duidt aan of de prefab-units al dan niet opgevuld zijn met boomkratsubstraat."""
        return self._heeftBoomkratsubstraat.get_waarde()

    @heeftBoomkratsubstraat.setter
    def heeftBoomkratsubstraat(self, value):
        self._heeftBoomkratsubstraat.set_waarde(value, owner=self)
