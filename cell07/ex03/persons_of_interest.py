#!/usr/bin/env python3

def famous_births(dictionary):
    for person in sorted(dictionary, key=lambda element: dictionary[element]["date_of_birth"]):
        person = dictionary[person]
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

def main():
    women_scientists =  {
                            "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
                            "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
                            "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
                            "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
                        }
    famous_births(women_scientists)

if __name__ == '__main__':
    main()
