def madlibs():
    print("The Mad Libs Game: 'The ranger with a Big Iron on His Hip'!\n")

    ranger_name = input("Enter your ranger's name: ")
    ranger_weapon = input("Enter your weapon: ")
    location = input("Enter a location: ")
    outlaw_name = input("Enter the outlaw in question's name: ")
    outlaw_action = input("Enter an action the outlaw carried out: ")

    madlib_story = f"""
    The ranger {ranger_name} rode into the {location} town,
    He was searching for an outlaw who {outlaw_action} and would never back down.
    He carried a {ranger_weapon} on his hip, small but grand,
    Ready to draw and defend justice across all of {location}.

    One day, {outlaw_name} came, a notorious figure for all the wrong reasons,
    He searched and challenged the ranger, with a devious look on his face.
    But {ranger_name} was quick, his aim was true,
    He drew his {ranger_weapon}, and the outlaw he promptly slew.

    The townsfolk cheered, the ranger hailed a hero,
    With the big iron on his hip, he brought peace, not zero.
    So here ends our tale, of the ranger so bold,
    With his {ranger_weapon} and courage, the legend we've told.
    """

    print("\nYour Big Iron Story:\n")
    print(madlib_story)

madlibs()

