# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMarkeringsproduct(KeuzelijstField):
    """De mogelijke producten voor een markering."""
    naam = 'KlMarkeringsproduct'
    label = 'Markeringsproduct'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlMarkeringsproduct'
    definition = 'De mogelijke producten voor een markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMarkeringsproduct'
    options = {
        'koudplast': KeuzelijstWaarde(invulwaarde='koudplast',
                                      label='Koudplast',
                                      status='ingebruik',
                                      definitie='Een koudplast is een markeringssubstantie gevormd door de chemische reactie van 2 of meerdere componenten (minstens 1 verharder en 1 hoofdcomponent), waarvan geen oplosmiddelen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringsproduct/koudplast'),
        'thermoplast': KeuzelijstWaarde(invulwaarde='thermoplast',
                                        label='Thermoplast',
                                        status='ingebruik',
                                        definitie='Een thermoplast is een wegmarkeringsproduct zonder oplosmiddel. De substantie wordt door verwarming vloeibaar gemaakt en wordt manueel of mechanisch aangebracht met een geëigend apparaat of toestel. Door afkoeling wordt een geheel gevormd.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringsproduct/thermoplast'),
        'verf': KeuzelijstWaarde(invulwaarde='verf',
                                 label='Verf',
                                 status='ingebruik',
                                 definitie='Een vloeibaar product dat vaste stoffen zoals bindmiddel, stoffen die kleuren reflecteren, vulstoffen en additieven bevat. Dit in combinatie met een oplosmiddel, organisch of op basis van water. De verf wordt aangebracht met een borstel, rol of pistool en vormt een geheel door verdamping van het oplosmiddel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringsproduct/verf'),
        'voorgevormd-koudgekleefd': KeuzelijstWaarde(invulwaarde='voorgevormd-koudgekleefd',
                                                     label='Voorgevormd koudgekleefd',
                                                     status='ingebruik',
                                                     definitie='Deze markeringsproducten, vervaardigd in de fabriek, zijn voorzien van een kleefstrook en worden op het wegdek vastgedrukt (bv. tape). De eigenschappen worden niet noemenswaardig gewijzigd bij het aanbrengen. Naast de klassieke lijnmarkeringen worden voorgevormde markeringen ook gebruikt voor afbeeldingen op het wegdek.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringsproduct/voorgevormd-koudgekleefd'),
        'voorgevormd-warmgekleefd': KeuzelijstWaarde(invulwaarde='voorgevormd-warmgekleefd',
                                                     label='Voorgevormd warmgekleefd',
                                                     status='ingebruik',
                                                     definitie='Een warm gekleefde voorgevormde markering is een voorgevormd wegmarkeringsproduct dat gemaakt wordt aan de hand van een thermoplast. Het wordt aangebracht door het product te verwarmen tot zijn smelttemperatuur. Voorgevormde thermoplasten worden tijdens het aanbrengen met glasparels en / of stroefmakende middelen nagestrooid.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMarkeringsproduct/voorgevormd-warmgekleefd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

