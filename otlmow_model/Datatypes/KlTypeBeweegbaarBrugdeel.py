# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBeweegbaarBrugdeel(KeuzelijstField):
    """Het type van het beweegbaar brugdeel."""
    naam = 'KlTypeBeweegbaarBrugdeel'
    label = 'Type beweegbaar brugdeel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeBeweegbaarBrugdeel'
    definition = 'Het type van het beweegbaar brugdeel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBeweegbaarBrugdeel'
    options = {
        'basculebrug': KeuzelijstWaarde(invulwaarde='basculebrug',
                                        label='Basculebrug',
                                        status='ingebruik',
                                        definitie='Brugdeel dat zich kan openen en sluiten door te draaien om het scharnierpunt, waar het brugdeel (ongeveer) in evenwicht is tussen het gewicht van het brugdek en dat van het contragewicht.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/basculebrug'),
        'draaibrug': KeuzelijstWaarde(invulwaarde='draaibrug',
                                      label='Draaibrug',
                                      status='ingebruik',
                                      definitie='Een brugdeel waarvan het beweegbare deel in een horizontaal vlak om een verticale as kan draaien. Een draaibrug kan gelijke of ongelijke armen hebben: de as waarrond het brugdeel draait, bevindt zich dan respectievelijk in het midden van of aan Ã©Ã©n zijde.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/draaibrug'),
        'geen-standaardtype': KeuzelijstWaarde(invulwaarde='geen-standaardtype',
                                               label='Geen standaardtype',
                                               status='ingebruik',
                                               definitie='Een brugdeel dat kan bewogen worden, maar niet kan beschreven worden door de andere termen. Vb.: een combinatie van bewegingsmethoden.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/geen-standaardtype'),
        'hefbrug': KeuzelijstWaarde(invulwaarde='hefbrug',
                                    label='Hefbrug',
                                    status='ingebruik',
                                    definitie='Een brugdeel waarvan het wegdek recht omhoog opgehesen wordt om de scheepvaart door te laten.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/hefbrug'),
        'helft-dubbele-basculebrug': KeuzelijstWaarde(invulwaarde='helft-dubbele-basculebrug',
                                                      label='Helft dubbele basculebrug',
                                                      status='ingebruik',
                                                      definitie='Bij een dubbele basculebrug hebben de brughelften slechts Ã©Ã©n vast steunpunt, het scharnierpunt. Wanneer het brugdeel gesloten wordt, worden de brughelften aan elkaar verbonden.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/helft-dubbele-basculebrug'),
        'klapbrug': KeuzelijstWaarde(invulwaarde='klapbrug',
                                     label='Klapbrug',
                                     status='ingebruik',
                                     definitie='Soort van basculebrug zonder contragewicht. Het voordeel van dergelijk brugdeel is dat deze minder plaats inneemt, maar het grote nadeel is dat er veel meer energie nodig is om de klapbrug te openen dan bij de volwaardige basculebrug. Daarom worden klapbruggen alleen bij kleine overspanningen gebruikt.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/klapbrug'),
        'ophaalbrug': KeuzelijstWaarde(invulwaarde='ophaalbrug',
                                       label='Ophaalbrug',
                                       status='ingebruik',
                                       definitie='Brugdeel waarvan het brugdek (ook wel de val of de klap genoemd) aan Ã©Ã©n kant scharnierend is opgehangen en aan de andere zijde door middel van een ketting of kabel opgehaald en naar beneden gelaten kan worden.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/ophaalbrug'),
        'pontonbrug': KeuzelijstWaarde(invulwaarde='pontonbrug',
                                       label='Pontonbrug',
                                       status='ingebruik',
                                       definitie='Een brugdeel naar een op het water drijvende ponton. Het brugdeel heeft een scharnier aan de ene kant en rolt aan de andere om toegang tot het ponton vanop de oever toe te laten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/pontonbrug'),
        'rolbasculebrug': KeuzelijstWaarde(invulwaarde='rolbasculebrug',
                                           label='Rolbasculebrug',
                                           status='ingebruik',
                                           definitie='Een brugdeel dat openklapt en rolt met een behulp van een contragewicht.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/rolbasculebrug'),
        'rolbrug': KeuzelijstWaarde(invulwaarde='rolbrug',
                                    label='Rolbrug',
                                    status='ingebruik',
                                    definitie='Een brugdeel dat op het land gerold wordt om het scheepvaartverkeer door te laten.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/rolbrug'),
        'straussbrug': KeuzelijstWaarde(invulwaarde='straussbrug',
                                        label='Straussbrug',
                                        status='ingebruik',
                                        definitie='Type basculebrug waarvan het tegengewicht zich boven het wegdek bevindt en die door drijfstangen geopend of gesloten wordt.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/straussbrug'),
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='Vast',
                                 status='ingebruik',
                                 definitie='Een brugdeel dat niet kan bewegen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweegbaarBrugdeel/vast')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

