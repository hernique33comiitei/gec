import os
import pyfiglet
from colorama import Fore, Style
from PyInquirer import prompt
from utils.utils import optionsTypeList, left


def generateTextStyle(text, style=Fore.CYAN):
    textArt = pyfiglet.figlet_format(text, font="slant")
    return f"{style}{textArt}{Style.RESET_ALL}"


def createQuestion(type, name, message, choices=None):
    selectQuestionForType = {
        'list': [{
            'type': type,
            'name': name,
            'message': message,
            'choices': choices
        }],
        'input': [{
            'type': type,
            'name': name,
            'message': message
        }]
    }

    return selectQuestionForType[type]


def menu():
    questionType = createQuestion(
        'list', 'type', 'select an option:', optionsTypeList)

    responseType = prompt(questionType)
    indexType = optionsTypeList.index(responseType['type'])

    if optionsTypeList[indexType] == left:  # this is select close option
        return

    questionDescription = createQuestion(
        'input', 'description', 'enter a description: ')

    responseDescription = prompt(questionDescription)
    responseFinishArray = [indexType, responseDescription['description']]

    return responseFinishArray


def commitDatas(message):
    try:
        os.system(f"git commit -m '{message}'")

    except:
        textErro = generateTextStyle("ERROR", Fore.RED)
        print(f"{textErro}")


def generateMessage():
    responsesMenu = menu()

    if not responsesMenu:
        textClose = generateTextStyle("SEE YOU LATER")
        return print(textClose)

    typeText = optionsTypeList[responsesMenu[0]]
    message = f"{typeText}{responsesMenu[1].capitalize()}"

    return commitDatas(message)
