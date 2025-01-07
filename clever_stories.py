"""
program: Clever Stories W01
author: Jayson Wade
description:

"""
#def article
def article(word):
    if word.lower().startswith(("hour", "honest", "heir")):
        return "an"
    if word.lower().startswith(("u", "e")) and word.lower()[:2] not in {"un", "eu"}:
        return "an"
    if word[0].lower() in 'aeiou':
        return "an"
    else:
        return "a"
    
#gather info
print("Please fill out the following:")

#filling words
adjective= input("List an adjective: ")
animal= input("List an animal: ")
verb= input("List an action verb: ")
exclamation= input("List an exclamation: ")
verb2= input("List a verb: ")
verb3= input("List an action verb: ")
#added words
random= input("list a weird object: ")
adjective2= input("List an adjective: ")
noun= input("list a noun: ")
noun2= input("list a noun: ")
adjective3= input("List an adjective: ")
animal2= input("List an animal/(plural)/: ")
room= input("List a room in a house: ")
adjective4= input("List an adjective: ")
object= input("List an object: ")

#the story
print()
print("This is your story:")
print()
print("The other day, I was really in trouble. It all started when I saw a very")
print(f'{adjective} {animal} {verb} down the hallway."{exclamation.capitalize()}!" I yelled. But all')
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print("right in front of my family.")
#added story 
print()
print(f"Just when I thought it was over, the {animal} pulled out {article(random)} {random} and")
print(f'began announcing {article(adjective2)} {adjective2} talent show. "{noun.capitalize()} and {noun2}," it said in {article(adjective3)} {adjective3}')
print('voice, "prepare to witness greatness!"')
print()
print(f"Before I could respond, the {animal} snapped its fingers-apparently this {animal} can snap-and")
print(f"summond a team of tap-dancing {animal2} from the {room}. They formed a line, synchronized")
print(f"perfectly, and began performing a flawless routine to the beat of my dad's {adjective4} {object},")
print("which had mysteriously powered itself on.")