def mad_libs():
    print("\n Let's creates a story! Fill in the blanks.")
    noun = input("Noun : ")
    verb = input("Verb : ")
    adjective = input("Adjective : ")
    place = input("place : ")

    story = f"""
    Once upon a time , a time ,a {adjective} {noun} 
    decide to {verb} at the {place}.
    Everyone was suprised, but it turned out
    to be the best idea ever!
    """
    print("\n Here's your story :\n")
    print(story)
