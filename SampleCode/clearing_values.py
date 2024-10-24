from otlmow_model.OtlmowModel.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar
if __name__ == '__main__':
    vr = Verkeersregelaar()
    vr.notitie = 'Dit is een notitie'
    vr.toestand = 'in-gebruik'
    print(vr)

    print('\n')
    vr.clear_value('notitie')
    print(vr)

