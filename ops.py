#!/usr/bin/env python3

#####TODO :
#good print
#edit a good readme 
# add cookies later 
from colorama import Fore, Back, Style
import optparse
import os
import requests
def banner() :
    print(Fore.BLUE ,
    """
    ______________________
    __  __ \__  __ \_  ___/
    _  / / /_  /_/ /____ \\
    / /_/ /_  ____/____/ /
    \____/ /_/     /____/




                                 [ 0UR4N05 (devalfo@protonmail.com) ]
                                        v 1.0
    """)
    print(Style.RESET_ALL)
    parse()

def parse() :
    usage = "Usage: python3 ops.py -u [url] -w [wordlist]\n\n\nExamples:\npython3 ops.py -u \"http://example.com/index.php?token=junk&redirection=<url>&token=junk\" \npython3 ops.py -u http://example.com/ -w /usr/share/wordlists/word.txt -q \npython3 ops.py -u http://example.com/ -t 1 -c {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}\n\n"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-q" , "--quiet" , dest="quiet" , help="Only show vulnerable links" , action="store_true")
    parser.add_option("-u" , "--url" , dest="url" , help="Target URL (if your link have parameters add a \'<url>\' to the vulnerable parameter" )
    parser.add_option("-t" , "--timeout" , dest="timeout" , help="Time out of waiting to a response(default is 4s)" , default=4 )
    parser.add_option("-w" , "--wordlist" , dest="wordlist" , help="Custom payloads wordlist (optional)" , default="./payloads/big_w.txt")
    (options, args) = parser.parse_args()
    global timeout
    global quiet
    url = options.url
    wordlist = options.wordlist
    if options.url is None:
        parser.print_help()
        exit()
    timeout = int(options.timeout)
    quiet = options.quiet
    checking(url , wordlist)


#check the link
def checking(urlp , wordlistp) :
    if "http" or "https" in urlp :
        print("[+]-Creating the wordlist")
        wordlist(urlp , wordlistp)
    else :
        print("[!]-Url is not correct , please read the documentation")
        exit()

def wordlist(urlw , wordlistp) :
    payloads = open(wordlistp, 'r')
    wordlist = open('./wordlists/wordlist.txt' , "a+")
    if "?" or "=" or "<url>" in urlw :
        print("[+]-Parameters detected")
        for line in payloads :
            line = line.strip(' \n\t')
            url = urlw.replace("<url>" , line) +"\n"
            wordlist.writelines(url)
        payloads.close()
    else : 
        for line in payloads :
            wordlist_elements = urlw + line
            wordlist.writelines(wordlist_elements)
        payloads.close()
    print("[+]-Wordlist done")
    scan()

def scan() :
    print("[/]-Scan started")
    wordlist_l = open("./wordlists/wordlist.txt" , "r")
    for line in wordlist_l :
        r = requests.get(line , timeout = timeout , allow_redirects=False)
        status_code = str(r.status_code)
        if quiet : 
            if r.status_code == 302 :
                res = "[" + status_code + "]--" + line
                print(Fore.GREEN, res)
                print(Style.RESET_ALL)
            elif r.status_code == 301 :
                res = "[" + status_code + "]--" + line
                print(Fore.YELLOW, res)
                print(Style.RESET_ALL)   
        else:
            if r.status_code == 302 :
                res = "[" + status_code + "]--" + line
                print(Fore.GREEN, res , end=" ")
                print(Style.RESET_ALL)
            elif r.status_code == 301 :
                res = "[" + status_code + "]--" + line
                print(Fore.YELLOW, res , end=" ")
                print(Style.RESET_ALL)   
            else : 
                res = "[" + status_code + "]--" + line
                print(Fore.RED, res , end=" ")
                print(Style.RESET_ALL)    
    print("Colors meanings :\n" , Fore.GREEN , "Green : Confirmed redirection\n" , Fore.YELLOW , "Yellow : Suspecious redirection\n" , Fore.RED , "Red : Not a redirection\n note: Please make sure to test the open redirect vulnerabilities before submitting them")    
    print(Style.RESET_ALL)
    choise = input("\n[+]-Scan finished , wanna delete the generated wordlist? [y/n] : ")
    if choise == "n" :
        print(Fore.YELLOW ,"[+]-Okey , BYE ")
        exit()
    elif choise == "y" :
        print(Fore.YELLOW ,"[+]-Done")
        os.remove("./wordlists/wordlist.txt")
    else :
        exit()
try:
    banner()
except KeyboardInterrupt :
    print(Fore.YELLOW , '\n[*]-OKEY ,BYEE')
    os.remove("./wordlists/wordlist.txt")
