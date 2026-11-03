# pes_3p1

this repo is created for the 5 days of training for 3rd sem students of PES Mandya. It was held in 1st week of Nov 2026. The content was Git and commands, Core Python concepts, problem solving on loops, recursion, arrays and strings. They also learnt basic DSA

---

## BLC PYTHON TRAINING FOR 3RD SEM E&C PES MANDYA

Programming Language Concepts
Core Python Concepts (Pythonic)
Some of the Libraries (str, list, tuple, dict, set, date)
Problem Solving (BLC Caliber, Coding practice)
Basic DSA (Searching and Sorting and Stack and Queue)

## App Installations:

    notepad_pp 	(To make Quick Notes)
    vs_code 	(To make Documentations and Coding and Development)
    python
    node 		(For Java Script and ReactJS)
    git
    git_desktop
    mongo_db 	(server, compass, shell)

## Git Commands:

Create git account (Use your permanent email and ph number)
Login to your git account
Create new Repository (Repo)
Name: blc_3p1_nov26 (student repo name)
pes_3p1_nov26 (Trainer repo name)
Give description for the new Repo
Keep the Repo public so that the trainer can access it
Add readme.md file to add notes
Keep other settings in tact.
Git configuration:

> git config --global user.name "your_git_username"

> git config --global user.email "your@email.com"

### Steps to create Git Personal Access Token (PAT):

    Click profile picture (Top right corner)
    Next page, scroll down click developer settings
    Next page click Personal access tokens and select classic
    Next page click generate new token and select classic
    Next page, give note, select no-expiry, select Repo checkBox
    Copy the PAT and mail it to your self with git_pat/git pat

> git clone https://github.com/neelmyna/pes_3p1

> git clone https://PAT@github.com/neelmyna/pes_3p1

## Git Push Operation:

> git add <path>
> This command lists/stages all the files that need to be updated in the remote repo

> git commit
> This command creates an object, stores/copies content of all the files that are staged and then the object is encrypted.

> git push

## This command finally uploads the commited object to the server.

## HOW DATA IS STORED IN MEMORY

The smallest unit of memory is BIT
In one bit we can stored 0 or 1

We ca make patterns of 0s and 1s and assume them to be some data

Let
000 000 be A
000 001 be B
000 011 be C etc.

Different group of people can have their own patterns.
But if we have to work on very big project like Airbus.....

ASCII
256 characters
ASCII Value ASCII Char BINARY
65 A 0100 0001
66 B
90 Z
97 a
99 c
122 z

ASCII value starts from 0 and 255

Let us take 45
0010 1101

Let us now store -45
absolute(-45)
45
0010 1101
1101 0010
1
1101 0011
= -1*2(7) + 1*2(6) + 1\*2(4) + 3
= -128 + 64 + 16 + 3
= -64 + 19
= -45

DTs in Python:
int
float
str
chr

Everything in Python is an Object

In C/C++/Java:
int num = 55;
int age = age;
int studentAge = 17;

class VtuStudentAge
int minimumAge = 18
int studentAge = 0
int maximumAge = 60

class BankAccount
int accNumber
string name
float balance
string type
int phoneNumber

    create()
    update()
    delete()
    freeze()
    search()
    list()
----------------------------------
