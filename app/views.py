#instruction
#virtualenv pillow
#flask selenium
#flask filedepot
#flask simhash flask\Scripts\pip install simhash

from app import app
from spell import correction
from screenshot import saveImage
from screenshot import saveImageUrl
from imagecompare import main
from testsc import DomSimhashTarget
from testsc import DomSimhashAgainst
from flask import request
import ruamel.yaml as yaml # Unicode to str
import json

@app.route('/')
@app.route('/index')

def index():
    return "Hello, World!"

# API Handling 
@app.route('/pingcat', methods = ['POST'])
def getpersonbyid():
    
    #app.logger.debug("JSON received...")
    #app.logger.debug(request.json)
    
    if request.json:
        mydata = request.json # will be 
        jsontestdata = json.dumps(mydata) 
        #print jsontestdata
        yamldata = yaml.safe_load(jsontestdata) # yaml used to unicode to str
        #print yamldata['personId']
        #print yamldata
        #return "Thanks. Your age is %s" % yamldata.get['personId']
        domainreturn = yamldata['fetchDomain']
        #print domainreturn
        #return domainreturn
        #return "json received"
        urlreturn = yamldata['urlName']

        domainURL = urlreturn
        domainfetch = domainreturn
        #print domainfetch
        a = correction(domainfetch)+'.com'

        #print a

        saveImage('http://'+a)

        saveImageUrl(domainURL)

        NormValue = main('app/static/test1.png', 'app/static/test2.png')

        print NormValue
        #print "First"


        if NormValue==0:
            #print "Second"
            TargetSimValue = DomSimhashTarget('http://'+a)
            AgainstSimValue = DomSimhashAgainst(domainURL)
            if TargetSimValue!=AgainstSimValue:
                print "Phishing Detected"  
                return "Phishing Detected. Please becareful of each action in this page"      
            else:
                print "Phishing Not Detected"
                #return "Phishing not detected. Chill" 

        print "Exit time"
        
    else:
        return "no json received"


# END 



        











