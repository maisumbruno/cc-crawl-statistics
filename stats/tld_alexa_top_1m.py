# derived from
#   http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
# fetched 2017-10-18, see also
#   https://support.alexa.com/hc/en-us/sections/200063274-Top-Sites

alexa_top_1m_tlds_about = {
  'date': '2017-10-18',
  'source': 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
}

alexa_top_1m_tlds = {
  # zcat top-1m.csv.zip \
  #  | perl -ne 'chomp; s/.+\.//; $h{$_}++;
  #              END {
  #                for (sort { $h{$b} <=> $h{$a} } keys %h) {
  #                  print "\047", $_, "\047:", $h{$_}, ", ";
  #                }
  #              }' \
  #  | fold --width=70 -s | perl -lpe 's/^/  /; s/:/: /g; s/\s+$//'
  'com': 475915, 'net': 50051, 'ru': 50034, 'org': 47068, 'de': 24059,
  'jp': 22883, 'br': 16947, 'uk': 15213, 'it': 13970, 'cn': 13172,
  'ir': 12900, 'fr': 12692, 'in': 12477, 'pl': 10961, 'info': 9921,
  'es': 7514, 'au': 7163, 'ua': 6864, 'co': 6440, 'kr': 5964, 'gr': 5229,
  'io': 5144, 'cz': 5087, 'tw': 5057, 'nl': 4891, 'ca': 4863, 'eu': 4397,
  'me': 4274, 'tv': 4061, 'mx': 3810, 'us': 3718, 'se': 3430, 'id': 3401,
  'edu': 3283, 'ro': 3106, 'ch': 3006, 'be': 2937, 'hu': 2921, 'tr': 2901,
  'biz': 2900, 'za': 2735, 'at': 2717, 'xyz': 2690, 'ar': 2682, 'vn': 2611,
  'dk': 2373, 'no': 2325, 'sk': 2246, 'club': 2144, 'cc': 2077, 'pt': 1991,
  'fi': 1852, 'cl': 1699, 'hk': 1615, 'my': 1505, 'il': 1503, 'kz': 1442,
  'bid': 1426, 'pk': 1382, 'az': 1369, 'by': 1357, 'ie': 1313, 'pro': 1267,
  'online': 1236, 'th': 1171, 'nz': 1170, 'su': 1131, 'sg': 1095,
  'top': 1088, 'gov': 1060, 'bg': 1019, 'lt': 973, 'xn--p1ai': 959,
  'pe': 889, 'pw': 882, 'ng': 862, 'site': 808, 'ph': 796, 'hr': 758,
  'ae': 728, 'rs': 723, 'mobi': 666, 'si': 665, 'download': 650, 'lv': 644,
  'to': 627, 'win': 619, 'tk': 611, 've': 608, 'uz': 594, 'sa': 583,
  'ws': 527, 'lk': 488, 'space': 483, 'ee': 477, 'cat': 467, 'xxx': 464,
  'bd': 462, 'ma': 456, 'review': 456, 'website': 449, 'eg': 446,
  'asia': 423, 'fm': 414, 'ge': 393, 'is': 376, 'news': 364, 'life': 356,
  'am': 345, 'ec': 339, 'stream': 317, 'nu': 312, 'ga': 306, 'ml': 305,
  'tn': 304, 'today': 302, 'do': 297, 'lu': 278, 'link': 276, 'la': 262,
  'ke': 262, 'tokyo': 260, 'name': 240, 'uy': 235, 'live': 232, 'ao': 232,
  'mk': 227, 'trade': 225, 'tech': 218, 'date': 217, 'ly': 211, 'dz': 210,
  'ba': 209, 'guru': 208, 'qa': 208, 'im': 205, 'mn': 204, 'md': 203,
  'cf': 201, 'tz': 199, 'bz': 198, 'gdn': 197, 'media': 194, 'cr': 188,
  'travel': 185, 'gg': 185, 'ai': 183, 'cu': 177, 'al': 167, 'world': 166,
  'dev': 161, 'one': 160, 'kg': 155, 'jobs': 151, 'aero': 144, 'blog': 143,
  'tj': 143, 'video': 142, 'click': 142, 'gt': 138, 'cy': 136, 'bo': 135,
  'mm': 134, 'pa': 134, 'py': 133, 'kw': 131, 'cloud': 130, 'ug': 130,
  'shop': 126, 'np': 125, 'ag': 122, 'af': 121, 'rocks': 120, 'sd': 118,
  'coop': 117, 'sv': 115, 'moe': 110, 'int': 110, 'zone': 109, 'li': 109,
  'om': 108, 'vip': 107, 'store': 107, 'work': 107, 'gq': 106, 'sy': 105,
  'fun': 104, 'press': 103, 'network': 101, 'cm': 97, 'jo': 97, 'global': 93,
  'porn': 90, 'st': 90, 'sh': 88, 'lb': 88, 'wiki': 87, 'ac': 86, 'gh': 86,
  'ninja': 85, 'men': 85, 'mo': 84, 'so': 84, 'host': 83, 'eus': 83,
  'ovh': 83, 'et': 81, 'vc': 81, 'center': 81, 'red': 80, 'pics': 77,
  'ps': 77, 'sexy': 76, 'mu': 76, 'ni': 74, 'academy': 73, 'mz': 72, 'ci': 71,
  're': 68, 'cx': 68, 'tm': 67, 'zw': 67, 'ms': 66, 'plus': 65, 'iq': 65,
  'rw': 63, 'party': 63, 'cd': 63, 'hn': 61, 'kh': 61, 'mg': 60, 'bh': 60,
  'mil': 57, 'sc': 56, 'tips': 56, 'sn': 56, 'city': 56, 'ltd': 55,
  'design': 54, 'mt': 52, 'tools': 50, 'social': 49, 'tt': 49, 'help': 48,
  'expert': 47, 'digital': 46, 'services': 46, 'guide': 46, 'gs': 46,
  'bn': 46, 'education': 46, 'audio': 45, 'zm': 44, 'bt': 44, 'nyc': 43,
  'tf': 43, 'company': 42, 'bw': 42, 'bet': 40, 'community': 39, 'chat': 39,
  'watch': 39, 'ad': 38, 'cash': 38, 'lol': 38, 'pg': 37, 'agency': 37,
  'solutions': 37, 'wang': 36, 'bank': 36, 'cool': 36, 'land': 35, 'na': 34,
  'blue': 34, 'bf': 34, 'email': 34, 'games': 34, 'sx': 34, 'ink': 34,
  'pink': 33, 'gal': 32, 'bike': 32, 'movie': 32, 'love': 32, 'gratis': 31,
  'tc': 31, 'pub': 30, 'school': 30, 'pm': 30, 'london': 29, 'gl': 29,
  'loan': 29, 'market': 29, 'pr': 28, 'mw': 28, 'works': 28, 'sex': 28,
  'pf': 28, 'group': 28, 'photos': 27, 'team': 27, 'fo': 27, 'systems': 27,
  'technology': 27, 'webcam': 27, 'science': 26, 'money': 26, 'as': 26,
  'uno': 26, 'report': 26, 'tube': 26, 'app': 25, 'taipei': 25, 'paris': 25,
  'events': 25, 'tl': 25, 'exchange': 24, 'jm': 24, 'studio': 24, 'yt': 24,
  'codes': 23, 'accountant': 23, 'run': 23, 'support': 22, 'gd': 21,
  'nc': 21, 'berlin': 21, 'ye': 20, 'style': 20, 'xn--80asehdb': 20,
  'wtf': 20, 'fj': 20, 'istanbul': 20, 'bio': 20, 'software': 20,
  'xn--j1amh': 19, 'photo': 19, 'xin': 19, 'church': 19, 'directory': 19,
  'bm': 19, 'xn--6frz82g': 19, 'cam': 19, 'sm': 18, 'dating': 18, 'mv': 18,
  'deals': 18, 'bi': 18, 'moscow': 18, 'fyi': 18, 'bzh': 18, 'museum': 18,
  'buzz': 18, 'pet': 17, 'mr': 17, 'careers': 17, 'energy': 17, 'cafe': 17,
  'ht': 17, 'farm': 17, 'marketing': 17, 'hosting': 17, 'cv': 17,
  'coffee': 16, 'fit': 16, 'rip': 16, 'house': 16, 'dj': 16, 'training': 16,
  'black': 16, 'vg': 16, 'direct': 16, 'art': 15, 'xn--p1acf': 15, 'gy': 15,
  'town': 15, 'bj': 15, 'je': 15, 'express': 15, 'racing': 15, 'ooo': 14,
  'onl': 14, 'fund': 14, 'gallery': 14, 'capital': 14, 'brussels': 14,
  'camp': 14, 'nrw': 14, 'scot': 14, 'international': 14, 'game': 13,
  'graphics': 13, 'vu': 13, 'university': 13, 'va': 13, 'sr': 13, 'show': 13,
  'pictures': 13, 'dog': 13, 'earth': 13, 'fitness': 12, 'lc': 12,
  'faith': 12, 'foundation': 12, 'gi': 12, 'mc': 12, 'casino': 12,
  'cricket': 11, 'wien': 11, 'gold': 11, 'sale': 11, 'business': 11,
  'ren': 11, 'krd': 11, 'care': 11, 'film': 11, 'ls': 11, 'build': 11,
  'sl': 10, 'domains': 10, 'kiwi': 10, 'bs': 10, 'ne': 10, 'wales': 10,
  'nagoya': 10, 'reviews': 10, 'abbott': 10, 'tg': 10, 'institute': 10,
  'menu': 10, 'place': 10, 'partners': 9, 'how': 9, 'google': 9, 'ski': 9,
  'photography': 9, 'ngo': 9, 'ist': 9, 'vision': 9, 'kim': 9, 'wf': 9,
  'ax': 8, 'clinic': 8, 'okinawa': 8, 'cards': 8, 'sb': 8, 'leclerc': 8,
  'swiss': 8, 'rest': 8, 'bar': 8, 'lat': 8, 'koeln': 7, 'supply': 7, 'cw': 7,
  'nf': 7, 'post': 7, 'sz': 7, 'desi': 7, 'coach': 7, 'gn': 7, 'green': 7,
  'gm': 7, 'adult': 7, 'quebec': 7, 'delivery': 7, 'engineering': 7,
  'bnpparibas': 7, 'box': 7, 'xn--3e0b707e': 6, 'gift': 6, 'kp': 6,
  'finance': 6, 'clothing': 6, 'bible': 6, 'kitchen': 6, 'shoes': 6, 'ky': 6,
  'xn--d1acj3b': 6, 'fashion': 6, 'hamburg': 6, 'cymru': 6, 'amsterdam': 6,
  'mp': 6, 'cg': 6, 'xn--90ais': 6, 'parts': 6, 'auction': 6, 'rio': 6,
  'tel': 6, 'camera': 6, 'dance': 5, 'dm': 5, 'yokohama': 5, 'schule': 5,
  'jetzt': 5, 'recipes': 5, 'xn--80adxhks': 5, 'xn--80aswg': 5, 'toys': 5,
  'africa': 5, 'vegas': 5, 'discount': 5, 'xn--fiqs8s': 5, 'ventures': 5,
  'pizza': 5, 'td': 5, 'office': 5, 'barclays': 5, 'kyoto': 5, 'vet': 5,
  'ads': 5, 'shopping': 5, 'boutique': 5, 'football': 4, 'immo': 4,
  'xn--tckwe': 4, 'army': 4, 'college': 4, 'garden': 4, 'horse': 4,
  'management': 4, 'poker': 4, 'hockey': 4, 'builders': 4, 'mba': 4,
  'soy': 4, 'wine': 4, 'xn--c1avg': 4, 'nico': 4, 'bb': 4, 'singles': 4,
  'fail': 4, 'vlaanderen': 4, 'law': 4, 'repair': 4, 'estate': 3, 'kn': 3,
  'vin': 3, 'band': 3, 'prod': 3, 'coupons': 3, 'gop': 3, 'gf': 3, 'aws': 3,
  'rent': 3, 'bradesco': 3, 'cheap': 3, 'gp': 3, 'tienda': 3, 'melbourne': 3,
  'taxi': 3, 'barcelona': 3, 'promo': 3, 'limo': 3, 'futbol': 3, 'monash': 3,
  'ong': 3, 'fish': 3, 'aw': 3, 'cern': 3, 'diet': 3, 'saarland': 3,
  'pharmacy': 3, 'basketball': 3, 'solar': 3, 'tirol': 3, 'tickets': 3,
  'barclaycard': 3, 'casa': 3, 'moda': 3, 'orange': 3, 'rentals': 3,
  'equipment': 3, 'gifts': 3, 'cab': 3, 'vi': 3, 'golf': 3, 'eco': 3,
  'bayern': 3, 'hsbc': 3, 'sap': 3, 'hm': 3, 'doctor': 2, 'fans': 2, 'tax': 2,
  'sandvik': 2, 'lighting': 2, 'markets': 2, 'loans': 2, 'surf': 2,
  'claims': 2, 'reisen': 2, 'yandex': 2, 'computer': 2, 'apartments': 2,
  'fage': 2, 'car': 2, 'credit': 2, 'observer': 2, 'luxury': 2, 'sky': 2,
  'mq': 2, 'consulting': 2, 'xn--t60b56a': 2, 'jcb': 2, 'archi': 2,
  'osaka': 2, 'ryukyu': 2, 'hitachi': 2, 'lgbt': 2, 'hiphop': 2, 'tatar': 2,
  'restaurant': 2, 'best': 2, 'pictet': 2, 'kred': 2, 'gent': 2, 'citic': 2,
  'schmidt': 2, 'wedding': 2, 'bingo': 2, 'corsica': 2, 'canon': 2, 'pn': 2,
  'legal': 2, 'mortgage': 2, 'theater': 2, 'xn--mk1bu44c': 2,
  'investments': 2, 'exposed': 2, 'yoga': 2, 'vote': 2, 'nr': 2, 'cba': 2,
  'auto': 2, 'holiday': 2, 'audi': 2, 'realtor': 2, 'ceo': 2, 'flights': 2,
  'voyage': 2, 'engineer': 2, 'diamonds': 2, 'cars': 2, 'komatsu': 2,
  'tours': 2, 'axa': 2, 'sbi': 2, 'ck': 2, 'holdings': 1, 'weir': 1,
  'java': 1, 'gmail': 1, 'properties': 1, 'new': 1, 'pars': 1, 'cisco': 1,
  'associates': 1, 'vacations': 1, 'flowers': 1, 'career': 1, 'guitars': 1,
  'irish': 1, 'insure': 1, 'xn--ngbc5azd': 1, 'accountants': 1,
  'financial': 1, 'kinder': 1, 'ricoh': 1, 'jll': 1, 'sydney': 1,
  'cooking': 1, 'abb': 1, 'mma': 1, 'trading': 1, 'xn--h2brj9c': 1,
  'xn--pgbs0dh': 1, 'beer': 1, 'xn--vuq861b': 1, 'bargains': 1, 'lr': 1,
  'jewelry': 1, 'productions': 1, 'supplies': 1, 'soccer': 1, 'hot': 1,
  'creditcard': 1, 'dental': 1, 'neustar': 1, 'lease': 1, 'bms': 1,
  'sarl': 1, 'anz': 1, 'telefonica': 1, 'shiksha': 1, 'afl': 1, 'gmbh': 1,
  'youtube': 1, 'globo': 1, 'organic': 1, 'furniture': 1, 'vodka': 1,
  'miami': 1, 'sohu': 1, 'goog': 1, 'study': 1, 'ki': 1, 'docs': 1, 'spot': 1,
  'contractors': 1, 'haus': 1, 'fk': 1, 'juegos': 1, 'dhl': 1, 'trust': 1,
  'praxi': 1, 'bcn': 1, 'pioneer': 1, 'ismaili': 1, 'tattoo': 1, 'lidl': 1,
  'physio': 1, 'ltda': 1, 'forsale': 1, 'xn--mgbab2bd': 1, 'property': 1,
  'cologne': 1, 'uol': 1, 'aq': 1, 'yahoo': 1, 'fox': 1, 'xn--54b7fta0cc': 1,
  'fishing': 1, 'alsace': 1, 'gripe': 1, 'final': 1, 'kpn': 1, 'frl': 1,
  'cuisinella': 1, 'plumbing': 1, 'srl': 1, 'cfa': 1, 'you': 1, 'trv': 1,
  'navy': 1, 'nec': 1, 'vanguard': 1, 'xn--90ae': 1, 'gw': 1, 'sncf': 1,
  'saxo': 1, 'salon': 1, 'now': 1, 'xn--wgbl6a': 1, 'erni': 1,
}
