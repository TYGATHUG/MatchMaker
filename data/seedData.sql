/* ======== Insert Values ======== */
/* Multi-row insert from a series of insert statements
  is faster than running individual inserts
 */
 BEGIN TRANSACTION;
    INSERT INTO Match VALUES ("Damon", "images.jpeg", "Damon", "Male", 35, 186, "Melbourne", "Bachelor", "White", "Atheist", "I study computer science and like to fly model airplanes.", 2, 3, 8, 19, 0, 35, 1, 0, 0, 0.5, 1, 0, 1);
    INSERT INTO Match VALUES ("Peter", "jim.jpeg", "Peter", "Male", 42, 172, "Melbourne", "Post grad", "Asian", "Christian", "I work as an accountant and enjoy gardening.", 0, 0, 3, 76, 2, 74, 1, 0, 0, 1, 1, 0.5, 1);
    INSERT INTO Match VALUES ("Mary", "mary.jpeg", "Mary", "Female", 23, 162, "Melbourne", "None", "White", "Christian", "I like reading books and going for brunch. ", 3, 30, 9, 23, 6, 50, 1, 1, 0, 0.5, 1, 0, 1);
    INSERT INTO Match VALUES ("Lucy", "Slider_3_-_Lucy_Hale__Actress.jpeg", "Lucy", "Female", 32, 163, "Melbourne", "Bachelor", "Asian", "Atheist", "I am a career driven professional woman", 8, 4, 35, 76, 2, 54, 1, 0.5, 1, 0.5, 1, 0.5, 1, 0, 0.5);
    INSERT INTO Match VALUES ("Stefanie", "4.jpeg", "Stefanie", "Female", 30, 170, "Sydney", "Bachelor", "Hispanic", "Catholic", "I'm just you're average person.", 5, 20, 15, 43, 2, 75, 0.5, 0.5, 1, 0, 0, 1, 0.5);
    INSERT INTO Match VALUES ("Tom", "5.jpeg", "Tom", "Male", 28, 150, "Syndey", "Associate Degree", "White", "Catholic", "I like to surf and long walks.", 10, 15, 3, 52, 12, 32, 1, 1, 0, 0, 0.5, 1, 0);
    INSERT INTO Match VALUES ("Arwa", "6.jpeg", "Arwa", "Female", 25, 180 , "Sydney", "PHD", "African", "Atheist", "I study a lot.", 43, 59, 2, 23, 3, 68, 0, 0.5, 1, 1, 1, 0, 0.5);
    INSERT INTO Match VALUES ("John", "7.jpeg", "John", "Male", 30, 190, "Melbourne", "Bachelor", "Asian", "Atheist", "I like to eat.", 10, 54, 32, 2, 42, 4, 1, 1, 0.5, 1, 0, 0, 1);
    INSERT INTO Match VALUES ("Ashe", "8.jpeg", "Ashe", "Male", 22, 175, "Melbourne", "Cert IV", "White", "Christian", "I like to go bowling.", 2, 32, 76, 8, 23, 22, 1, 0, 0, 0.5, 1, 1, 1);
    INSERT INTO Match VALUES ("Sophie", "9.jpeg", "Sophie", "Female", 39, 180, "Melbourne", "Bachelor", "White", "Catholic", "I like to go fishing.", 3, 5, 21, 42, 74, 29, 1, 1, 0.5, 1, 0, 0, 1);
    INSERT INTO Match VALUES ("Laura", "10.jpeg", "Laura", "Female", 29, 177, "Melbourne", "Bachelor", "Asian", "Atheist", "I like to dance.", 22, 5, 75, 34, 6, 43, 1, 0.5, 0.5, 0, 1, 1, 1);
  COMMIT;


/*
    for sqlite3

    users = [
        ("Damon", "images.jpeg", "Damon", "Male", 35, 186, "Melbourne", "Bachelor", "White", "Atheist",
                 "I study computer science and like to fly model airplanes.", 2, 3, 8, 19, 0, 35, 1, 0, 0, 0.5, 1, 0, 1),
        ("Peter", "jim.jpeg", "Peter", "Male", 42, 172, "Melbourne", "Post grad", "Asian", "Christian",
                   "I work as an accountant and enjoy gardening.", 0, 0, 3, 76, 2, 74, 1, 0, 0, 1, 1, 0.5, 1),
        ("Mary", "mary.jpeg", "Mary", "Female", 23, 162, "Melbourne", "None", "White", "Christian",
                   "I like reading books and going for brunch. ", 3, 30, 9, 23, 6, 50, 1, 1, 0, 0.5, 1, 0, 1),
        ("Lucy", "Slider_3_-_Lucy_Hale__Actress.jpeg", "Lucy", "Female", 32, 163, "Melbourne", "Bachelor", "Asian",
                   "Atheist", "I am a career driven professional woman", 8, 4, 35, 76, 2, 54, 1, 0.5, 1, 0.5, 1, 0.5, 1, 0,
                   0.5),
        ("Stefanie", "4.jpeg", "Stefanie", "Female", 30, 170, "Sydney", "Bachelor", "Hispanic", "Catholic",
                   "I'm just you're average person.", 5, 20, 15, 43, 2, 75, 0.5, 0.5, 1, 0, 0, 1, 0.5),
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
 */