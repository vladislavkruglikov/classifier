SEED = 0

RU_CHARS_LOWER = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
EN_CHARS_LOWER = set("abcdefghijklmnopqrstuvwxyz")

RU_CHAR_TO_AUGMENTED_CHARS = {
    "а": ["а", "a"],
    "и": ["и", "u"],
    "в": ["в", "8"],
    "с": ["с", "c"],
    "е": ["e", "е"],
    "к": ["к", "k"],
    "з": ["3", "з"],
    "р": ["р", "p"],
    "о": ["о", "o"],
    "ё": ["ё", "е"],
    "е": ["ё", "е"]
}

TENNIS_ITEMS = [
    "теннис(у|а|ы)?", "теннисист(а|ы|у)?", "теннисистк(а|у|ой)","корт(у|а|ы|ах|е)?",
    "atp", "wta", "US Open", "AUS(TRALIAN)? OPEN", "КУБОК ДЭВИСА", "Grand Slam",
    "кубок кремля", "КУБОК ФЕДЕРАЦИИ", "КУБОК ХОПМАНА",
    "новак(а|у|и)?", "ракетк(а|у|ой|и)", "libema open",
    "федерер", "уильямс", "надаль", "алькарас", "циньвэнь",
    "даниил медведев", "кудерметова", "блинкова", "ролан гаррос",
    "хаддад", "Циципас(ом|у)?", "Индиан Уэллс", "Богот(е)", "Мухова",
    "Младенович", "Пегула", "Большо(й|го) шлем(а)",
    "Контавейт", "ХАЛЕП", "Потапова",
    "УИМБЛДОН", "РОЛАН ГАРРОС", "рублев", "хачанов",
    "карацев", "Сафиуллин"
]

FOOTBALL_ITEMS = [
    "футбол(у|а|е)?","пенальти(ст|ам|у)?", "манчестер","зенит(у)?","роналд(у|о)?","цска","динамо",
    "фк","рпл","криштиану","псж","спартак(у|а)?","сити","арсенал(а|у)?","уефа","барселон(а|е)"
    "мадрид","ювентус","мбаппе","аршавин","ливерпул(ь|ю)",
    "тоттенхэм","бавария","бензема","ювентус","юфл","милан","фифа","дзюба","краснодар","дембеле",
    "шахтер","евро","хави","аякс","рфс","неймар" 
    "левандовски","монако","холанд"
]

BASKETBALL_ITEMS = [
    "(футбол(у|а|е)?|пенальти(ст|ам|у)?|уефа)",
    "(манчестер(а|у)?|зенит(а|у)?псж|сити|арсенал(а|у)?|барселона(е|у)?|мадрид(а)?|ювентус(а|у)?|фк" 
     "|ливерпул(ь|ю)?|тоттенхэм(а|у)?|бавари(я|и)?|ювентус(а|у)?|милан(а)?|краснодар(а|у)?|шахтер(а)?)",
    "(криштиан(о|у)?|мбаппе|аршавин(а|у)?|дзюб(а|е|у)|дембеле|хави|неймар(а|у)?|левандовски|холанд"
    "|акинфеев|онопко|кержаков(а|ы|у)?)",
    "(рпл|уефа|рфс|юфл)"
]

WINTER_SPORT_ITEMS = [
    "биатлон","евгениямедведева", "лыжи", "ibu", "fis", "шерегеш", "фигурное", "щербакова", "горнолыжный",
    "isu", "керлинг", "фигурное",'камила',
    "логинов", "валиева", "йоханнес", "плющенко", "ski", "ски", "лыжник", "фигурист",
    "трусова", "устюгов", "червоткин", "спицов",
    "снегоходные", "аксель"
]

VOLLEYBALL_ITEMS = [
    "волейбол(а|у|е|ьный|ьные)?","пляжка","пляжныйволейбол","волейбол(ист|истка)","волейболновости","волейболроссии",
    "вфв","новостиволейбола",
    "волейбольн(ые|ая|ую|ым)?","волейболсми","либеро","доигров(ка|щик|щица)","пляжн(ый|ые|ого|ому)","кетова"
]

HOCKEY_ITEMS = [
    "шайб(а|у|ы|ам)", "нхл", "кхл", "хокке(ист|исты|й|йный)", "хк", "стэнли", "овечкин(а|у)?",
    "кросби", "тамп(а|е|у)", "капризов(а|у)?","малкин(а|у)?", "питтсбург", "кучеров(а|у)?","радулов(а|у)?",
    "шипачев(а|у)?", "флери", "фхр", "грецки", "буллит(а|ы|ов)?", "пингвинз"
]

ATHLETICS_ITEMS = [
                    'бег(ун|уны|унья|а|овые|овой|ать|овые|овых)?', 'забег', 'легк(ая|ой)',
                   'делисьбегом', 'атлет(ы)?',
                   'всембег', 'атлетик(а|е|у)', 'легкаяатлетика',
                   'забег(и|е)',  'grut', 'шиповки', 'марафон(а|ы)?'
                   'высот(а|у|е|ы)','трейл', 'полумарафон(а|ы)?', 'rhr','офп','фитнес(а|е)?'
]

ESPORT_ITEMS = [
    "(cs|dota|valorant|csgo|go|кс|провалорант|валорант|pubgmobile|pubg|пабг|дот(а|е)|dota2|дот(а|е)2|steam|htlv)",
    "(navi|нави|g2|g2army|allezg2|faze|og|vp|вп|mouz|ence|eg|furia|big|forze|lgd|astralis|астралис|boom)",
    "(iem|major|rmr|blast|мейджор(а|ы|е)?|мажор(ы|е)?|pmgc(2021)?|esl|cybershoke|pgl"
    "|ti(10|11)?|pmpl(cis)?|epl|dpc|mycsgo|csgoup|fpl|d2cl|pglmajor)",
    "(m0nesy|симпл(у|а)?|s1mple|yekindar|b1t|smooya|ange1|бумыч)",
    "(скин(ы|ов)?|киберспорт(а|у|смен|смены)?|стрим(ы|а|мов|ер|еры|ера)?пк|разработчик(и)?|админ(а|ы)?"
    "|аккаунт(ы)?|монитор(ы)?|кейс(а|ы)?|клан(а|ы|у)?|ник|геймер(ы|ов)|клан(ы|ов|ами)|трайхард?|тиммейт(а|ов|ы)?)",
    "(awp|буст|молотов|overpass|ванвей|fissure|cмок(и)?|inferno)"
]

BOARDGAMES_ITEMS = [
    "(настол(ок|ка|ку|ки|ьщик|ьщиков)|настольн(ые|ых|ым|ая|ый|ой|ую)|настольныйфэшн|яжнастольщик"  
    "|настолокмногонебывает|гильдияразработчиковнастольныхигр|котнастолкин)",
    "(шахмат(ную|ные|ный|ная|ной|ы|ист|исты|ам|ами|истов|ах)?|warhammer(40k)?|задачишахматы|цитатышахматы|манчкин"
    "|тюльпаномания|аниме)",
    "(магнус(а|у)?|непомнящ(ему|ий)|кургинян|ян(я|у)?|хикар(а|у)|накамура|алехин(а)?|карлсен"
    "|каспаров(а|у)?|фишер(а|у)?)",
    "(шах|мат|фиде|гроссмейстер(ы|ам|ами|ов)?|мидгард|гамбит|ктулху|рыцар(ь|и|ей|ский)|комикс(ы)?)"
]

MOTOSPORT_ITEMS = [
'motogp','мотоцикл', 'мотогонки', 'yamaha','мото', 'moto3',
'мотоциклов', 'мотокроссу','mxgp', 'маркес', 'ama',
'мотоцикла',  'байк', 'сл2022', 'цтвс', 'vr46', 'mx2',
'квадроцикл',  'бастианини','зарко', 'маркеса', 'куартараро',
'франческо', 'дакар'
]

AUTOSPORT_ITEMS = [
       'гран', 'формулы', 'f1', 'nascar', 'дрифт', 'ferrari',
       'машины', 'tcr', 'ф1', 'трассе', 'формуле', 'red', 'fia', 'шарль',
       'феррари', 'машина', 'пилотов', 'макс', 'wec', 'гонок',
        'гонщик',  'льюис', 'ферстаппен', 'авто',
       'уик', 'формула', 'хэмилтон', 'алонсо',
       'автомобилей', 'ралли', 'автомобиль', 'риккардо', 'гасли',
       'автоспорт', 'рулем', 'машину', 'автоспорта',
        'ваз', 'автомобиля', 'гп', 'iwsc',  'шилка', 'haas',
       'машине', 'дрифту', 'монако', 'пит', 'bmw', 'пилота',
       'пилоты', 'smp', 'ле', 'vettel', 'пиастри',
       'болид', 'феттель', 'леклер', 'автомобили',
    'кими', 'монце', 'леклера', 'ред',
        'альпин', 'сво', 'валттери',
       'шарля', 'ферстаппена', 'энд', 'шумахер', 'wtcr',
       'uld', 'себастьян'
]

EXTREME_ITEMS = [
    'aftg', 'пересыла', 'безенги', 'прыжки',
       'matt', 'экстрим', 'bmx',
       'деки', 'паркур', 'прыжков',
       'вестсайда',  'rjs',
       'серф', 'zone23', 'горах', 'дек', 'гор', 'трюки', 'вестсайд',
       'прорайдер', 'велосипед', 'тар', 'дека',
       'гачи', 'деку', 'барбелл',
       'роупджампинг', 'высота', 'бордшорты', 'утопии', 'rad',
        'роуп', 'теплицы',
        'колеса', 'прыгнуть', 'хай', 'альпинизму', 'райдеров', 'фингерборд',
       'горы'
]

MARTIAL_ARTS_ITEMS = [
    'ufc', 'бой', 'боя', 'мма', 'бою', 'бокса', 'wwe',
       'боксу', 'емельяненко', 'бокс', 'боец', 'самбо', 'боев',
       'mma', 'драться', 'али', 'кудо', 'хабиб', 'бои',
       'поединок', 'нокаут', 'канело', 'макгрегор', 'петр', 'пояс',
       'бойцов', 'конор', 'поединка', 'ян', 'тони', 'шлеменко', 'каратэ',
       'усик', 'борьбе', 'ломаченко', 'удар', 'чимаев', 'aew',
       'джошуа', 'грудева',  'тайсон', 'магомед',
       'кикбоксингу',
       'фьюри', 'кард', 'брюс', 'боксеров',
       'хабиба', 'ринг', 'махачев', 'сенсей', 'ринге', 'боевых',
       'головкин', 'ниндзя', 'бойца',
       'дзюдо', 'оливейра', 'ислам', 'хамзат',
       'нокаутировал', 'майк', 'вольной', 'удары',
       'жекпе', 'удара', 'ударов', 'айкидо', 'магомедов', 'нурмагомедов',
       'udar', 'михаила', 'боксера',
       'лютый', 'кимоно',
       'единоборств'
]

CATEGORY_TO_ITEMS = {
    "tennis": TENNIS_ITEMS,
    "football": FOOTBALL_ITEMS,
    "basketball": BASKETBALL_ITEMS,
    "winter_sport": WINTER_SPORT_ITEMS,
    "volleyball": VOLLEYBALL_ITEMS,
    "hockey": HOCKEY_ITEMS,
    "athletics": ATHLETICS_ITEMS,
    "esport": ESPORT_ITEMS,
    "boardgames": BOARDGAMES_ITEMS,
    "motosport": MOTOSPORT_ITEMS,
    "autosport": AUTOSPORT_ITEMS,
    "extreme": EXTREME_ITEMS,
    "martial_arts": MARTIAL_ARTS_ITEMS
}
