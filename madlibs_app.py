#------------------------------------------
# Python Learning -- Creating a MadLibs App
#------------------------------------------

#------------------------------------------
#

def which_story():
    name = input("Who is your favourite women in technology? ")
    chosen_story = name.lower()
    if chosen_story == "ada":
        ada_madlib()
    elif chosen_story == "grace":
        grace_madlib()
    elif chosen_story == "katherine":
        katherine_madlib()
    else:
        print("**Choose one of the three women in technology**")
        return which_story()

def ada_madlib():
    name, nationality, country_birth, invention, invention_name, acronym, friend1, friend2 = user_summary()
    print("""
        {} was a {} mathematician and writer, chiefly known for her work on {}. She was the first to recognise that
        {} had applications beyond what she had imagined at first. She wrote and published a paper and described
        that the idea could solve the problem of {}. As a result, she is now recognised as one of the most famous
        computer scientists of all time.\n

        Her motivation and educational exploits brought her into contact with scientists such as Andrew Crosse, Sir
        David Brewster, Charles Wheatstone, Michael Faraday and the author Charles Dickens, contacts which she used to
        further her education. She described her approach as 'poetical science' and herself as an 'Analyst (& Metaphysician)'.\n

        When {} was a teenager, her mathematical talents led her to a long working relationship and friendship with
        fellow British mathematician Charles Babbage, also known as "the father of computers", and in particular,
        Babbage's work on the Analytical Engine. {}’s mindset of "poetical science" led her to ask questions about the
        {} (as shown in her notes).)""".format(name, nationality, invention_name, invention_name, invention, name, name, invention_name ))

def grace_madlib():
    name, nationality, country_birth, invention, invention_name, acronym, friend1, friend2 = user_summary()
    print("""
        {} was an {} computer scientist and {} Navy rear admiral. {} was a pioneer of computer programming who invented
        one of the first compiler related tools. She popularized the idea of machine-independent programming languages,
        which led to the development of {}, an early high-level programming language still in use today.\n

        Prior to joining the Navy, {} attained a Ph.D. in mathematics from Yale University and was a professor of mathematics
        at Vassar College. {} attempted to enlist in the Navy during World War II but was rejected because she was 34 years
        old. She instead joined the Navy Reserves. {} began her computing career in 1944 when she worked on the Harvard Mark
        I team led by {}. In 1949, she joined the Eckert–Mauchly Computer Corporation and was part of the team that developed
        the UNIVAC I computer. At Eckert–Mauchly she began developing the compiler. She believed that a programming language
        based on English was possible. Her compiler converted English terms into machine code understood by computers.
        By 1952, {} had finished her program linker (originally called a compiler).\n

        Owing to her accomplishments and her naval rank, she was sometimes referred to as "Amazing {}".The {} Navy named a ship
        the USS {}. {} was awarded 40 honorary degrees from universities across the world. A college at Yale University
        was renamed in her honor. In 1991, she received the National Medal of Technology.
        """.format(name, nationality, country_birth, name, acronym, name, name, name, friend1, name, name, nationality, name, name))

def katherine_madlib():
    name, nationality, country_birth, invention, invention_name, acronym, friend1, friend2 = user_summary()
    print("""
        {} is an {} mathematician whose calculations of orbital mechanics as a NASA employee were critical to the success
        of the first and subsequent U.S. manned spaceflights.During her 35-year career at NASA, {} earned a reputation for
        mastering complex manual calculations and helped the space agency pioneer {} to perform computational tasks in deep space.\n

        {}'s work included calculating trajectories, launch windows and emergency return paths for Project Mercury spaceflights,
        including those of astronauts {} and {}. {} calculations were also essential to the beginning of the Space Shuttle
        program, and she worked on plans for a mission to Mars. In 2015, President Barack Obama awarded {} the Presidential
        Medal of Freedom. {} was portrayed by Taraji P. Henson as a lead character in the 2016 film Hidden Figures.

        """.format(name, nationality, name, invention_name, name, friend1, friend2, name, name, name))

#------------------------------------------
# User Input Sub-functions

def user_summary():
    name = user_input_name()
    print(name)
    nationality = user_input_nationality()
    print(nationality)
    country_birth = user_input_country_birth()
    print(country_birth)
    invention = user_input_invention()
    print(invention)
    invention_name = user_input_invention_name()
    print(invention_name)
    acronym = user_input_acronym()
    print(acronym)
    friend1 = user_input_friend1()
    print(friend1)
    friend2 = user_input_friend2()
    print(friend2)

    return name, nationality, country_birth, invention, invention_name, acronym, friend1, friend2

def user_input_name():
    user_name = input("What is your name? ")

    return user_name

def user_input_nationality():
    user_nationality = input("What is your nationality? ")

    return user_nationality

def user_input_country_birth():
    user_country_birth = input("What country were you born in? ")

    return user_country_birth

def user_input_invention():
    user_invention = input("If you could invent something what would it be? ")

    return user_invention

def user_input_invention_name():
    user_invention_name = input("What would your invention be called? ")

    return user_invention_name

def user_input_acronym():
    user_acronym = input("Give us a cool acronym ")

    return user_acronym

def user_input_friend1():
    user_friend1 = input("A friend's name: ")

    return user_friend1

def user_input_friend2():
    user_friend2 = input("Another friend's name: ")

    return user_friend2

which_story()







