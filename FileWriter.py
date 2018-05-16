from datetime import *
from decimal import *
import configparser
import sys

recordList = []
recordCount = 0
options = "1. New record   2. Print records  3. Modify Admin Settings  4. Export Records to File  5. Delete record  q. Quit"
ctOptions = "1. New CT record   2. Return  3. Change CT Settings"
ctSettings = "1. Tax Year  2. Notes  3. Plan Start Date  4. Plan End Date  5. Last Name  6. First Name  7. Return to Previous Menu"

class globalSettings():
    #Global admin settings
    admin = "EV1"
    employer = "SSB23"
    sync = "Y"
    date = date.today().strftime("%m%d%Y")
    time = datetime.now().strftime("%I%M%S")
    version = "1.0"
    
    #CT record settings
    taxYearToggle = False
    notesToggle = False
    planStartDateToggle = False
    planEndDateToggle = False
    lastNameToggle = False
    firstNameToggle = False

class ctRecord:
    def __init__(self, participantID, planName, contributionDate, contributionDescription, contributionAmount, amountType, taxYear, notes, planStartDate, planEndDate, lastName, firstName):
        self.recordType = 'CT'
        self.participantID = participantID
        self.planName = planName
        self.contributionDate = contributionDate
        self.contributionDescription = contributionDescription
        self.ContributionAmount = contributionAmount
        self.amountType = amountType
        self.taxYear = taxYear
        self.notes = notes
        self.planStartDate = planStartDate
        self.planEndDate = planEndDate
        self.lastName = lastName
        self.firstName = firstName

class recordHeader:
    def __init__(self, admincode, employercode, syncflag, fileversion, submitdate, submittime):
        self.admincode = admincode
        self.employercode = employercode
        self.syncflag = syncflag
        self.fileversion = fileversion
        self.submitdate = submitdate
        self.submittime = submittime

    def printHeader(self):
        header = ('FH|{}|{}|{}|{}|{}|{}').format(self.admincode, self.employercode, self.syncflag, self.submitdate, self.submittime, self.fileversion)
        print(header)

    def writeHeader(self):
        header = ('FH|{}|{}|{}|{}|{}|{}').format(self.admincode, self.employercode, self.syncflag, self.submitdate, self.submittime, self.fileversion)
        return header

class recordFooter:
    def __init__(self, admincode, employercode, submitdate, submittime):
        self.admincode = admincode
        self.employercode = employercode
        self.submitdate = submitdate
        self.submittime = submittime

    def printFooter(self):
        footer = ('FF|{}|{}|{}|{}|{}').format(getRecordCount(), self.admincode, self.employercode, self.submitdate, self.submittime)
        print(footer)

    def writeFooter(self):
        footer = ('FF|{}|{}|{}|{}|{}').format(getRecordCount(), self.admincode, self.employercode, self.submitdate, self.submittime)
        return footer

class inputValidation:

    def dateValidation(self, x):
        datestring = x
        try:
            if(x == 'n'):
                return ''
            date = datetime.strptime(datestring, '%m/%d/%Y')
        except:
            print("Invalid date. Proper format for date is MM/DD/YYYY. Or type n to skip.")
            datestring = inputValidation.dateValidation(input(""))
        return datestring
        

def getSettings():

    def getCtRecordSettings():
        globalSettings.taxYearToggle = config.getboolean('ctRecordSettings', 'taxYearToggle')
        globalSettings.notesToggle = config.getboolean('ctRecordSettings', 'notesToggle')
        globalSettings.planStartDateToggle = config.getboolean('ctRecordSettings', 'planStartDateToggle')
        globalSettings.planEndDateToggle = config.getboolean('ctRecordSettings', 'planEndDateToggle')
        globalSettings.lastNameToggle = config.getboolean('ctRecordSettings', 'lastNameToggle')
        globalSettings.firstNameToggle = config.getboolean('ctRecordSettings', 'firstNameToggle')
        print('CT Config Loaded.')

    config = configparser.SafeConfigParser()

    try:
        config.read('config.ini')
        getCtRecordSettings()
    except IOError:
        print("Could not load configuration file. Using default settings.")

def toggleCTSettings():
    while True:
        toggles = ('Tax Year: {} | Notes: {} | Plan Start Date: {} | Plan End Date: {} | Last Name: {} | First Name: {} |').format(globalSettings.taxYearToggle, globalSettings.notesToggle, globalSettings.planStartDateToggle, globalSettings.planEndDateToggle, globalSettings.lastNameToggle, globalSettings.firstNameToggle)
        print(toggles)
        print(ctSettings)
        selection = input("")
        if selection == '1':
            globalSettings.taxYearToggle = not globalSettings.taxYearToggle
        if selection == '2':
            globalSettings.notesToggle = not globalSettings.notesToggle
        if selection == '3':
            globalSettings.planStartDateToggle = not globalSettings.planStartDateToggle
        if selection == '4':
            globalSettings.planEndDateToggle = not globalSettings.planEndDateToggle
        if selection == '5':
            globalSettings.lastNameToggle = not globalSettings.lastNameToggle
        if selection == '6':
            globalSettings.firstNameToggle = not globalSettings.firstNameToggle
        if selection == '7':
            newRecord()
            break
            
def printAdminSettings():
    formattedSettings = ('Admin: {}| Employer: {}| Sync: {}| Version: {} ').format(globalSettings.admin, globalSettings.employer, globalSettings.sync, globalSettings.version)
    print(formattedSettings)

def changeAdmin():
    newAdmin = input("Input new admin: ")
    print("Change new admin to " + newAdmin + "?")
    while True:
        response = input("")
        if response == 'y':
            globalSettings.admin = newAdmin
            break
        if response == 'n':
            break
    modifyAdminSettings()

def changeEmployer():
    newEmployer = input("Input new employer: ")
    print("Change new employer to " + newEmployer + "?")
    while True:
        response = input("")
        if response == 'y':
            globalSettings.employer = newEmployer
            break
        if response == 'n':
            break
    modifyAdminSettings()

def changeSyncFlag():
    while True:
        response = input("Input new flag setting: ")
        if(response == 'y'):
            globalSettings.sync = 'Y'
            break
        if(response == 'n'):
            globalSettings.sync = 'N'
            break
    modifyAdminSettings()

def changeVersion():
    newVersion = input("Input new version: ")
    print("Change version number to " + newVersion + "?")
    while True:
        response = input("")
        if response == 'y':
            globalSettings.version = newVersion
            break
        if response == 'n':
            break
    modifyAdminSettings()

def getRecordCount():
    return recordCount

def incrementCount():
    global recordCount
    recordCount += 1

def menu():
    while True:
        print(options)
        selection = input("")
        if selection == '1':
            newRecord()
            break
        if selection == '2':
            printRecords()
        if selection == '3':
            modifyAdminSettings()
            break
        if selection == '4':
            exportToFile()
            break
        if selection == '5':
            deleteRecord()
        if selection == 'q':
            sys.exit(0)
            break

def exportToFile():
    i = 1
    fileName = input("Export file name?")
    fileName += '.txt'

    file = open(fileName, "w")
    header = recordHeader(globalSettings.admin, globalSettings.employer, globalSettings.sync, globalSettings.version, globalSettings.date, globalSettings.time)
    file.write(header.writeHeader() + "\n")

    for record in recordList:
        if(record.recordType == 'CT'):
            file.write('[{}]{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(i, record.recordType, record.participantID, record.planName, record.contributionDate, record.contributionDescription, record.ContributionAmount, record.amountType, record.taxYear, record.notes, record.planStartDate, record.planEndDate, record.lastName, record.firstName) + "\n")
        i += 1

    footer = recordFooter(globalSettings.admin, globalSettings.employer, globalSettings.date, globalSettings.time)
    file.write(footer.writeFooter())
    file.close()

    menu()



def newCtRecord():
    participantID = input("Participant ID?")
    planName = input("Plan name?")
    cd = inputValidation.dateValidation(input("Contribution Date?"))
    contributionDate = cd
    contributionDescription = input("Contribution Description?")
    contributionAmount = input("Contribution Amount?")
    amountType = input("Amount Type?")
    
    if globalSettings.taxYearToggle == True:
        taxYear = input("Tax Year?")
    else:
        taxYear = ""
    
    if globalSettings.notesToggle == True:
        notes = input("Notes?")
    else:
        notes = ""

    if globalSettings.planStartDateToggle == True:
        planStartDate = inputValidation.dateValidation(input("Plan year start date?"))
    else:
        planStartDate = ""

    if globalSettings.planEndDateToggle == True:
        planEndDate = inputValidation.dateValidation(input("Plan year end date?"))
    else:
        planEndDate = ""

    if globalSettings.lastNameToggle == True:    
        lastName = input("Last name?")
    else:
        lastName = ""

    if globalSettings.firstNameToggle == True:    
        firstName = input("First name?")
    else:
        firstName = ""

    record = ctRecord(participantID, planName, contributionDate, contributionDescription, contributionAmount, amountType, taxYear, notes, planStartDate, planEndDate, lastName, firstName)
    recordList.append(record)
    incrementCount()

    newRecord()
    
def newRecord():
    while True:
        print(ctOptions)
        selection = input("")
        if selection == '1':
            newCtRecord()
            break
        if selection == '2':
            menu()
            break
        if selection == '3':
            toggleCTSettings()
            break

def printRecords():
    i = 1
    header = recordHeader(globalSettings.admin, globalSettings.employer, globalSettings.sync, globalSettings.version, globalSettings.date, globalSettings.time)
    header.printHeader()
    for record in recordList:
        if(record.recordType == 'CT'):
            print('[{}]{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(i, record.recordType, record.participantID, record.planName, record.contributionDate, record.contributionDescription, record.ContributionAmount, record.amountType, record.taxYear, record.notes, record.planStartDate, record.planEndDate, record.lastName, record.firstName))
        i += 1
    footer = recordFooter(globalSettings.admin, globalSettings.employer, globalSettings.date, globalSettings.time)
    footer.printFooter()

def deleteRecord():
    try:
        record = int(input("Delete record number: "))
        if(record < 1):
            menu()
    except ValueError:
        print("Not a valid number!")
        menu()
    try:
        record -= 1
        print(record)
        del recordList[record]
        menu()
    except IndexError:
        print("Record does not exist!")
        menu()

def modifyAdminSettings():
    while True:
        printAdminSettings()
        print("1. Change admin  2. Change employer  3. Change sync flag  4. Change version  5. Return to previous menu")
        selection = input()
        if selection == '1':
            changeAdmin()
            break
        if selection == '2':
            changeEmployer()
            break
        if selection == '3':
            changeSyncFlag()
            break
        if selection == '4':
            changeVersion()
            break
        if selection == '5':
            menu()
            break


#Program flow
globalSettings = globalSettings()
inputValidation = inputValidation()

getSettings()
menu()