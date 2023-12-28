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
    if (value == ''):
        return True
    try:
        import math
        if (math.isnan(float(value))):
            return True
        else:
            return False
    except:
        return False

def DRFCodeDistribution(drgList):
    sepsisCases = []
    ApneaCases = []
    HypoglycemiaCases = []
    PPHNCases = []
    PneumothoraxCases = []
    necCases = []
    bpdCases = []
    hypothermiaCases = []
    ropCases = []
    rdsCases = []
    jaundiceCases = []
    cvsCases = []
    giCases = []
    hemorrhageCases = []
    asphyxiaCases = []
    HIECases = []

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

    congenital_HeadFootFingersRibsLimbsICD = ['Q01.2', 'Q02', 'Q65.9', 'Q66.02', 'Q66.89', 'Q66.91', 'Q67.3', 'Q67.4',
                                              'Q69.0', 'Q69.9', 'Q70.9', 'Q75.3', 'Q76.6', 'Q79.0', 'Q79.8', 'Q87.1',
                                              'Q87.2', 'Q87.3', 'Q87.89']
    congenital_brainICD = ['Q03.1', 'Q03.8', 'Q03.9', 'Q04.0', 'Q04.3', 'Q04.4', 'Q04.6', 'Q04.8', 'Q04.9','P91.2']
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

    totalCost = 0

    rdsTotalCost = []
    sepsisTotalCost = []
    bpdTotalCost = []
    necTotalCost = []
    ivhTotalCost = []
    pneumoTotalCost = []
    apneaTotalCost = []
    pphnTotalCost = []
    hypothermiaTotalCost = []
    ropTotalCost = []
    jaundiceTotalCost = []
    cvsTotalCost = []
    giTotalCost = []
    asphyxiaTotalCost = []
    hypoglycemiaTotalCost = []
    hieTotalCost = []
    los = []

    for code in drgList:
        patientRows = patientMaster[patientMaster['APRDRG Code'] == code]

        for index, row in patientRows.iterrows():

            isApnea = False
            isPPHN = False
            isPneumo = False
            isRDS = False
            isIVH = False
            isBPD = False
            isSepsis = False
            isNEC = False
            isHypothermia = False
            isROP = False
            isJaundice = False
            isCVS = False
            isGI = False
            isAsphyxia = False
            isHypoglycemia = False
            isHie = False

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
            if(isCongenital):
                continue
            mrn = row['Hashed MRN']
            encounterRows = encounterofPatients[encounterofPatients['Hashed MRN'] == mrn]
            if (len(encounterRows) > 0 and row['Total_Direct_Variable_Cost'] > 0 and row['APRDRG Code'] != 'NO DATA'):
                los.append(row['LOS'])
                totalCost = totalCost + sum(encounterRows['Total Direct Variable Cost'])

                for code in hypothermiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isHypothermia = True
                        hypothermiaCases.append(row['PatientID'])
                        break
                for code in sepsisICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isSepsis = True
                        sepsisCases.append(row['PatientID'])
                        break
                for code in necICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isNEC = True
                        necCases.append(row['PatientID'])
                        break
                for code in ropICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isROP = True
                        ropCases.append(row['PatientID'])
                        break
                for code in bpdICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isBPD = True
                        bpdCases.append(row['PatientID'])
                        break
                for code in rdsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isRDS = True
                        rdsCases.append(row['PatientID'])
                        break
                for code in jaundiceICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isJaundice = True
                        jaundiceCases.append(row['PatientID'])
                        break
                for code in cvsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isCVS = True
                        cvsCases.append(row['PatientID'])
                        break
                for code in giICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isGI = True
                        giCases.append(row['PatientID'])
                        break
                for code in hemorrhageICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isIVH = True
                        hemorrhageCases.append(row['PatientID'])
                        break
                for code in asphyxiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isAsphyxia = True
                        asphyxiaCases.append(row['PatientID'])
                        break
                for code in apneaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isApnea = True
                        ApneaCases.append(row['PatientID'])
                        break
                for code in hypoglycemiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isHypoglycemia = True
                        HypoglycemiaCases.append(row['PatientID'])
                        break
                for code in pphnICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPPHN = True
                        PPHNCases.append(row['PatientID'])
                        break
                for code in pneumothoraxICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPneumo = True
                        PneumothoraxCases.append(row['PatientID'])
                        break
                for code in hieICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isHie = True
                        HIECases.append(row['PatientID'])
                        break

                if (isRDS):
                    rdsTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isSepsis):
                    sepsisTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isBPD):
                    bpdTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isNEC):
                    necTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isIVH):
                    ivhTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isApnea):
                    apneaTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isPPHN):
                    pphnTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isHypothermia):
                    hypothermiaTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isROP):
                    ropTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isJaundice):
                    jaundiceTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isCVS):
                    cvsTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isGI):
                    giTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isAsphyxia):
                    asphyxiaTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isHypoglycemia):
                    hypoglycemiaTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isHie):
                    hieTotalCost.append(row['Total_Direct_Variable_Cost'])
                if (isPneumo):
                    pneumoTotalCost.append(row['Total_Direct_Variable_Cost'])

    morbidityDict = {}
    morbidityDict['DRG Code'] = drgList
    morbidityDict['Patient Count'] = len(los)
    morbidityDict['Average LOS'] = round(sum(los) / len(los), 2)
    morbidityDict['Cost per patient in $K'] = round(totalCost / (1000 * len(los)), 2)

    morbidityDict["Hypothermia"] = 0
    morbidityDict["Sepsis"] = 0
    morbidityDict["ROP"] = 0
    morbidityDict["BPD"] = 0
    morbidityDict["NEC"] = 0
    morbidityDict["RDS"] = 0
    morbidityDict["Jaundice"] = 0
    morbidityDict["CVS"] = 0
    morbidityDict["Asphyxia"] = 0
    morbidityDict["Hemorrhage"] = 0
    morbidityDict["GI"] = 0
    morbidityDict["Apnea"] = 0
    morbidityDict["Hypoglycemia"] = 0
    morbidityDict["PPHN"] = 0
    morbidityDict["Pneumothorax"] = 0
    morbidityDict["HIE"] = 0

    if(len(hypothermiaTotalCost) > 0):
        morbidityDict["Hypothermia"] = round(sum(hypothermiaTotalCost) / 1000 / len(hypothermiaTotalCost),2)
    if (len(sepsisTotalCost) > 0):
        morbidityDict["Sepsis"] = round(sum(sepsisTotalCost) / 1000 / len(sepsisTotalCost),2)
    if (len(ropTotalCost) > 0):
        morbidityDict["ROP"] = round(sum(ropTotalCost) / 1000 / len(ropTotalCost),2)
    if (len(bpdTotalCost) > 0):
        morbidityDict["BPD"] = round(sum(bpdTotalCost) / 1000 / len(bpdTotalCost),2)
    if (len(necTotalCost) > 0):
        morbidityDict["NEC"] = round(sum(necTotalCost) / 1000 / len(necTotalCost),2)
    if (len(rdsTotalCost) > 0):
        morbidityDict["RDS"] = round(sum(rdsTotalCost) / 1000 / len(rdsTotalCost),2)
    if (len(jaundiceTotalCost) > 0):
        morbidityDict["Jaundice"] = round(sum(jaundiceTotalCost) / 1000 / len(jaundiceTotalCost),2)
    if (len(cvsTotalCost) > 0):
        morbidityDict["CVS"] = round(sum(cvsTotalCost) / 1000 / len(cvsTotalCost),2)
    if (len(asphyxiaTotalCost) > 0):
        morbidityDict["Asphyxia"] = round(sum(asphyxiaTotalCost) / 1000 / len(asphyxiaTotalCost),2)
    if (len(ivhTotalCost) > 0):
        morbidityDict["Hemorrhage"] = round(sum(ivhTotalCost) / 1000 / len(ivhTotalCost),2)
    if (len(giTotalCost) > 0):
        morbidityDict["GI"] = round(sum(giTotalCost) / 1000 / len(giTotalCost),2)
    if (len(apneaTotalCost) > 0):
        morbidityDict["Apnea"] = round(sum(apneaTotalCost) / 1000 / len(apneaTotalCost),2)
    if (len(hypoglycemiaTotalCost) > 0):
        morbidityDict["Hypoglycemia"] = round(sum(hypoglycemiaTotalCost) / 1000 / len(hypoglycemiaTotalCost),2)
    if (len(pphnTotalCost) > 0):
        morbidityDict["PPHN"] = round(sum(pphnTotalCost) / 1000 / len(pphnTotalCost),2)
    if (len(pneumoTotalCost) > 0):
        morbidityDict["Pneumothorax"] = round(sum(pneumoTotalCost) / 1000 / len(pneumoTotalCost),2)
    if (len(hieTotalCost) > 0):
        morbidityDict["HIE"] = round(sum(hieTotalCost) / 1000 / len(hieTotalCost),2)

    return morbidityDict


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

outputTable1 = DRFCodeDistribution(drgCodeGreaterthan500Lessthan750)
outputTable2 = DRFCodeDistribution(drgCodeGreaterthan750Lessthan1000)
outputTable3 = DRFCodeDistribution(drgCodeLessthan1000Only)
outputTable4 = DRFCodeDistribution(drgCodeLessthan1000)
outputTable5 = DRFCodeDistribution(drgCodeGreaterthan1000Lessthan1250)
outputTable6 = DRFCodeDistribution(drgCodeGreaterthan1250Lessthan1500)
outputTable7 = DRFCodeDistribution(drgCodeLessthan1500Only)
outputTable8 = DRFCodeDistribution(drgCodeLessthan1500)
outputTable9 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2000)
outputTable10 = DRFCodeDistribution(drgCodeGreaterthan2000Lessthan2500)
outputTable11 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500Only)
outputTable12 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500)
outputTable13 = DRFCodeDistribution(drgCodeGreaterthan2500)
outputTable14 = DRFCodeDistribution(drgAll)

outputTable = PrettyTable(["Weight categories (gm)",
    "500-750",
    "750-1000",
    "<1000",
    "Total 500-1000",
    "1000-1250",
    "1250-1500",
    "<1500",
    "Total 500-1500",
    "1500-2000",
    "2000-2500",
    "1500-2500",
    "Total 1500-2500",
    ">2500",
    "All"])

outputTable.add_row(['DRG Code', outputTable1['DRG Code'], outputTable2['DRG Code'],
      outputTable3['DRG Code'], outputTable4['DRG Code'],
      outputTable5['DRG Code'], outputTable6['DRG Code'], outputTable7['DRG Code'],
      outputTable8['DRG Code'], outputTable9['DRG Code'], outputTable10['DRG Code'],
      outputTable11['DRG Code'], outputTable12['DRG Code'], outputTable13['DRG Code'],
      outputTable14['DRG Code']])

outputTable.add_row(['Patient Count', outputTable1['Patient Count'], outputTable2['Patient Count'],
      outputTable3['Patient Count'], outputTable4['Patient Count'],
      outputTable5['Patient Count'], outputTable6['Patient Count'], outputTable7['Patient Count'],
      outputTable8['Patient Count'], outputTable9['Patient Count'], outputTable10['Patient Count'],
      outputTable11['Patient Count'], outputTable12['Patient Count'], outputTable13['Patient Count'],
      outputTable14['Patient Count']])

outputTable.add_row(['Average LOS', outputTable1['Average LOS'], outputTable2['Average LOS'],
      outputTable3['Average LOS'], outputTable4['Average LOS'],
      outputTable5['Average LOS'], outputTable6['Average LOS'], outputTable7['Average LOS'],
      outputTable8['Average LOS'], outputTable9['Average LOS'], outputTable10['Average LOS'],
      outputTable11['Average LOS'], outputTable12['Average LOS'], outputTable13['Average LOS'],
      outputTable14['Average LOS']])

outputTable.add_row(['Cost per patient in $K', outputTable1['Cost per patient in $K'], outputTable2['Cost per patient in $K'],
      outputTable3['Cost per patient in $K'], outputTable4['Cost per patient in $K'],
      outputTable5['Cost per patient in $K'], outputTable6['Cost per patient in $K'], outputTable7['Cost per patient in $K'],
      outputTable8['Cost per patient in $K'], outputTable9['Cost per patient in $K'], outputTable10['Cost per patient in $K'],
      outputTable11['Cost per patient in $K'], outputTable12['Cost per patient in $K'], outputTable13['Cost per patient in $K'],
      outputTable14['Cost per patient in $K']])
outputTable.add_row(['RDS', outputTable1['RDS'], outputTable2['RDS'],
      outputTable3['RDS'], outputTable4['RDS'],
      outputTable5['RDS'], outputTable6['RDS'], outputTable7['RDS'],
      outputTable8['RDS'], outputTable9['RDS'], outputTable10['RDS'],
      outputTable11['RDS'], outputTable12['RDS'], outputTable13['RDS'],
      outputTable14['RDS']])
outputTable.add_row(['Apnea', outputTable1['Apnea'], outputTable2['Apnea'],
      outputTable3['Apnea'], outputTable4['Apnea'],
      outputTable5['Apnea'], outputTable6['Apnea'], outputTable7['Apnea'],
      outputTable8['Apnea'], outputTable9['Apnea'], outputTable10['Apnea'],
      outputTable11['Apnea'], outputTable12['Apnea'], outputTable13['Apnea'],
      outputTable14['Apnea']])
outputTable.add_row(['BPD', outputTable1['BPD'], outputTable2['BPD'],
      outputTable3['BPD'], outputTable4['BPD'],
      outputTable5['BPD'], outputTable6['BPD'], outputTable7['BPD'],
      outputTable8['BPD'], outputTable9['BPD'], outputTable10['BPD'],
      outputTable11['BPD'], outputTable12['BPD'], outputTable13['BPD'],
      outputTable14['BPD']])
outputTable.add_row(['Sepsis', outputTable1['Sepsis'], outputTable2['Sepsis'],
      outputTable3['Sepsis'], outputTable4['Sepsis'],
      outputTable5['Sepsis'], outputTable6['Sepsis'], outputTable7['Sepsis'],
      outputTable8['Sepsis'], outputTable9['Sepsis'], outputTable10['Sepsis'],
      outputTable11['Sepsis'], outputTable12['Sepsis'], outputTable13['Sepsis'],
      outputTable14['Sepsis']])
outputTable.add_row(['Hemorrhage', outputTable1['Hemorrhage'], outputTable2['Hemorrhage'],
      outputTable3['Hemorrhage'], outputTable4['Hemorrhage'],
      outputTable5['Hemorrhage'], outputTable6['Hemorrhage'], outputTable7['Hemorrhage'],
      outputTable8['Hemorrhage'], outputTable9['Hemorrhage'], outputTable10['Hemorrhage'],
      outputTable11['Hemorrhage'], outputTable12['Hemorrhage'], outputTable13['Hemorrhage'],
      outputTable14['Hemorrhage']])

outputTable.add_row(['Pneumothorax', outputTable1['Pneumothorax'], outputTable2['Pneumothorax'],
      outputTable3['Pneumothorax'], outputTable4['Pneumothorax'],
      outputTable5['Pneumothorax'], outputTable6['Pneumothorax'], outputTable7['Pneumothorax'],
      outputTable8['Pneumothorax'], outputTable9['Pneumothorax'], outputTable10['Pneumothorax'],
      outputTable11['Pneumothorax'], outputTable12['Pneumothorax'], outputTable13['Pneumothorax'],
      outputTable14['Pneumothorax']])
outputTable.add_row(['GI', outputTable1['GI'], outputTable2['GI'],
      outputTable3['GI'], outputTable4['GI'],
      outputTable5['GI'], outputTable6['GI'], outputTable7['GI'],
      outputTable8['GI'], outputTable9['GI'], outputTable10['GI'],
      outputTable11['GI'], outputTable12['GI'], outputTable13['GI'],
      outputTable14['GI']])
outputTable.add_row(['Jaundice', outputTable1['Jaundice'], outputTable2['Jaundice'],
      outputTable3['Jaundice'], outputTable4['Jaundice'],
      outputTable5['Jaundice'], outputTable6['Jaundice'], outputTable7['Jaundice'],
      outputTable8['Jaundice'], outputTable9['Jaundice'], outputTable10['Jaundice'],
      outputTable11['Jaundice'], outputTable12['Jaundice'], outputTable13['Jaundice'],
      outputTable14['Jaundice']])
outputTable.add_row(['NEC', outputTable1['NEC'], outputTable2['NEC'],
      outputTable3['NEC'], outputTable4['NEC'],
      outputTable5['NEC'], outputTable6['NEC'], outputTable7['NEC'],
      outputTable8['NEC'], outputTable9['NEC'], outputTable10['NEC'],
      outputTable11['NEC'], outputTable12['NEC'], outputTable13['NEC'],
      outputTable14['NEC']])
outputTable.add_row(['ROP', outputTable1['ROP'], outputTable2['ROP'],
      outputTable3['ROP'], outputTable4['ROP'],
      outputTable5['ROP'], outputTable6['ROP'], outputTable7['ROP'],
      outputTable8['ROP'], outputTable9['ROP'], outputTable10['ROP'],
      outputTable11['ROP'], outputTable12['ROP'], outputTable13['ROP'],
      outputTable14['ROP']])
outputTable.add_row(['PPHN', outputTable1['PPHN'], outputTable2['PPHN'],
      outputTable3['PPHN'], outputTable4['PPHN'],
      outputTable5['PPHN'], outputTable6['PPHN'], outputTable7['PPHN'],
      outputTable8['PPHN'], outputTable9['PPHN'], outputTable10['PPHN'],
      outputTable11['PPHN'], outputTable12['PPHN'], outputTable13['PPHN'],
      outputTable14['PPHN']])
outputTable.add_row(['Asphyxia', outputTable1['Asphyxia'], outputTable2['Asphyxia'],
      outputTable3['Asphyxia'], outputTable4['Asphyxia'],
      outputTable5['Asphyxia'], outputTable6['Asphyxia'], outputTable7['Asphyxia'],
      outputTable8['Asphyxia'], outputTable9['Asphyxia'], outputTable10['Asphyxia'],
      outputTable11['Asphyxia'], outputTable12['Asphyxia'], outputTable13['Asphyxia'],
      outputTable14['Asphyxia']])
outputTable.add_row(['Hypoglycemia', outputTable1['Hypoglycemia'], outputTable2['Hypoglycemia'],
      outputTable3['Hypoglycemia'], outputTable4['Hypoglycemia'],
      outputTable5['Hypoglycemia'], outputTable6['Hypoglycemia'], outputTable7['Hypoglycemia'],
      outputTable8['Hypoglycemia'], outputTable9['Hypoglycemia'], outputTable10['Hypoglycemia'],
      outputTable11['Hypoglycemia'], outputTable12['Hypoglycemia'], outputTable13['Hypoglycemia'],
      outputTable14['Hypoglycemia']])
outputTable.add_row(['Hypothermia', outputTable1['Hypothermia'], outputTable2['Hypothermia'],
      outputTable3['Hypothermia'], outputTable4['Hypothermia'],
      outputTable5['Hypothermia'], outputTable6['Hypothermia'], outputTable7['Hypothermia'],
      outputTable8['Hypothermia'], outputTable9['Hypothermia'], outputTable10['Hypothermia'],
      outputTable11['Hypothermia'], outputTable12['Hypothermia'], outputTable13['Hypothermia'],
      outputTable14['Hypothermia']])
outputTable.add_row(['HIE', outputTable1['HIE'], outputTable2['HIE'],
      outputTable3['HIE'], outputTable4['HIE'],
      outputTable5['HIE'], outputTable6['HIE'], outputTable7['HIE'],
      outputTable8['HIE'], outputTable9['HIE'], outputTable10['HIE'],
      outputTable11['HIE'], outputTable12['HIE'], outputTable13['HIE'],
      outputTable14['HIE']])

print(outputTable)
