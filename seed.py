from app import create_app, db
from app.models.cat import Cat
from app.models.caretaker import Caretaker
from random import choice, choices, randrange, sample

NAMES = [
    "Leo",
    "Bella",
    "Milo",
    "Charlie",
    "Kitty",
    "Lucy",
    "Nala",
    "Simba",
    "Jack",
    "Loki",
    "Chloe",
    "Chloe",
    "Pepper",
    "Oreo",
    "Cleo",
    "Cleo",
    "Lola",
    "Willow",
    "Daisy",
    "Ollie",
    "Sophie",
    "Salem",
    "Tiger",
    "Binx",
    "Pumpkin",
    "Coco",
    "Penny",
    "Buddy",
    "Oscar",
    "Toby",
    "Rosie",
    "Frankie",
    "Boo",
    "Tigger",
    "Louie",
    "Mochi",
    "Midnight",
    "Lulu",
    "Boots",
    "Boots",
    "Ginger",
    "Baby",
    "Baby",
    "Piper",
    "Mittens",
    "Gus",
    "Gizmo",
    "Princess",
    "Peanut",
    "Maggie",
    "Lucky",
    "Rocky",
    "Sam",
    "Millie",
    "Bear",
    "Hazel",
    "Teddy",
    "Ruby",
    "Ash",
    "Jax",
    "Scout",
    "Minnie",
    "Abby",
    "Abby",
    "Sunny",
    "Belle",
    "Marley",
    "Marley",
    "Thor",
    "Frank",
    "Joey",
    "Moose",
    "Moose",
    "Emma",
    "Murphy",
    "Romeo",
    "Riley",
    "Tucker",
    "Bagheera",
    "Olivia",
    "Neko",
    "Jackson",
    "Calvin",
    "Clyde",
]

COLORS = [
    "White",
    "Black",
    "Red",
    "Ginger",
    "Blue",
    "Grey",
    "Cream",
    "Brown",
    "Cinnamon",
    "Fawn",
    "Striped tabby",
    "Mackerel tabby",
    "Classic tabby",
    "Blotched tabby",
    "Spotted tabby",
    "Ticked tabby",
    "Tortoiseshell",
    "Calico",
]

PERSONALITIES = [
    "Skittish",
    "Outgoing",
    "Confident",
    "Spontaneous",
    "Impulsive",
    "Friendly",
    "Adventurous",
    "Relaxed",
    "Gentle",
    "Playful",
    "Affectionate",
    "Curious",
    "Peaceful",
    "Docile",
    "Sweet",
    "Active",
    "Sociable",
    "Purposeful",
    "Talkative",
    "Determined",
    "Vocal",
    "Loving",
    "Inquisitive",
]

CARETAKERS = [
    "Reina Williams",
    "Reid Mack",
    "Deborah Meyer",
    "Kaitlyn Suarez",
    "Karissa Schmitt",
    "Jaliyah Cisneros",
    "Laurel Bishop",
    "Issac Nguyen",
    "Beatrice Russo",
    "Conner Silva",
    "Kaiya Duncan",
    "Mikaela Chung",
    "Kaleigh Barnes",
    "Carlos Martinez",
    "Pedro Mcguire",
    "Angelica Sanford",
    "Rylee Johnson",
    "Jovani Hahn",
    "Charlotte Huffman",
    "Brendan Valentine",
    "Danna Delgado",
    "Silas Flowers",
    "Antoine Boone",
    "Walter Mercer",
    "Maxim Davila",
    "Devin Tyler",
    "Kolton Bullock",
    "Jordon Tucker",
    "Jadiel Shepherd",
    "Lexie Dalton",
    "Chana Parker",
    "Shyla Matthews",
    "Tristin Steele",
    "Leticia Graves",
    "Semaj Jimenez",
    "Trey Paul",
    "Jorge Franklin",
    "Payten Nicholson",
    "Dahlia Snyder",
    "Ben Cooper",
    "Kareem Madden",
    "Jayla Lang",
    "Brisa Hanna",
    "Ashton Jensen",
    "Ian Farmer",
    "Henry Watkins",
    "Marvin Hebert",
    "Gauge Glover",
    "Kelsey Holden",
    "Kendal Beard",
    "Claudia Rios",
    "Jaidyn Skinner",
    "Freddy Harrell",
    "Sonia Zuniga",
    "River Dean",
    "Jaquan Hebert",
    "Vanessa Christian",
    "Leticia Larson",
    "Tate Oconnell",
    "Juliette Garza",
    "Micaela Trevino",
    "Javion Lowery",
    "Mckinley Braun",
    "Franco Nguyen",
    "Rhett Moon",
    "Bella Woods",
    "Macy Bautista",
    "Kaiya Lara",
    "Evelin Horn",
    "Alexandria Eaton",
    "Frida Cross",
    "Kyleigh Koch",
    "Teresa Lopez",
    "Izayah Mullins",
    "Hayden Golden",
    "Miracle Friedman",
    "King Bryant",
    "Estrella Middleton",
    "Alexander Wyatt",
    "Santos Pittman",
    "Kaden Lowe",
    "Joaquin Arroyo",
    "Ahmad Dalton",
    "Lena Oliver",
    "Chasity Copeland",
    "Brittany Archer",
    "Frankie Lynch",
    "Juliet Armstrong",
    "Andy Hernandez",
    "Katelynn Fitzgerald",
    "Houston Christensen",
    "Alyvia Yates",
    "Dane Reeves",
    "Lucian Spears",
    "Azaria Avila",
    "Turner Le",
    "Yazmin Abbott",
    "Hayden Mathis",
    "Karson Ingram",
    "Karly Ferrell",
]

def getName():
    return choice(NAMES)

def getPerson():
    return choice(CARETAKERS)

def getColor():
    return choice(COLORS)

def getPersonality():
    return choice(PERSONALITIES)

def getPets():
    return randrange(5, 500)

def getCats(count):
    names = sample(NAMES, count)
    return [
        Cat(
            name=name,
            color=getColor(),
            personality=getPersonality(),
            pet_count=getPets(),
        )
        for name in names]

def getCaretakers(count):
    names = sample(CARETAKERS, count)
    return [ Caretaker(name=name) for name in names]

def load():
    app = create_app()

    cats = getCats(10)
    caretakers = getCaretakers(10)
    splits = sorted(set(choices(range(1, len(cats)), k=len(caretakers))))

    caretaker_iter = iter(caretakers)
    split_iter = iter(splits)
    caretaker = next(caretaker_iter)
    split = next(split_iter)

    for i, cat in enumerate(cats):
        if i == split:
            caretaker = next(caretaker_iter)
            try:
                split = next(split_iter)
            except StopIteration:
                split = len(cats)

        cat.caretaker = caretaker

    with app.app_context():
        db.session.add_all(caretakers)
        db.session.commit()
        db.session.add_all(cats)
        db.session.commit()

def main():
    load()

if __name__ == "__main__":
    main()