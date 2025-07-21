import random

fruits = [
    "apple", "banana", "cherry", "orange", "grape",
    "pear", "kiwi", "mango", "papaya", "pineapple",
    "watermelon", "cantaloupe", "honeydew", "lemon", "lime",
    "grapefruit", "peach", "plum", "apricot", "nectarine",
    "pomegranate", "fig", "date", "coconut", "raspberry",
    "strawberry", "blueberry", "blackberry", "boysenberry", "currant",
    "gooseberry", "elderberry", "cranberry", "mulberry", "persimmon",
    "tangerine", "clementine", "mandarin", "kumquat", "lychee",
    "passionfruit", "dragonfruit", "starfruit", "guava", "jackfruit",
    "durian", "cherimoya", "rambutan", "longan", "sapote",
    "soursop", "feijoa", "jabuticaba", "ackee", "ugli fruit",
    "quince", "loquat", "olive", "miracle fruit", "salak",
    "tamarind", "breadfruit", "plantain", "avocado", "tomato",
    "carambola", "kiwano", "marionberry", "loganberry", "cloudberry",
    "aronia", "honeysuckle", "serviceberry", "chokeberry", "rowan",
    "bilberry", "yuzu", "pomelo", "satsuma", "calamansi",
    "bergamot", "finger lime", "makrut lime", "white currant", "red currant",
    "black currant", "maqui berry", "sea buckthorn", "medlar", "sugar apple",
    "osage orange", "prickly pear", "cactus pear", "dewberry", "jostaberry",
    "naranjilla", "lucuma", "canistel", "pepino", "horned melon",
]

if __name__ == "__main__":
    for fruit in random.sample(fruits, 5):
        print(fruit)
