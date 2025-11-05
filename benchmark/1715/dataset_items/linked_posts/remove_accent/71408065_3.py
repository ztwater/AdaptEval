examples = [
    ("hello, world", "hello, world"),
    ("42", "42"),
    ("你好，世界", "你好，世界"),
    (
        "Dès Noël, où un zéphyr haï me vêt de glaçons würmiens, je dîne d’exquis rôtis de bœuf au kir, à l’aÿ d’âge mûr, &cætera.",
        "des noel, ou un zephyr hai me vet de glacons wuermiens, je dine d’exquis rotis de boeuf au kir, a l’ay d’age mur, &caetera.",
    ),
    (
        "Falsches Üben von Xylophonmusik quält jeden größeren Zwerg.",
        "falsches ueben von xylophonmusik quaelt jeden groesseren zwerg.",
    ),
    (
        "Љубазни фењерџија чађавог лица хоће да ми покаже штос.",
        "љубазни фењерџија чађавог лица хоће да ми покаже штос.",
    ),
    (
        "Ljubazni fenjerdžija čađavog lica hoće da mi pokaže štos.",
        "ljubazni fenjerdzija cadavog lica hoce da mi pokaze stos.",
    ),
    (
        "Quizdeltagerne spiste jordbær med fløde, mens cirkusklovnen Walther spillede på xylofon.",
        "quizdeltagerne spiste jordbaer med flode, mens cirkusklovnen walther spillede pa xylofon.",
    ),
    (
        "Kæmi ný öxi hér ykist þjófum nú bæði víl og ádrepa.",
        "kaemi ny oexi her ykist þjofum nu baedi vil og adrepa.",
    ),
    (
        "Glāžšķūņa rūķīši dzērumā čiepj Baha koncertflīģeļu vākus.",
        "glazskuna rukisi dzeruma ciepj baha koncertfligelu vakus.",
    )
]

for (given, expected) in examples:
    assert remove_diacritics(given) == expected
