def main()->None:
  try:
    place : str = input("Noun(Place): ")
    verb1 : str = input("Verb: ")
    adjective1 : str = input("Adjective: ")
    noun1 : str = input("Noun: ")
    noun2 : str = input("Noun(Animal): ")
    verb2  : str = input("Verb: ")
    adjective2 : str = input("Adjective: ")
    noun3 : str = input("Noun: ")
    adjective3 : str = input("Adjective: ") 
    madlibs : str = f"My favorite place to go is the  {place}. I like \
to {verb1} with my {adjective1} friends. We always bring a \
{noun1} to share. Sometimes, we see a {noun2} running by, \
and it makes us {verb2}. One time, we even saw a \
{adjective2} {noun3} floating in the sky! It was the most {adjective3} day ever!"
    print(madlibs)
    return None
  except:
    print("\nUnknown Error Occured!")
    return None
if __name__ == "__main__":
  main()