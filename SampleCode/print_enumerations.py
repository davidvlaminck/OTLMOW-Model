from otlmow_model.OtlmowModel.Datatypes.KlWvLedOverhang import KlWvLedOverhang

if __name__ == "__main__":
    kl = KlWvLedOverhang
    for k, v in kl.options.items():
        if v.status == 'ingebruik':
            print(f'{v}\t{v.label}')