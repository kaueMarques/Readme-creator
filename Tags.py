class Tags:
    
    def makeDiv(strName: str, strPosition: str, strTags: str):
        return f"\n\n<div align=\"{strPosition}\" class=\"{strName}\">\n\n {strTags} \n\n</div>\n"

def makeTag(strType: str, strText: str):
    return f"\t\t\n<{strType}>{strText}</{strType}>\n"


def makeText(strType: str, strPosition: str, strText: str):
    return f"\t\n\n<{strType} align=\"{strPosition}\">{strText}</{strType}>\n"


def makeText(strType: str, strDecoration: str, strPosition: str,  strText: str):
    return f"\t\n\n<{strType} align=\"{strPosition}\"> <{strDecoration}> {strText} </{strDecoration}> </{strType}>\n"


def makeIMG(strNameIMG: str, strPostion: str, strImageURL: str):
    return f"\t<img src=\"{strImageURL}\" alt=\"{strNameIMG}\" align=\"{strPostion}\">\n"


def makeShild(strName: str, strColor: str):
    return f'\t\n![{strName}](https://img.shields.io/badge/{strName}-{strColor}.svg?style=for-the-badge&logo={strName}&logoColor=white)\n'


def makeShildMadeWithIMG(strText: str, strColor: str, strLogo: str, strTechSite: str):
    return f"\t\n[![{strText}](https://img.shields.io/badge/Made % 20with-{strLogo}-{strColor}?style=for-the-badge & logo={strLogo})]({strTechSite})\n"


def makeHiddenElement(strTitle: str, strElements: str):
    return f"\n<details>\n<summary>{strTitle}</summary>\n{strElements}\n</details>\n"


def makeVideo(strLink: str):
    return strLink


def makeCommand(strCommand: str):
    return f"\t\n``` {strCommand} ```\n"

def makeList(strAsk:str):

    strFormatedMD = """"""

    strElement = input(f"{strAsk}: ")

    while strElement != "":
        strFormatedMD += makeTag('li', f"{strElement}" )
        strElement = input(f"{strAsk}: ")

    return  strFormatedMD

def makeIMGList():
    strFormatedMD = """"""

    strIMG = input("Image URL/Dir: ")
    strNameIMG = input("Image URL/Dir: ")

    while strIMG != "":
        strFormatedMD += makeIMG(strNameIMG, 'center', strIMG)
        strIMG = input(f"IMG URL/Dir: ")
        strNameIMG = input("Image URL/Dir: ")

    return strFormatedMD


def makeTechList():
    
    techList = {'':''}
    

    strTechName = input("Tech Name: ")
    strTechColor = input("Tech Color: ")

    while strTechName != "" or strTechColor != "":
        str

    

    return ""




