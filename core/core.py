import os
import pyfiglet
from colorama import Fore, Style
from PyInquirer import prompt
from utils.utils import *


def generateTextStyle(text, style=Fore.CYAN):
    textArt = pyfiglet.figlet_format(text, font="slant")
    return f"{style}{textArt}{Style.RESET_ALL}"


def menu(optionsType):
    questionType = [
        {
            'type': 'list',
            'name': 'type',
            'message': 'select an option:',
            'choices': optionsType
        }
    ]
    responseType = prompt(questionType)
    indexType = optionsType.index(responseType['type'])

    if optionsTypeList[indexType] == left:  # this is select close option
        return

    questionDescription = [
        {
            'type': 'input',
            'name': 'description',
            'message': 'enter a description: '
        }
    ]
    responseDescription = prompt(questionDescription)

    responseFinishArray = [indexType, responseDescription['description']]
    return responseFinishArray


def pushDatas(message):
    try:
        os.system(f"git commit -m '{message}'")
        os.system("git push")

    except:
        textErro = generateTextStyle("ERROR", Fore.RED)
        print(f"{textErro}")


def generateMessage():
    responsesMenu = menu(optionsTypeList)

    if not responsesMenu:
        textClose = generateTextStyle("SEE YOU LATER")
        return print(textClose)

    typeText = optionsTypeList[responsesMenu[0]]
    message = f"{typeText}{responsesMenu[1].capitalize()}"

    return pushDatas(message)
