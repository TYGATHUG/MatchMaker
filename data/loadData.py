import sqlite3

conn = sqlite3.connect('app.db')
c = conn.cursor()


def data_entry():
    users = [
        ("Tom", "5.jpeg", "Tom", "Male", 28, 150, "Syndey", "Associate Degree", "White", "Catholic",
         "I like to surf and long walks.", 10, 15, 3, 52, 12, 32, 1, 1, 0, 0, 0.5, 1, 0),
        ("Arwa", "6.jpeg", "Arwa", "Female", 25, 180, "Sydney", "PHD", "African", "Atheist", "I study a lot.", 43, 59,
         2, 23, 3, 68, 0, 0.5, 1, 1, 1, 0, 0.5),
        ("John", "7.jpeg", "John", "Male", 30, 190, "Melbourne", "Bachelor", "Asian", "Atheist", "I like to eat.", 10,
         54, 32, 2, 42, 4, 1, 1, 0.5, 1, 0, 0, 1),
        ("Ashe", "8.jpeg", "Ashe", "Male", 22, 175, "Melbourne", "Cert IV", "White", "Christian",
         "I like to go bowling.", 2, 32, 76, 8, 23, 22, 1, 0, 0, 0.5, 1, 1, 1),
        ("Sophie", "9.jpeg", "Sophie", "Female", 39, 180, "Melbourne", "Bachelor", "White", "Catholic",
         "I like to go fishing.", 3, 5, 21, 42, 74, 29, 1, 1, 0.5, 1, 0, 0, 1),
        ("Laura", "10.jpeg", "Laura", "Female", 29, 177, "Melbourne", "Bachelor", "Asian", "Atheist",
         "I like to dance.", 22, 5, 75, 34, 6, 43, 1, 0.5, 0.5, 0, 1, 1, 1)
    ]

    conn.executemany("INSERT INTO Match(username, image, name, gender, age, height, location, education, ethnicity, "
                    "religion, bio, practicality, love, excitment, challenge, closeness, structure, live_music, "
                    "spare_moment_purchases, gym_member, outdoors, volunteering, entreprenuer, reading) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", users)
    conn.commit()
    c.close()
    conn.close()

data_entry()