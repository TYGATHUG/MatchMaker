/* ======== Drop Table ======== */
DROP TABLE IF EXISTS AUTH;
DROP TABLE IF EXISTS USER;
DROP TABLE IF EXISTS CHAT;
DROP TABLE IF EXISTS MATCH;




/* ======== Create Table ======== */
CREATE TABLE AUTH (
    uid integer not null primary key autoincrement,
    email text not null,
    password text not null,
    date real
);

CREATE TABLE USER (
    id integer primary key autoincrement,
    fname text not null,
    lname text not null,
    gender text not null check (gender = "Male" or gender = "Female"),
    age integer not null,
    location text not null,
    height integer not null,
    occupation text not null,
    education text not null,
    ethnicity text not null,
    religion text not null,
    about text not null,
    er integer, -- Emotional Range
    c integer,  -- Conscientiousness
    o integer,  -- Openness
    ie integer, -- Introversion/Extraversion
    a integer,  -- Agreeableness

    foreign key(uid) references AUTH (uid)
);

CREATE TABLE MATCH (
    id integer primary key autoincrement,
    practicality int not null,
    love int not null,
    excitment int not null,
    challenge int not null
    closeness int not null,
    structure int not null,
    live_music int not null,
    spare_of_moment_purchase int not null,
    gym_member int not null,
    outdoors int not null,
    volunteering int not null,
    entreprenuer int not null,
    reading int not null 
)


CREATE TABLE CHAT (
    cid integer not null primary key autoincrement,
    uid1 integer not null,
    uid2 integer not null,
    chatlog text,

    foreign key(uid1) references AUTH (uid),
    foreign key(uid2) references AUTH (uid)
);