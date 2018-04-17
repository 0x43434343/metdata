
"""

author ; Alharbi fahad, faa5431@rit.edu
Course; csec 471 , penetration testing

"""

import requests
from bs4 import BeautifulSoup
import sys
from optparse import OptionParser


def setUpAconnect(site):
    '''
    the purpose of this function is only set a up a connect to the target and get the data and return
    :param site: target
    :return: a content
    '''

    r = requests.get(site)

    content = r.content

    return content

def findAllEmails(site):
    r = requests.get(site)

    content = r.content

    soup = BeautifulSoup(content, "html.parser")


    for a in soup.find_all('a', href=True, text=True):

        if '@' in a['href']:
            print(a['href'][7:])

def getAllThePaths(site):
    '''

    the purpose of this function is only collect all the path of the target
    and store it in a list
    :param site: target
    :return: return a list that contains all the paths
    '''

    #let's set up our call

    site = setUpAconnect(site)
    path = list()
    r = ""

    content = site
    soup = BeautifulSoup(content ,"html.parser")


    links = list()
    for a in soup.find_all('a' ,href=True, text=True):


        if a['href'] in path or 'http' in a['href']:

            continue
        else:
            path.append(a['href'])


    return path




def test():


    target = 'http://www.tcc-ict.com/'


    print(UseGoogleForMoreCo(target))

def help():
    '''
    help function 
    '''
    print("------------------------------------")
    print("example  ")
    print("python metadata.py http://target.com")
    print("------------------------------------")




def execute(target):

    ''' 
    this will execute the code 
    '''
    print("get all the link that we going to looking into it ")
    print("==============================")

    for getAll in getAllThePaths(target):


        print(target+getAll)

    print("==============================")




    print("now !! collect all the emails")

    print("==============================")

    for getAll in getAllThePaths(target):


        findAllEmails(target+getAll)


    print("==============================")
    print("have a great day ")

def main():
    '''
    the main function 
    pre-condition , if argument not equal 2 
    post-condition , will return to help function 
    '''

    if len(sys.argv) !=2:

        help()
        sys.exit()

    else:
        target = sys.argv[1]



        execute(target)



if __name__ == '__main__':
    main()



