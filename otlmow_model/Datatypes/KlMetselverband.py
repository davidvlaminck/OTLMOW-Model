# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMetselverband(KeuzelijstField):
    """De rangschikking waarin stenen worden gemetseld."""
    naam = 'KlMetselverband'
    label = 'Metselverband'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMetselverband'
    definition = 'De rangschikking waarin stenen worden gemetseld.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMetselverband'
    options = {
        'engels-verband': KeuzelijstWaarde(invulwaarde='engels-verband',
                                           label='Engels verband',
                                           status='ingebruik',
                                           definitie='Hierbij worden telkens drie strekken (lange zijde van de steen) met een kop (zijde van een steen die de kleinste oppervlakte heeft) afgewisseld. De koppen komen midden boven de middelste van de strekken van de laag eronder en erboven.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/engels-verband'),
        'halfsteenverband': KeuzelijstWaarde(invulwaarde='halfsteenverband',
                                             label='Halfsteenverband',
                                             status='ingebruik',
                                             definitie='Ook wel strekverband of Grieks verband genoemd. In dit verband ziet men enkel de lange zijden van de steen (strekken) en per laag wordt er telkens een halve steen versprongen. Op deze manier ontstaat een sterk verband, aangezien de stootvoegen maximaal verspringen.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/halfsteenverband'),
        'kettingverband': KeuzelijstWaarde(invulwaarde='kettingverband',
                                           label='Kettingverband',
                                           status='ingebruik',
                                           definitie='Ook wel Noor(d)s verband genoemd. Hierbij worden telkens twee strekken (lange zijde van de steen) met een kop (zijde van een steen die de kleinste oppervlakte heeft) afgewisseld. De koppen komen midden boven de stootvoegen tussen de twee strekken van de laag eronder en erboven.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/kettingverband'),
        'klezoorverband': KeuzelijstWaarde(invulwaarde='klezoorverband',
                                           label='Klezoorverband',
                                           status='ingebruik',
                                           definitie='In dit verband ziet men enkel de lange zijden van de steen (strekken). De lagen verspringen onderling slechts met 1 klezoor (1/4 steen). Het klezoorverband is een zwak verband omdat de stootvoegen in de verschillende lagen dicht bij elkaar liggen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/klezoorverband'),
        'koppenverband': KeuzelijstWaarde(invulwaarde='koppenverband',
                                          label='Koppenverband',
                                          status='ingebruik',
                                          definitie='Een koppen- of patijtsverband bestaat uit koppenlagen die onderling per laag een halve kop (zijde van een steen die de kleinste oppervlakte heeft) zijn versprongen. Dit verband is het meest geschikt voor gebogen muren.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/koppenverband'),
        'kruisverband': KeuzelijstWaarde(invulwaarde='kruisverband',
                                         label='Kruisverband',
                                         status='ingebruik',
                                         definitie='Ook Hollands verband genoemd. Hierbij worden koppenlagen (zijde van een steen die de kleinste oppervlakte heeft) met streklagen (lange zijde van de steen) afgewisseld. Het patroon herhaalt zich iedere vier lagen, waarbij door het verspringen een sterk verband ontstaat.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/kruisverband'),
        'staand-verband': KeuzelijstWaarde(invulwaarde='staand-verband',
                                           label='Staand verband',
                                           status='ingebruik',
                                           definitie='Hierbij worden koppenlagen (zijde van een steen die de kleinste oppervlakte heeft) met streklagen (lange zijde van de steen) afgewisseld. Het patroon herhaalt zich iedere twee lagen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/staand-verband'),
        'vlaams-verband': KeuzelijstWaarde(invulwaarde='vlaams-verband',
                                           label='Vlaams verband',
                                           status='ingebruik',
                                           definitie='Het Vlaams verband bestaat uit een afwisseling van koppen (zijde van een steen die de kleinste oppervlakte heeft) en strekken (lange zijde van de baksteen). De koppen liggen daarbij in het midden van de strekken van de laag eronder en erboven.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMetselverband/vlaams-verband')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

