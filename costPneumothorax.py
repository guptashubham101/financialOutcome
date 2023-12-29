from prettytable import PrettyTable
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
encoding = 'unicode_escape'

def loadData(name):
    # Use a breakpoint in the code line below to debug your script.
    return pd.read_csv(name, encoding='unicode_escape')

def loadExcel(name):
    # Use a breakpoint in the code line below to debug your script.
    return pd.ExcelFile(name)

def isnan(value):
    if value == '':
        return True
    try:
        import math
        if math.isnan(float(value)):
            return True
        else:
            return False
    except:
        return False

def DRFCodeDistribution(drgList):
    sepsisICD = ['P36', 'R65.21', 'P83.0']
    necICD = ['P77']
    hypothermiaICD = ['P80.8', 'P80.9', 'P81.0', 'P81.8', 'P81.9']
    ropICD = ['H35', 'H57']
    bpdICD = ['P27.1', 'P27.8', 'P27.9']

    rdsICD = ['P22.0', 'P22.1', 'P22.8', 'P22.9', 'P28.5', 'P28.89', 'P28.9']
    jaundiceICD = ['P58.3', 'P59.0', 'P59.3', 'P59.8', 'P59.9', 'P80.9', 'P81.8', 'R17']
    cvsICD = ['G93.89', 'I25.3', 'I27.21', 'I31.3', 'I42.4', 'I42.7', 'I45.6', 'I45.81', 'I45.89', 'I47.1', 'I48.92',
              'I49.9', 'I95.89', 'I95.9', 'P29.89']
    giICD = ['J95.2', 'K00.6', 'K31.82', 'K42.9', 'K55.021', 'K55.069', 'K56.2', 'K60.2', 'K65.1', 'K73.9', 'K83.1',
             'K90.9', 'K91.2', 'K91.89', 'P01.3', 'P24.31', 'P74.1', 'P76.0', 'P76.1', 'P76.8', 'P76.9', 'P78.0',
             'P78.2', 'P78.83', 'P78.89', 'P92.01', 'P92.09', 'P92.1', 'P92.3', 'R13.10', 'R13.19', 'R16.0', 'R18.8',
             'R62.51', 'R63.3', 'R63.4']
    hemorrhageICD = ['P12.2', 'P12.3', 'P26.1', 'P26.8', 'P26.9', 'P52.0', 'P52.1', 'P52.21', 'P52.22', 'P52.3',
                     'P52.4', 'P52.5', 'P52.6', 'P52.8', 'P52.9', 'P54.5']
    asphyxiaICD = ['P03.810', 'P03.811', 'P03.82', 'P24.21', 'P71.1', 'P91.4', 'P96.83']
    apneaICD = ['P28.3', 'P28.4', 'R06.3']
    hypoglycemiaICD = ['E16.1', 'P70.0', 'P70.1', 'P70.3', 'P70.4', 'P80.9', 'P81.9', 'P70.2', 'P81.9']
    pphnICD = ['P29.2', 'P29.30']
    pneumothoraxICD = ['P25.1']
    hieICD = ['P91.60', 'P91.61', 'P91.62', 'P91.63']
    otherICD = ['P94.0','Z20.6','P61.0','P04.14','P96.1','T80.89XA','D18.09','P55.1','P94.2','P04.9','P29.12','Z05.1','B09','Z05.42','P04.49','Z20.828','P04.18','P92.9']

    congenital_HeadFootFingersRibsLimbsICD = ['Q01.2', 'Q02', 'Q65.9', 'Q66.02', 'Q66.89', 'Q66.91', 'Q67.3', 'Q67.4',
                                              'Q69.0', 'Q69.9', 'Q70.9', 'Q75.3', 'Q76.6', 'Q79.0', 'Q79.8', 'Q87.1',
                                              'Q87.2', 'Q87.3', 'Q87.89']
    congenital_brainICD = ['Q03.1', 'Q03.8', 'Q03.9', 'Q04.0', 'Q04.3', 'Q04.4', 'Q04.6', 'Q04.8', 'Q04.9', 'P91.2']
    congenital_spinalICD = ['Q05.7', 'Q05.8', 'Q05.9', 'Q06.8', 'Q07.03', 'Q07.9', 'Q10.5']
    congenital_sensoryOrgansICD = ['Q16.1', 'Q17.0', 'Q17.2', 'Q17.4', 'Q17.5', 'Q17.8', 'Q18.0', 'Q20.1', 'Q30.0',
                                   'Q30.1', 'Q30.2', 'Q81.9', 'Q82.5', 'Q82.6', 'Q82.8', 'Q86.0']
    congenital_cardiacICD = ['Q20.3', 'Q20.4', 'Q20.8', 'Q21.0', 'Q21.1', 'Q21.2', 'Q21.3', 'Q22.0', 'Q22.1', 'Q22.2',
                             'Q22.4', 'Q22.5', 'Q22.8', 'Q23.0', 'Q23.1', 'Q23.2', 'Q23.3', 'Q23.4', 'Q24.0', 'Q24.5',
                             'Q24.8', 'Q24.9', 'Q25.0', 'Q25.1', 'Q25.21', 'Q25.29', 'Q25.42', 'Q25.43', 'Q25.47',
                             'Q25.49', 'Q25.5', 'Q25.6', 'Q25.79', 'Q26.1', 'Q26.3', 'Q28.3']
    congenital_renalDiseaseICD = ['Q27.0', 'Q27.2', 'Q27.8', 'Q60.0', 'Q60.3', 'Q61.02', 'Q61.3', 'Q61.4', 'Q62.0',
                                  'Q62.32', 'Q62.39', 'Q62.7', 'Q63.0', 'Q63.1', 'Q63.8', 'Q64.2', 'Q64.31', 'Q64.73']
    congenital_esophagusICD = ['Q31.5', 'Q39.0', 'Q39.1', 'Q39.2', 'Q39.3']
    congenital_lungICD = ['Q33.0', 'Q33.2', 'Q33.6', 'Q33.8']
    congenital_intestineICD = ['Q40.1', 'Q41.0', 'Q41.1', 'Q41.2', 'Q42.2', 'Q42.3', 'Q42.9', 'Q43.1', 'Q43.3', 'Q43.8']
    congenital_genitalICD = ['Q43.7', 'Q52.3', 'Q52.4', 'Q53.10', 'Q53.112', 'Q53.20', 'Q53.9', 'Q54.0', 'Q54.1',
                             'Q54.4', 'Q54.8', 'Q54.9', 'Q55.29', 'Q55.62', 'Q55.64']
    congenital_liverICD = ['Q44.2', 'Q44.3', 'Q44.7']
    congenital_chestICD = ['Q67.7']
    congenital_diaphragmICD = ['Q79.1']
    congenital_digestiveICD = ['Q79.2', 'Q79.3', 'Q79.59']
    congenital_downeSyndromeICD = ['Q90.0', 'Q90.9', 'Q91.3', 'Q92.8']
    congenital_chromosome_abnormalitiesICD = ['Q93.3', 'Q93.81', 'Q93.88', 'Q96.9', 'Q99.8']
    los = []
    surfactantList = ['HC SURFACTANT ADMINISTRATION',
                      'SURFACTANT ADMIN THRU TUBE', 'PORACTANT ALFA 120 MG/1.5 ML SUSPENSION',
                      'PORACTANT ALFA 80 MG/ML SUSP', 'PORACTANT ALFA 240 MG/3 ML SUSPENSION']

    surfactantListAgePneumo = []
    surfactantListAgePneumoNon = []
    totalCostPneumothorax = []
    totalCostNoPneumothorax = []
    pneumoPatients = []
    pneumoNonPatients = []

    pneumoMechDays = []
    pneumoNonMechDays = []
    pneumoCPAPDays = []
    pneumoNonCPAPDays = []

    nonInvasiveList = ['HC NONINVASIVE VENTILATION/CPAP SUBSEQUENT DAY',
                       'HC NONINVASIVE VENTILATION/CPAP SETTING OR DEVICE ADJUSTMENT',
                       'HC NONINVASIVE VENTILATION/CPAP PATIENT/SYSTEM ASSESSMENT',
                       'HC NONINVASIVE VENTILATION/CPAP FIRST DAY',
                       'HC NONINVASIVE VENTILATION/CPAP SET UP',
                       'HC NONINVASIVE VENTILATON/CPAP EQUIPMENT CHANGE', 'HC HFOV CIRCUIT',
                       'HC HIGH FLOW THERAPY EQUIPMENT CHANGE', 'HC HIGH FLOW OXYGEN DAILY',
                       'HC HIGH FLOW THERAPY PATIENT/SYSTEM ASSESSMENT', 'HC HIGH FLOW THERAPY SYSTEM SET UP',
                       'CPAP/BIPAP, DAILY', 'HC HOME CPAP MANAGEMENT DAILY']

    mechList = ['HC MECHANICAL VENTILATION SUBSEQUENT DAY',
                'HC MECHANICAL VENTILATION PATIENT/SYSTEM ASSESSMENT',
                'HC MECHANICAL VENTILATION SETTING ADJUSTMENT',
                'HC MECHANICAL VENTILATION PRONE POSITIONING',
                'HC MECHANICAL VENTILATION CIRCUIT/EQUIPMENT CHANGE',
                'HC MECHANICAL VENTILATION SWITCH ENTIRE VENTILATOR',
                'HC MECHANICAL VENTILATION FIRST DAY',
                'HC MECHANICAL VENTILATION SET UP']

    for code in drgList:
        patientRows = patientMaster[patientMaster['APRDRG Code'] == code]

        for index, row in patientRows.iterrows():
            surfactantDate = None
            dictDates = {}
            dictDatesCPAP = {}
            dictDatesMech = {}
            value1 = ''
            value2 = ''
            value3 = ''
            value4 = ''
            value5 = ''
            if (not isnan(row['ICD1'])):
                value1 = row['ICD1']
            if (not isnan(row['ICD2'])):
                value2 = row['ICD2']
            if (not isnan(row['ICD3'])):
                value3 = row['ICD3']
            if (not isnan(row['ICD4'])):
                value4 = row['ICD4']
            if (not isnan(row['ICD5'])):
                value5 = row['ICD5']

            if (row['DISPOSITION'] != 'Discharged to Home or Self Care (Routine Discharge)'):
                continue
            isCongenital = False
            for code in congenital_HeadFootFingersRibsLimbsICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_brainICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_spinalICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_sensoryOrgansICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_cardiacICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_renalDiseaseICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_esophagusICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_lungICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_intestineICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_genitalICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_liverICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_chestICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_diaphragmICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_digestiveICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_downeSyndromeICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            for code in congenital_chromosome_abnormalitiesICD:
                if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                        code) or value4.__contains__(code) or value5.__contains__(code)):
                    isCongenital = True
                    break
            if (isCongenital):
                continue

            mrn = row['Hashed MRN']
            encounterRows = encounterofPatients[encounterofPatients['Hashed MRN'] == mrn]
            if (len(encounterRows) > 0 and row['Total_Direct_Variable_Cost'] > 0 and row['APRDRG Code'] != 'NO DATA'):

                isSurfactant = False
                isMechanical = False
                isCPAP = False
                isApnea = False
                isPPHN = False
                isPneumo = False
                isRDS = False
                isIVH = False
                isBPD = False
                isSepsis = False
                isNEC = False
                isOther = False
                isHypothermia = False
                isrop = False
                isJaundice = False
                isCVS = False
                isGI = False
                isAsphyxia = False
                isHypoglycemia = False
                isHie = False
                currMechDays = 0
                currCPAPDays = 0
                isPatientICD = False

                for code in hypothermiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isHypothermia = True
                        break

                for code in sepsisICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isSepsis = True
                        break

                for code in necICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isNEC = True
                        break
                for code in ropICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isrop = True
                        break
                for code in bpdICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isBPD = True
                        break
                for code in rdsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isRDS = True
                        break
                for code in jaundiceICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isJaundice = True
                        break
                for code in cvsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isCVS = True
                        break
                for code in giICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isGI = True
                        break
                for code in hemorrhageICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isIVH = True
                        break
                for code in asphyxiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isAsphyxia = True
                        break
                for code in apneaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isApnea = True
                        break
                for code in hypoglycemiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isHypoglycemia = True
                        break
                for code in hieICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isHie = True
                        break
                for code in pphnICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isPPHN = True
                        break
                for code in pneumothoraxICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPneumo = True
                        break
                for code in otherICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        isOther = True
                        break

                los.append(row['LOS'])

                for index1, encounter in encounterRows.iterrows():

                    if (encounter['Total Direct Variable Cost'] > 0):
                        dictDates[encounter['Service Dt']] = 1
                        dictDatesCPAP[encounter['Service Dt']] = False
                        dictDatesMech[encounter['Service Dt']] = False
                        isAnyVentPresent = False
                        if (encounter['Activity Desc'] in nonInvasiveList):
                            isCPAP = True

                        if (encounter['Activity Desc'] in mechList):
                            isMechanical = True

                        if (encounter['Activity Desc'] in surfactantList):
                            isSurfactant = True
                            if (surfactantDate is None):
                                surfactantDate = encounter['Service Dt']
                        if (isAnyVentPresent):
                            dictDates[encounter['Service Dt']] = True
                dictDatesList = [i for i in dictDates]
                dictDatesList.sort()

                for index1, encounter in encounterRows.iterrows():
                    if (encounter['Total Direct Variable Cost'] > 0 and encounter['Service Dt'] in dictDates and
                            dictDates[encounter['Service Dt']]):
                        if (encounter['Activity Desc'] in nonInvasiveList and not dictDatesCPAP[
                            encounter['Service Dt']]):
                            dictDatesCPAP[encounter['Service Dt']] = True
                            currCPAPDays = currCPAPDays + 1
                        if ((encounter['Activity Desc'] in mechList) and not dictDatesMech[encounter['Service Dt']]):
                            dictDatesMech[encounter['Service Dt']] = True
                            currMechDays = currMechDays + 1



                if isSurfactant and isRDS:
                    if (isPneumo):

                        if (not isPatientICD):
                            surfactantListAgePneumo.append((surfactantDate - dictDatesList[0]).days)
                            totalCostPneumothorax.append(sum(encounterRows['Total Direct Variable Cost']))
                            pneumoPatients.append(row['Hashed MRN'])
                            if isMechanical:
                                pneumoMechDays.append(currMechDays)

                            if isCPAP:
                                pneumoCPAPDays.append(currCPAPDays)

                    else:
                        if (not isPatientICD):
                            pneumoNonPatients.append(row['Hashed MRN'])
                            surfactantListAgePneumoNon.append((surfactantDate - dictDatesList[0]).days)
                            totalCostNoPneumothorax.append(sum(encounterRows['Total Direct Variable Cost']))

                            if isMechanical:
                                pneumoNonMechDays.append(currMechDays)

                            if isCPAP:
                                pneumoNonCPAPDays.append(currCPAPDays)


    pneumoDict = {}
    pneumoDict['Pneumo Count'] = len(surfactantListAgePneumo)
    pneumoDict['Non Pneumo Count'] = len(surfactantListAgePneumoNon)
    if(len(surfactantListAgePneumo)):
        pneumoDict['Age Surfactant Given Pneumo'] = round(sum(surfactantListAgePneumo)/len(surfactantListAgePneumo),2)
    else:
        pneumoDict['Age Surfactant Given Pneumo'] = '-'
    if (len(surfactantListAgePneumoNon)):
        pneumoDict['Age Surfactant Given Non Pneumo'] = round(sum(surfactantListAgePneumoNon) / len(surfactantListAgePneumoNon),2)
    else:
        pneumoDict['Age Surfactant Given Non Pneumo'] = '-'

    if (len(totalCostPneumothorax) > 0):
        pneumoDict['Pneumo Cost per patient in K'] = round(sum(totalCostPneumothorax) / len(totalCostPneumothorax)/1000)
    else:
        pneumoDict['Pneumo Cost per patient in K'] = 0
    if (len(totalCostNoPneumothorax) > 0):
        pneumoDict['Non Pneumo Cost per patient in K'] = round(sum(totalCostNoPneumothorax) / len(totalCostNoPneumothorax)/1000)
    else:
        pneumoDict['Non Pneumo Cost per patient in K'] = 0

    if (len(pneumoMechDays)) > 0:
        pneumoDict['Pneumo Mech Vent Days'] =  round(sum(pneumoMechDays) / len(pneumoMechDays),2)
    else:
        pneumoDict['Pneumo Mech Vent Days'] =  '-'
    if (len(pneumoNonMechDays)) > 0:
        pneumoDict['Non Pneumo Mech Vent Days'] =  round(sum(pneumoNonMechDays) / len(pneumoNonMechDays),2)
    else:
        pneumoDict['Non Pneumo Mech Vent Days'] =  '-'

    if (len(pneumoCPAPDays)) > 0:
        pneumoDict['Pneumo CPAP Vent Days'] =  round(sum(pneumoCPAPDays) / len(pneumoCPAPDays),2)
    else:
        pneumoDict['Pneumo CPAP Vent Days'] =  '-'

    if (len(pneumoNonCPAPDays)) > 0:
        pneumoDict['Non Pneumo CPAP Vent Days'] =  round(sum(pneumoNonCPAPDays) / len(pneumoNonCPAPDays),2)
    else:
        pneumoDict['Non Pneumo CPAP Vent Days'] =  '-'

    return pneumoDict


excelPathHospitalCost = 'Hospital Costs.xlsx'
providerCost = loadData('451502252_texas-health-harris-methodist-hospital-alliance_standardcharges 10-28-22.csv')
hospitalCostExcel = loadExcel(excelPathHospitalCost)
patientMaster = hospitalCostExcel.parse("PatientMaster")
encounterofPatients = hospitalCostExcel.parse("Encounter Level")
itemizedFinancials = hospitalCostExcel.parse("Financials Itemized")

drgCodeGreaterthan500Lessthan750 = [591]
drgCodeGreaterthan750Lessthan1000 = [593]
drgCodeLessthan1000 = [589, 593, 591]
drgCodeLessthan1000Only = [589]
drgCodeGreaterthan1000Lessthan1250 = [602, 603]
drgCodeGreaterthan1250Lessthan1500 = [607, 608]
drgCodeLessthan1500 = [588, 607, 602, 593, 591, 589, 608, 603]
drgCodeLessthan1500Only = [588]
drgCodeGreaterthan1500Lessthan2000 = [614, 612, 611, 613]
drgCodeGreaterthan2000Lessthan2500 = [626, 622, 625, 621, 623]
drgCodeGreaterthan1500Lessthan2500 = [609, 614, 612, 611, 613, 626, 622, 625, 621, 623]
drgCodeGreaterthan1500Lessthan2500Only = [609]
drgCodeLessthan2500 = [626, 622, 625, 621, 623, 609, 614, 612, 611, 613, 588, 607, 602, 593, 591, 589, 608, 603]
drgCodeGreaterthan2500 = [640, 634, 639, 633, 631, 636]
drgAll = [626, 622, 625, 621, 623, 609, 614, 612, 611, 613, 588, 607, 602, 593, 591, 589, 608, 603, 640, 634, 639, 633,
          631, 636]

pneumothoraxTable1 = DRFCodeDistribution(drgCodeGreaterthan500Lessthan750)
pneumothoraxTable2 = DRFCodeDistribution(drgCodeGreaterthan750Lessthan1000)
pneumothoraxTable3 = DRFCodeDistribution(drgCodeLessthan1000Only)
pneumothoraxTable4 = DRFCodeDistribution(drgCodeLessthan1000)
pneumothoraxTable5 = DRFCodeDistribution(drgCodeGreaterthan1000Lessthan1250)
pneumothoraxTable6 = DRFCodeDistribution(drgCodeGreaterthan1250Lessthan1500)
pneumothoraxTable7 = DRFCodeDistribution(drgCodeLessthan1500Only)
pneumothoraxTable8 = DRFCodeDistribution(drgCodeLessthan1500)
pneumothoraxTable9 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2000)
pneumothoraxTable10 = DRFCodeDistribution(drgCodeGreaterthan2000Lessthan2500)
pneumothoraxTable11 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500Only)
pneumothoraxTable12 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500)
pneumothoraxTable13 = DRFCodeDistribution(drgCodeGreaterthan2500)
pneumothoraxTable14 = DRFCodeDistribution(drgAll)

pneumothoraxTable = PrettyTable(["Weight categories (gm)",
    "Total Count",
    "Pneumothorax Count",
    "Non Pneumothorax Count",
    "Pneumothorax Age at Surfactant Given",
    "Non Pneumothorax Age at Surfactant Given",
    "Pneumothorax Total Average Cost in K",
    "Non Pneumothorax Total Average Cost in K",
    "Pneumothorax Mech",
    "Non Pneumothorax Mech",
    "Pneumothorax CPAP Days",
    "Non Pneumothorax CPAP Days",
     ])


pneumothoraxTable.add_row(['500-750', pneumothoraxTable1['Pneumo Count'] + pneumothoraxTable1['Non Pneumo Count'], pneumothoraxTable1['Pneumo Count'], pneumothoraxTable1['Non Pneumo Count'],
      pneumothoraxTable1['Age Surfactant Given Pneumo'], pneumothoraxTable1['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable1['Pneumo Cost per patient in K'], pneumothoraxTable1['Non Pneumo Cost per patient in K'], pneumothoraxTable1['Pneumo Mech Vent Days'],
      pneumothoraxTable1['Non Pneumo Mech Vent Days'], pneumothoraxTable1['Pneumo CPAP Vent Days'], pneumothoraxTable1['Non Pneumo CPAP Vent Days']])

pneumothoraxTable.add_row(['750-1000', pneumothoraxTable2['Pneumo Count'] + pneumothoraxTable2['Non Pneumo Count'], pneumothoraxTable2['Pneumo Count'], pneumothoraxTable2['Non Pneumo Count'],
      pneumothoraxTable2['Age Surfactant Given Pneumo'], pneumothoraxTable2['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable2['Pneumo Cost per patient in K'], pneumothoraxTable2['Non Pneumo Cost per patient in K'], pneumothoraxTable2['Pneumo Mech Vent Days'],
      pneumothoraxTable2['Non Pneumo Mech Vent Days'], pneumothoraxTable2['Pneumo CPAP Vent Days'], pneumothoraxTable2['Non Pneumo CPAP Vent Days']])

pneumothoraxTable.add_row(['<1000', pneumothoraxTable3['Pneumo Count'] + pneumothoraxTable3['Non Pneumo Count'],pneumothoraxTable3['Pneumo Count'], pneumothoraxTable3['Non Pneumo Count'],
      pneumothoraxTable3['Age Surfactant Given Pneumo'], pneumothoraxTable3['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable3['Pneumo Cost per patient in K'], pneumothoraxTable3['Non Pneumo Cost per patient in K'], pneumothoraxTable3['Pneumo Mech Vent Days'],
      pneumothoraxTable3['Non Pneumo Mech Vent Days'], pneumothoraxTable3['Pneumo CPAP Vent Days'], pneumothoraxTable3['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['Total 500-1000', pneumothoraxTable4['Pneumo Count'] + pneumothoraxTable4['Non Pneumo Count'],pneumothoraxTable4['Pneumo Count'], pneumothoraxTable4['Non Pneumo Count'],
      pneumothoraxTable4['Age Surfactant Given Pneumo'], pneumothoraxTable4['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable4['Pneumo Cost per patient in K'], pneumothoraxTable4['Non Pneumo Cost per patient in K'], pneumothoraxTable4['Pneumo Mech Vent Days'],
      pneumothoraxTable4['Non Pneumo Mech Vent Days'], pneumothoraxTable4['Pneumo CPAP Vent Days'], pneumothoraxTable4['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['1000-1250', pneumothoraxTable5['Pneumo Count'] + pneumothoraxTable5['Non Pneumo Count'],pneumothoraxTable5['Pneumo Count'], pneumothoraxTable5['Non Pneumo Count'],
      pneumothoraxTable5['Age Surfactant Given Pneumo'], pneumothoraxTable5['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable5['Pneumo Cost per patient in K'], pneumothoraxTable5['Non Pneumo Cost per patient in K'], pneumothoraxTable5['Pneumo Mech Vent Days'],
      pneumothoraxTable5['Non Pneumo Mech Vent Days'], pneumothoraxTable5['Pneumo CPAP Vent Days'], pneumothoraxTable5['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['1250-1500', pneumothoraxTable6['Pneumo Count'] + pneumothoraxTable6['Non Pneumo Count'],pneumothoraxTable6['Pneumo Count'], pneumothoraxTable6['Non Pneumo Count'],
      pneumothoraxTable6['Age Surfactant Given Pneumo'], pneumothoraxTable6['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable6['Pneumo Cost per patient in K'], pneumothoraxTable6['Non Pneumo Cost per patient in K'], pneumothoraxTable6['Pneumo Mech Vent Days'],
      pneumothoraxTable6['Non Pneumo Mech Vent Days'], pneumothoraxTable6['Pneumo CPAP Vent Days'], pneumothoraxTable6['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['<1500', pneumothoraxTable7['Pneumo Count'] + pneumothoraxTable7['Non Pneumo Count'],pneumothoraxTable7['Pneumo Count'], pneumothoraxTable7['Non Pneumo Count'],
      pneumothoraxTable7['Age Surfactant Given Pneumo'], pneumothoraxTable7['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable7['Pneumo Cost per patient in K'], pneumothoraxTable7['Non Pneumo Cost per patient in K'], pneumothoraxTable7['Pneumo Mech Vent Days'],
      pneumothoraxTable7['Non Pneumo Mech Vent Days'], pneumothoraxTable7['Pneumo CPAP Vent Days'], pneumothoraxTable7['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['Total 500-1500', pneumothoraxTable8['Pneumo Count'] + pneumothoraxTable8['Non Pneumo Count'],pneumothoraxTable8['Pneumo Count'], pneumothoraxTable8['Non Pneumo Count'],
      pneumothoraxTable8['Age Surfactant Given Pneumo'], pneumothoraxTable8['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable8['Pneumo Cost per patient in K'], pneumothoraxTable8['Non Pneumo Cost per patient in K'], pneumothoraxTable8['Pneumo Mech Vent Days'],
      pneumothoraxTable8['Non Pneumo Mech Vent Days'], pneumothoraxTable8['Pneumo CPAP Vent Days'], pneumothoraxTable8['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['1500-2000', pneumothoraxTable9['Pneumo Count'] + pneumothoraxTable9['Non Pneumo Count'],pneumothoraxTable9['Pneumo Count'], pneumothoraxTable9['Non Pneumo Count'],
      pneumothoraxTable9['Age Surfactant Given Pneumo'], pneumothoraxTable9['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable9['Pneumo Cost per patient in K'], pneumothoraxTable9['Non Pneumo Cost per patient in K'], pneumothoraxTable9['Pneumo Mech Vent Days'],
      pneumothoraxTable9['Non Pneumo Mech Vent Days'], pneumothoraxTable9['Pneumo CPAP Vent Days'], pneumothoraxTable9['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['2000-2500', pneumothoraxTable10['Pneumo Count'] + pneumothoraxTable10['Non Pneumo Count'],pneumothoraxTable10['Pneumo Count'], pneumothoraxTable10['Non Pneumo Count'],
      pneumothoraxTable10['Age Surfactant Given Pneumo'], pneumothoraxTable10['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable10['Pneumo Cost per patient in K'], pneumothoraxTable10['Non Pneumo Cost per patient in K'], pneumothoraxTable10['Pneumo Mech Vent Days'],
      pneumothoraxTable10['Non Pneumo Mech Vent Days'], pneumothoraxTable10['Pneumo CPAP Vent Days'], pneumothoraxTable10['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['1500-2500', pneumothoraxTable11['Pneumo Count'] + pneumothoraxTable11['Non Pneumo Count'],pneumothoraxTable11['Pneumo Count'], pneumothoraxTable11['Non Pneumo Count'],
      pneumothoraxTable11['Age Surfactant Given Pneumo'], pneumothoraxTable11['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable11['Pneumo Cost per patient in K'], pneumothoraxTable11['Non Pneumo Cost per patient in K'], pneumothoraxTable11['Pneumo Mech Vent Days'],
      pneumothoraxTable11['Non Pneumo Mech Vent Days'], pneumothoraxTable11['Pneumo CPAP Vent Days'], pneumothoraxTable11['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['Total 1500-2500', pneumothoraxTable12['Pneumo Count'] + pneumothoraxTable12['Non Pneumo Count'],pneumothoraxTable12['Pneumo Count'], pneumothoraxTable12['Non Pneumo Count'],
      pneumothoraxTable12['Age Surfactant Given Pneumo'], pneumothoraxTable12['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable12['Pneumo Cost per patient in K'], pneumothoraxTable12['Non Pneumo Cost per patient in K'], pneumothoraxTable12['Pneumo Mech Vent Days'],
      pneumothoraxTable12['Non Pneumo Mech Vent Days'], pneumothoraxTable12['Pneumo CPAP Vent Days'], pneumothoraxTable12['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['>2500', pneumothoraxTable13['Pneumo Count'] + pneumothoraxTable13['Non Pneumo Count'],pneumothoraxTable13['Pneumo Count'], pneumothoraxTable13['Non Pneumo Count'],
      pneumothoraxTable13['Age Surfactant Given Pneumo'], pneumothoraxTable13['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable13['Pneumo Cost per patient in K'], pneumothoraxTable13['Non Pneumo Cost per patient in K'], pneumothoraxTable13['Pneumo Mech Vent Days'],
      pneumothoraxTable13['Non Pneumo Mech Vent Days'], pneumothoraxTable13['Pneumo CPAP Vent Days'], pneumothoraxTable13['Non Pneumo CPAP Vent Days']])
pneumothoraxTable.add_row(['All', pneumothoraxTable14['Pneumo Count'] + pneumothoraxTable14['Non Pneumo Count'],pneumothoraxTable14['Pneumo Count'], pneumothoraxTable14['Non Pneumo Count'],
      pneumothoraxTable14['Age Surfactant Given Pneumo'], pneumothoraxTable14['Age Surfactant Given Non Pneumo'],
      pneumothoraxTable14['Pneumo Cost per patient in K'], pneumothoraxTable14['Non Pneumo Cost per patient in K'], pneumothoraxTable14['Pneumo Mech Vent Days'],
      pneumothoraxTable14['Non Pneumo Mech Vent Days'], pneumothoraxTable14['Pneumo CPAP Vent Days'], pneumothoraxTable14['Non Pneumo CPAP Vent Days']])



print(pneumothoraxTable)
