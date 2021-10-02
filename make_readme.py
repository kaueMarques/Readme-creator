##############################W###############
#Variables

strMarkdown = """"""
lines = "="*10
dobleLines = lines*4

strMarkdown = """"""

strProjectName:str=  ""
strShortDescription:str= ""
strDescription:str= ""

##############################W###############
# Methods

from Tags import *


def welcome():
    welcome = f"""
    \t{dobleLines}
    \t{lines}  Markdown Creator  {lines}
    \t{dobleLines}
    \n\tHere we gonna create your \"README.md\"  automatically.
    \n\tIf you don't want any element leave in blank
    \n\t{dobleLines}
    """
    print(welcome)

##############################W############### 
# Creating Document

welcome()

strProjectName = input("Project Name: ")
strShortDescription = input("Short Description: ")
strDescription = input("Description: ")
strTechUsada = input("Tech Usada: ")
strCorTags = input("Cor Tags: ")


strMarkdown +=  Tags.makeDiv('Header', 'center',

    makeTag('h1', strProjectName)
    + makeText('p','i','center', strShortDescription)
    + makeShild(strTechUsada, strCorTags)
    
)


strMarkdown += Tags.makeDiv('Galery', 'left',

    makeTag('h1', '🖼️ Image Showcase')
    +makeIMGList()

)

strMarkdown +=  Tags.makeDiv('FullDescription', 'left',

    makeTag('h1', '📖 Description')
    + makeTag('p',strDescription)

)


strMarkdown +=  Tags.makeDiv('Instalation', 'left',

    makeTag('h1', '📦 Instalation')
    + makeTag('h3', 'Requisites: ')
    + makeList('step ')
    + makeTag('h3', 'Instalation: ')
    + makeList('step ')

)

print(strMarkdown)

with open('README.md', 'w') as f:
    f.write(strMarkdown)
