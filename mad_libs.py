def get_input(word_type :str):
    word : str =input(f"Type a {word_type}")
    return (word)

noun1=get_input("noun")
verb1=get_input("verb")
noun2=get_input("noun")
verb2=get_input("verb") 
story= f""" Hi I am {noun1} , I like to {verb1} and I am a freind of  {noun2}
we always {verb2} together!! What about you"""

print(story)