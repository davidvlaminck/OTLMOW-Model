# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBrugdeel(KeuzelijstField):
    """Het soort brugdeel."""
    naam = 'KlTypeBrugdeel'
    label = 'Type brugdeel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeBrugdeel'
    definition = 'Het soort brugdeel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBrugdeel'
    options = {
        'baileybrug': KeuzelijstWaarde(invulwaarde='baileybrug',
                                       label='baileybrug',
                                       status='ingebruik',
                                       definitie='Deze brug is opgebouwd uit panelen die met elkaar verbonden worden.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/baileybrug'),
        'boogbrug': KeuzelijstWaarde(invulwaarde='boogbrug',
                                     label='boogbrug',
                                     status='ingebruik',
                                     definitie='Dit brugtype wordt toegepast voor overspanningen van 20 tot 200 meter. Een boogbrug heeft slechts 1 dragende hoofdcomponent: de boog. De landhoofden of funderingsmassief t. p. v. de booggeboortes worden meer belast.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/boogbrug'),
        'bowstringbrug': KeuzelijstWaarde(invulwaarde='bowstringbrug',
                                          label='bowstringbrug',
                                          status='ingebruik',
                                          definitie='Dit brugtype wordt toegepast voor overspanningen van 60 tot 200 meter. Een bowstringbrug bestaat uit twee hoofdcomponenten: de boog (bow) en een trekker (string). Deze brug kan geen spatkrachten uitoefenen op de funderingen en is in zijn geheel verplaatsbaar.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/bowstringbrug'),
        'hangbrug': KeuzelijstWaarde(invulwaarde='hangbrug',
                                     label='hangbrug',
                                     status='ingebruik',
                                     definitie='Dit brugtype wordt vooral toegepast bij de grootste overspanningen (van 500 tot meer dan 2000 meter). De brug vereist steeds twee hoge pijlers waarover twee zware draagkabels lopen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/hangbrug'),
        'liggerbrug-balk-en-met-constante-hoogte': KeuzelijstWaarde(invulwaarde='liggerbrug-balk-en-met-constante-hoogte',
                                                                    label='liggerbrug - balk(en) met constante hoogte',
                                                                    status='ingebruik',
                                                                    definitie='Een vaste brug met een plank, of meerdere planken met gelijke hoogtes, die het water of het land overspant. Onderaan de balken bevindt zich de wapening (passieve wapening of actieve voorspanwapening) die de trek opneemt, bovenaan bevindt zich de brugdekplaat die de druk opneemt. Ook balkbrug genoemd.',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/liggerbrug-balk-en-met-constante-hoogte'),
        'liggerbrug-balk-en-met-veranderlijke-hoogte': KeuzelijstWaarde(invulwaarde='liggerbrug-balk-en-met-veranderlijke-hoogte',
                                                                        label='liggerbrug - balk(en) met veranderlijke hoogte',
                                                                        status='ingebruik',
                                                                        definitie='Een vaste brug met een plank, of meerdere planken met verschillende hoogtes, die het water of het land overspant. Onderaan de balken bevindt zich de wapening (passieve wapening of actieve voorspanwapening) die de trek opneemt, bovenaan bevindt zich de brugdekplaat die de druk opneemt. Ook balkbrug genoemd.',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/liggerbrug-balk-en-met-veranderlijke-hoogte'),
        'liggerbrug-koker-s-met-constante-hoogte': KeuzelijstWaarde(invulwaarde='liggerbrug-koker-s-met-constante-hoogte',
                                                                    label='liggerbrug - koker(s) met constante hoogte',
                                                                    status='ingebruik',
                                                                    definitie='Een vaste brug waarbij het brugdek gevormd wordt met kokerliggers (enkelvoudige of meercellige). Ook caissonliggerbrug genoemd. Dit brugtype wordt vooral gebruikt om grote overspanningen te maken.',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/liggerbrug-koker-s-met-constante-hoogte'),
        'liggerbrug-koker-s-met-veranderlijke-hoogte': KeuzelijstWaarde(invulwaarde='liggerbrug-koker-s-met-veranderlijke-hoogte',
                                                                        label='liggerbrug - koker(s) met veranderlijke hoogte',
                                                                        status='ingebruik',
                                                                        definitie='Een vaste brug waarbij het brugdek gevormd wordt met kokerliggers (enkelvoudige of meercellige). Ook caissonliggerbrug genoemd. Dit brugtype wordt vooral gebruikt om grote overspanningen te maken. Boven de pijlers voorziet men een hoge zware doorsnede waardoor de doorsnede in het midden van de overspanning aanzienlijk lichter kan gemaakt worden. Dit zijn voornamelijk betonnen bruggen.',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/liggerbrug-koker-s-met-veranderlijke-hoogte'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='ingebruik',
                                        definitie='Het type brugdeel is onbekend.	',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/niet-gekend'),
        'plaatbrug': KeuzelijstWaarde(invulwaarde='plaatbrug',
                                      label='plaatbrug',
                                      status='ingebruik',
                                      definitie='Het brugdek wordt gevormd met een plaat.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/plaatbrug'),
        'portaalbrug-met-liggers': KeuzelijstWaarde(invulwaarde='portaalbrug-met-liggers',
                                                    label='portaalbrug met liggers',
                                                    status='ingebruik',
                                                    definitie='De bovenbouw is ter plaatse van de pijlers monoliet aan de onderbouw verbonden. Het horizontale deel bestaat uit liggers.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/portaalbrug-met-liggers'),
        'portaalbrug-met-plaat': KeuzelijstWaarde(invulwaarde='portaalbrug-met-plaat',
                                                  label='portaalbrug met plaat',
                                                  status='ingebruik',
                                                  definitie='De bovenbouw is ter plaatse van de pijlers monoliet aan de onderbouw verbonden. Het horizontale deel bestaat uit een plaat.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/portaalbrug-met-plaat'),
        'tuibrug': KeuzelijstWaarde(invulwaarde='tuibrug',
                                    label='tuibrug',
                                    status='ingebruik',
                                    definitie='Dit brugtype wordt toegepast voor overspanningen van 100 tot 500 meter (of soms ook meer). De trekkers (tuien) worden vanaf het brugdek rechtstreek naar de pijler geleid. De tuien kunnen in de pylonen verankerd worden of doorheen de pylonen geleid worden om in de volgende overspanning opnieuw in het brugdek verankerd te worden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/tuibrug'),
        'vakwerkbrug': KeuzelijstWaarde(invulwaarde='vakwerkbrug',
                                        label='vakwerkbrug',
                                        status='ingebruik',
                                        definitie='Een vakwerk bestaat uit een bovenregel en onderregel, die met elkaar verbonden zijn door schuine en rechte stijlen via de knopen. Beide hoofdliggers zijn bovenaan verbonden met een windverband.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/vakwerkbrug'),
        'vierendeelbrug': KeuzelijstWaarde(invulwaarde='vierendeelbrug',
                                           label='vierendeelbrug',
                                           status='ingebruik',
                                           definitie='Een vierendeelligger bestaat uit vierhoekige elementen. De knopen van de vierendeelbrug moeten in staat zijn om momenten op te nemen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdeel/vierendeelbrug')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

