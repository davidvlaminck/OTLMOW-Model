from otlmow_model.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar

if __name__ == "__main__":
    vr = Verkeersregelaar()
    vr.isActief = True
    vr.naam = 'VR'
    vr.toestand = 'in-gebruik'

    print(vr)
