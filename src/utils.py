capitals_brazil = [
    ("Rio Branco", "AC"),
    ("Maceió", "AL"),
    ("Macapá", "AP"),
    ("Manaus", "AM"),
    ("Salvador", "BA"),
    ("Fortaleza", "CE"),
    ("Brasília", "DF"),
    ("Vitória", "ES"),
    ("Goiânia", "GO"),
    ("São Luís", "MA"),
    ("Cuiabá", "MT"),
    ("Campo Grande", "MS"),
    ("Belo Horizonte", "MG"),
    ("Belém", "PA"),
    ("João Pessoa", "PB"),
    ("Curitiba", "PR"),
    ("Recife", "PE"),
    ("Teresina", "PI"),
    ("Rio de Janeiro", "RJ"),
    ("Natal", "RN"),
    ("Porto Alegre", "RS"),
    ("Porto Velho", "RO"),
    ("Boa Vista", "RR"),
    ("Florianópolis", "SC"),
    ("São Paulo", "SP"),
    ("Aracaju", "SE"),
    ("Palmas", "TO")
]

def moon_phase_case(value):
    if value == 0:
        return "New Moon"
    elif 0 < value < 0.25:
        return "Waxing Crescent"
    elif value == 0.25:
        return "First Quarter"
    elif 0.25 < value < 0.5:
        return "Waxing Gibbous"
    elif value == 0.5:
        return "Full Moon"
    elif 0.5 < value < 0.75:
        return "Waning Gibbous"
    elif value == 0.75:
        return "Last Quarter"
    elif 0.75 < value < 1:
        return "Waning Crescent"
    elif value == 1:
        return "New Moon"
    else:
        return "Unknown"