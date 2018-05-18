from datetime import *
from decimal import *
import configparser
import sys



class globalSettings():
    #Global admin settings
    admin = "EV1"
    employer = "SSB23"
    sync = "Y"
    date = date.today().strftime("%m%d%Y")
    time = datetime.now().strftime("%I%M%S")
    version = "1.0"

class ctRecordSettings():
    taxYearToggle = False
    notesToggle = False
    planStartDateToggle = False
    planEndDateToggle = False
    lastNameToggle = False
    firstNameToggle = False

class enRecordSettings():
    enrollmentTerminationDateToggle = False
    employerContributionLevelToggle = False
    employerContributionAmountToggle = False
    primaryReimbursmentToggle = False
    alternateReimbursmentToggle = False
    enrolledInClaimsPackageToggle = False
    electionAmountIndicatorToggle = False
    hdapCoverageLevelToggle = False
    planYearStartDateToggle = False
    termsAcceptedToggle = False
    dateTermsAcceptedToggle = False
    timeTermsAcceptedToggle = False
    changeDateToggle = False
    spendDownToggle = False

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

class enRecord:
    def __init__(self, participantID, planName, enrollmentEffectiveDate, participantElectionAmount, enrollmentTerminationDate, employerContributionLevel, employerContributionAmount, primaryReimbursment, alternateReimbursment, enrolledInClaimsPackage, electionAmountIndicator, hdapCoverageLevel, planYearStartDate, termsAccepted, dateTermsAccepted, timeTermsAccepted, changeDate, spendDown):
        self.recordType = 'EN'
        self.participantID = participantID
        self.planName = planName
        self.enrollmentEffectiveDate = enrollmentEffectiveDate
        self.participantElectionAmount = participantElectionAmount
        self.enrollmentTerminationDate = enrollmentTerminationDate
        self.employerContributionLevel = employerContributionLevel
        self.employerContributionAmount = employerContributionAmount
        self.primaryReimbursment = primaryReimbursment
        self.alternateReimbursment = alternateReimbursment
        self.enrolledInClaimsPackage = enrolledInClaimsPackage
        self.electionAmountIndicator = electionAmountIndicator
        self.hdapCoverageLevel = hdapCoverageLevel
        self.planYearStartDate = planYearStartDate
        self.termsAccepted = termsAccepted
        self.dateTermsAccepted = dateTermsAccepted
        self.timeTermsAccepted = timeTermsAccepted
        self.changeDate = changeDate
        self.spendDown = spendDown

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
            if(x == ''):
                return ''
            date = datetime.strptime(datestring, '%m%d%Y')
        except:
            print("Invalid date. Proper format for date is MMDDYYYY.")
            datestring = inputValidation.dateValidation(input(""))
        return datestring
        

def getSettings():

    def getCtRecordSettings():
        ctRecordSettings.taxYearToggle = config.getboolean('ctRecordSettings', 'taxYearToggle')
        ctRecordSettings.notesToggle = config.getboolean('ctRecordSettings', 'notesToggle')
        ctRecordSettings.planStartDateToggle = config.getboolean('ctRecordSettings', 'planStartDateToggle')
        ctRecordSettings.planEndDateToggle = config.getboolean('ctRecordSettings', 'planEndDateToggle')
        ctRecordSettings.lastNameToggle = config.getboolean('ctRecordSettings', 'lastNameToggle')
        ctRecordSettings.firstNameToggle = config.getboolean('ctRecordSettings', 'firstNameToggle')
        print('CT Config Loaded.')

    def getEnRecordSettings():
        enRecordSettings.participantElectionAmountToggle = config.getboolean('enRecordSettings', 'participantElectionAmountToggle')
        enRecordSettings.enrollmentTerminationDateToggle = config.getboolean('enRecordSettings', 'enrollmentTerminationDateToggle')
        enRecordSettings.employerContributionLevelToggle = config.getboolean('enRecordSettings', 'employerContributionLevelToggle')
        enRecordSettings.employerContributionAmountToggle = config.getboolean('enRecordSettings', 'employerContributionAmountToggle')
        enRecordSettings.primaryReimbursmentToggle = config.getboolean('enRecordSettings', 'primaryReimbursmentToggle')
        enRecordSettings.alternateReimbursmentToggle = config.getboolean('enRecordSettings', 'alternateReimbursmentToggle')
        enRecordSettings.enrolledInClaimsPackageToggle = config.getboolean('enRecordSettings', 'enrolledInClaimsPackageToggle')
        enRecordSettings.electionAmountIndicatorToggle = config.getboolean('enRecordSettings', 'electionAmountIndicatorToggle')
        enRecordSettings.hdapCoverageLevelToggle = config.getboolean('enRecordSettings', 'hdapCoverageLevelToggle')
        enRecordSettings.planYearStartDateToggle = config.getboolean('enRecordSettings', 'planYearStartDateToggle')
        enRecordSettings.termsAcceptedToggle = config.getboolean('enRecordSettings', 'termsAcceptedToggle')
        enRecordSettings.dateTermsAcceptedToggle = config.getboolean('enRecordSettings', 'dateTermsAcceptedToggle')
        enRecordSettings.timeTermsAcceptedToggle = config.getboolean('enRecordSettings', 'timeTermsAcceptedToggle')
        enRecordSettings.changeDateToggle = config.getboolean('enRecordSettings', 'changeDateToggle')
        enRecordSettings.spendDownToggle = config.getboolean('enRecordSettings', 'spendDownToggle')
        print('EN Config Loaded.')


    config = configparser.SafeConfigParser()

    try:
        config.read('config.ini')
        getCtRecordSettings()
        getEnRecordSettings()
    except IOError:
        print("Could not load configuration file(s). Using default settings.")

def toggleCTSettings():
    while True:
        toggles = ('Tax Year: {} | Notes: {} | Plan Start Date: {} | Plan End Date: {} | Last Name: {} | First Name: {} |').format(ctRecordSettings.taxYearToggle, ctRecordSettings.notesToggle, ctRecordSettings.planStartDateToggle, ctRecordSettings.planEndDateToggle, ctRecordSettings.lastNameToggle, ctRecordSettings.firstNameToggle)
        print(toggles)
        print(ctSettings)
        selection = input("")
        if selection == '1':
            ctRecordSettings.taxYearToggle = not ctRecordSettings.taxYearToggle
        if selection == '2':
            ctRecordSettings.notesToggle = not ctRecordSettings.notesToggle
        if selection == '3':
            ctRecordSettings.planStartDateToggle = not ctRecordSettings.planStartDateToggle
        if selection == '4':
            ctRecordSettings.planEndDateToggle = not ctRecordSettings.planEndDateToggle
        if selection == '5':
            ctRecordSettings.lastNameToggle = not ctRecordSettings.lastNameToggle
        if selection == '6':
            ctRecordSettings.firstNameToggle = not ctRecordSettings.firstNameToggle
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

def decrementCount():
    global recordCount
    recordCount -= 1

def menu():
    try:
        for key in sorted(options):
            print(key,'=> ',options[key].__name__)
        selection = input("=>")
        while True:
            options.get(selection,"")()
            selection = input("=>")
    except TypeError:
        menu()

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
        if(record.recordType == 'EN'):
            file.write('[{}]{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(i, record.recordType, record.participantID, record.planName, record.enrollmentEffectiveDate, record.participantElectionAmount, record.enrollmentTerminationDate, record.employerContributionLevel, record.employerContributionAmount, record.primaryReimbursment, record.alternateReimbursment, record.enrolledInClaimsPackage, record.electionAmountIndicator, record.hdapCoverageLevel, record.planYearStartDate, record.termsAccepted, record.dateTermsAccepted, record.timeTermsAccepted, record.changeDate, record.spendDown) + "\n")
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
    
    if ctRecordSettings.taxYearToggle == True:
        taxYear = input("Tax Year?")
    else:
        taxYear = ""
    
    if ctRecordSettings.notesToggle == True:
        notes = input("Notes?")
    else:
        notes = ""

    if ctRecordSettings.planStartDateToggle == True:
        planStartDate = inputValidation.dateValidation(input("Plan year start date?"))
    else:
        planStartDate = ""

    if ctRecordSettings.planEndDateToggle == True:
        planEndDate = inputValidation.dateValidation(input("Plan year end date?"))
    else:
        planEndDate = ""

    if ctRecordSettings.lastNameToggle == True:    
        lastName = input("Last name?")
    else:
        lastName = ""

    if ctRecordSettings.firstNameToggle == True:    
        firstName = input("First name?")
    else:
        firstName = ""

    record = ctRecord(participantID, planName, contributionDate, contributionDescription, contributionAmount, amountType, taxYear, notes, planStartDate, planEndDate, lastName, firstName)
    recordList.append(record)
    incrementCount()

    newRecord()

def newENRecord():
    participantID = input("Participant ID?")
    planName = input("Plan name?")
    enrollmentEffectiveDate = input("Enrollment effective date?")
    participantElectionAmount = input("Participant election amount?")

    if enRecordSettings.enrollmentTerminationDateToggle == True:
        enrollmentTerminationDate = input("Enrollment termination date?")
    else:
        enrollmentTerminationDate = ""

    if enRecordSettings.employerContributionLevelToggle == True:
        employerContributionLevel == input("Employer Contribution Level?")
    else:
        employerContributionLevel = ""

    if enRecordSettings.employerContributionAmountToggle == True:
        employerContributionAmount = input("Employer contribution amount?")
    else:
        employerContributionAmount = ""

    if enRecordSettings.primaryReimbursmentToggle == True:
        primaryReimbursment = input("Primary reimbursment method?")
    else:
        primaryReimbursment = ""

    if enRecordSettings.alternateReimbursmentToggle == True:
        alternateReimbursment = input("Alternate reimbursement method?")
    else:
        alternateReimbursment = ""
    
    if enRecordSettings.enrolledInClaimsPackageToggle == True:
        enrolledInClaimsPackage = input("Enrolled in claims package?")
    else:
        enrolledInClaimsPackage = ""

    if enRecordSettings.electionAmountIndicatorToggle == True:
        electionAmountIndicator = input("Election amount indicator?")
    else:
        electionAmountIndicator = ""

    if enRecordSettings.hdapCoverageLevelToggle == True:
        hdapCoverageLevel = input("HDAP coverage level?")
    else:
        hdapCoverageLevel = ""

    if enRecordSettings.planYearStartDateToggle == True:
        planYearStartDate = input("Plan year start date?")
    else:
        planYearStartDate = ""

    if enRecordSettings.termsAcceptedToggle == True:
        termsAccepted = input("Terms accepted?")
    else:
        termsAccepted = ""

    if enRecordSettings.dateTermsAcceptedToggle == True:
        dateTermsAccepted = input("Date terms were accepted?")
    else:
        dateTermsAccepted = ""

    if enRecordSettings.timeTermsAcceptedToggle == True:
        timeTermsAccepted = input("Time terms were accepted?")
    else:
        timeTermsAccepted = ""

    if enRecordSettings.changeDateToggle == True:
        changeDate = input("Change date?")
    else:
        changeDate = ""

    if enRecordSettings.spendDownToggle == True:
        spendDown = input("Spend down?")
    else:
        spendDown = ""

    record = enRecord(participantID, planName, enrollmentEffectiveDate, participantElectionAmount, enrollmentTerminationDate, employerContributionLevel, employerContributionAmount, primaryReimbursment, alternateReimbursment, enrolledInClaimsPackage, electionAmountIndicator, hdapCoverageLevel, planYearStartDate, termsAccepted, dateTermsAccepted, timeTermsAccepted, changeDate, spendDown)
    recordList.append(record)
    incrementCount()

    newRecord()
    
def newRecord():
    try:
        for key in sorted(recordOptions):
            print(key,'=>',recordOptions[key].__name__)
        selection = input("=>")
        while True:
            recordOptions.get(selection,"")()
            selection = input("=>")
    except TypeError:
        menu()

def quitProgram():
    print("quit")
    sys.exit(0)

def printRecords():
    i = 1
    header = recordHeader(globalSettings.admin, globalSettings.employer, globalSettings.sync, globalSettings.version, globalSettings.date, globalSettings.time)
    header.printHeader()
    for record in recordList:
        if(record.recordType == 'CT'):
            print('[{}]{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(i, record.recordType, record.participantID, record.planName, record.contributionDate, record.contributionDescription, record.ContributionAmount, record.amountType, record.taxYear, record.notes, record.planStartDate, record.planEndDate, record.lastName, record.firstName))
        if(record.recordType == 'EN'):
            print('[{}]{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(i, record.recordType, record.participantID, record.planName, record.enrollmentEffectiveDate, record.participantElectionAmount, record.enrollmentTerminationDate, record.employerContributionLevel, record.employerContributionAmount, record.primaryReimbursment, record.alternateReimbursment, record.enrolledInClaimsPackage, record.electionAmountIndicator, record.hdapCoverageLevel, record.planYearStartDate, record.termsAccepted, record.dateTermsAccepted, record.timeTermsAccepted, record.changeDate, record.spendDown))
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
        del recordList[record]
        decrementCount()
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

recordList = []
recordCount = 0
options = {'1':newRecord,'2':printRecords,'3':modifyAdminSettings,'4':exportToFile,'5':deleteRecord, '6':quitProgram}
recordOptions = {'1':newCtRecord,'2':toggleCTSettings,'3':newENRecord, '4':menu}#"1. New CT record \n2. Return \n3. Change CT Settings"
ctSettings = "1. Tax Year \n2. Notes \n3. Plan Start Date \n4. Plan End Date \n5. Last Name \n6. First Name \n7. Return to Previous Menu"

#Program flow
globalSettings = globalSettings()
ctRecordSettings = ctRecordSettings()
inputValidation = inputValidation()

getSettings()
menu()

