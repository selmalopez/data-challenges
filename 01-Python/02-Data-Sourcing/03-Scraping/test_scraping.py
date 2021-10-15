# pylint: disable=missing-docstring,invalid-name

#: paste the code from Kitt's instructions

from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(open("https://recipes.lewagon.com/"), "html.parser")

    for recipe in soup.find_all("name", "prep_time","difficulty"):

        name= recipe.find("recipe-name")
        prep_time = int(recipe.find("prep_time", class_="recipe-cooktime").string.strip('min'))
        difficulty = recipe.find("recipe-difficulty")

    for i in range(len(recipe)):
        print(name[i])
        print(prep_time[i])
        print(difficulty[i])

def write_csv(ingredient, recipes):

    with open('https://recipes.lewagon.com/', 'w') as csvfile:
        file = csvfile.DictWriter(csvfile, fieldnames=recipes[0].keys())
        file.writeheader()
        for i in recipes:
            file.writerow(i)

    #return "ingredient+ liste[i]"


     #zip
#for movie in soup.find_all("div", class_="lister-item-content"):

#error : file not found
