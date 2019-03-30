from math import sqrt


def median(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n // 2]
    else:
        return sum(sorted(lst)[n // 2 - 1:n // 2 + 1]) / 2.0


def string_distance(*strings):
    def bag_of_letters(*tables):
        usable_characters = {}

        # make a master list of characters
        for tbl in tables:
            for char in tbl:
                usable_characters.setdefault(char, 0)

        # use the master list to set default key values for easy comparison
        for tbl in tables:
            for char in usable_characters:
                tbl.setdefault(char, 0)

        # use our master list as way to iterate through each character,
        # and
        for char in usable_characters:
            dif_squared = []
            dist = 0
            for enum, p in enumerate(tables):
                for q in tables[enum + 1:]:
                    dif_squared.append((p[char] - q[char]) ** 2)
                dist = sqrt(sum(dif_squared))
            usable_characters[char] = dist

        return usable_characters

    def char_freq_tbl(string):
        freq_tbl = {}
        for char in string:
            if char in freq_tbl:
                freq_tbl[char] += 1
            else:
                freq_tbl[char] = 1
        return freq_tbl

    character_freq_tables = []
    for s in strings:
        character_freq_tables.append(char_freq_tbl(s))

    char_distance_array = bag_of_letters(*character_freq_tables)
    return char_distance_array


str_a = 'joshuapfarinsaldfjkil.com'
str_b = 'josh   farina@gmail.com'
str_c = 'joshuap   ina@gmail.com'
str_d = 'the quick brown fox jumped over the lazy dog'

dist_dict = string_distance(str_a, str_b, str_c, str_d)

dist_list = [dist_dict[x] for x in dist_dict]

print(median(dist_list))
