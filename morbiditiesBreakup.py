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

    sepsisPneumo = 0
    sepsisNoPneumo = 0

    bpdPneumo = 0
    bpdNoPneumo = 0

    necPneumo = 0
    necNoPneumo = 0

    ivhPneumo = 0
    ivhNoPneumo = 0

    onlyPneumo = 0
    onlyNoPneumo = 0

    apneaPneumo = 0
    apneaNoPneumo = 0

    pphnPneumo = 0
    pphnNoPneumo = 0

    hypothermiaPneumo = 0
    hypothermiaNoPneumo = 0

    ropPneumo = 0
    ropNoPneumo = 0

    jaundicePneumo = 0
    jaundiceNoPneumo = 0

    cvsPneumo = 0
    cvsNoPneumo = 0

    giPneumo = 0
    giNoPneumo = 0

    asphyxiaPneumo = 0
    asphyxiaNoPneumo = 0

    hypoglycemiaPneumo = 0
    hypoglycemiaNoPneumo = 0

    hiePneumo = 0
    hieNoPneumo = 0
    otherPneumo = 0
    otherNoPneumo = 0

    los = []
    surfactantList = ['HC SURFACTANT ADMINISTRATION',
                      'SURFACTANT ADMIN THRU TUBE', 'PORACTANT ALFA 120 MG/1.5 ML SUSPENSION',
                      'PORACTANT ALFA 80 MG/ML SUSP', 'PORACTANT ALFA 240 MG/3 ML SUSPENSION']

    for code in drgList:
        patientRows = patientMaster[patientMaster['APRDRG Code'] == code]

        for index, row in patientRows.iterrows():

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

                        if (encounter['Activity Desc'] in surfactantList):
                            isSurfactant = True

                if isSurfactant and isRDS:
                    if (isPneumo):
                        if (isSepsis):
                            sepsisPneumo = sepsisPneumo + 1
                        if (isBPD):
                            bpdPneumo = bpdPneumo + 1
                        if (isNEC):
                            necPneumo = necPneumo + 1
                        if (isIVH):
                            ivhPneumo = ivhPneumo + 1
                        if (not isPatientICD):
                            onlyPneumo = onlyPneumo + 1
                        if (isApnea):
                            apneaPneumo = apneaPneumo + 1
                        if (isPPHN):
                            pphnPneumo = pphnPneumo + 1
                        if (isHypothermia):
                            hypothermiaPneumo = hypothermiaPneumo + 1
                        if (isrop):
                            ropPneumo = ropPneumo + 1
                        if (isJaundice):
                            jaundicePneumo = jaundicePneumo + 1
                        if (isCVS):
                            cvsPneumo = cvsPneumo + 1
                        if (isGI):
                            giPneumo = giPneumo + 1
                        if (isAsphyxia):
                            asphyxiaPneumo = asphyxiaPneumo + 1
                        if (isHypoglycemia):
                            hypoglycemiaPneumo = hypoglycemiaPneumo + 1
                        if (isHie):
                            hiePneumo = hiePneumo + 1
                        if (isOther):
                            otherPneumo = otherPneumo + 1

                    else:
                        if (isSepsis):
                            sepsisNoPneumo = sepsisNoPneumo + 1
                        if (isBPD):
                            bpdNoPneumo = bpdNoPneumo + 1
                        if (isNEC):
                            necNoPneumo = necNoPneumo + 1
                        if (isIVH):
                            ivhNoPneumo = ivhNoPneumo + 1
                        if (not isPatientICD):
                            onlyNoPneumo = onlyNoPneumo + 1
                        if (isApnea):
                            apneaNoPneumo = apneaNoPneumo + 1
                        if (isPPHN):
                            pphnNoPneumo = pphnNoPneumo + 1
                        if (isHypothermia):
                            hypothermiaNoPneumo = hypothermiaNoPneumo + 1
                        if (isrop):
                            ropNoPneumo = ropNoPneumo + 1
                        if (isJaundice):
                            jaundiceNoPneumo = jaundiceNoPneumo + 1
                        if (isCVS):
                            cvsNoPneumo = cvsNoPneumo + 1
                        if (isGI):
                            giNoPneumo = giNoPneumo + 1
                        if (isAsphyxia):
                            asphyxiaNoPneumo = asphyxiaNoPneumo + 1
                        if (isHypoglycemia):
                            hypoglycemiaNoPneumo = hypoglycemiaNoPneumo + 1
                        if (isHie):
                            hieNoPneumo = hieNoPneumo + 1
                        if (isOther):
                            otherNoPneumo = otherNoPneumo + 1

    morbiditiesPneumo = {}
    morbiditiesNoPneumo = {}
    morbiditiesPneumo['Sepsis'] = sepsisPneumo
    morbiditiesPneumo['BPD'] = bpdPneumo
    morbiditiesPneumo['NEC'] = necPneumo
    morbiditiesPneumo['Hemorrhage'] = ivhPneumo
    morbiditiesPneumo[('Only Pneumo'
                       'thorax')] = onlyPneumo
    morbiditiesPneumo['Apnea'] = apneaPneumo
    morbiditiesPneumo['PPHN'] = pphnPneumo
    morbiditiesPneumo['Hypothermia'] = hypothermiaPneumo
    morbiditiesPneumo['ROP'] = ropPneumo
    morbiditiesPneumo['Jaundice'] = jaundicePneumo
    morbiditiesPneumo['CVS'] = cvsPneumo
    morbiditiesPneumo['GI'] = giPneumo
    morbiditiesPneumo['Asphyxia'] = asphyxiaPneumo
    morbiditiesPneumo['Hypoglycemia'] = hypoglycemiaPneumo
    morbiditiesPneumo['HIE'] = hiePneumo
    morbiditiesPneumo['Others'] = otherPneumo

    morbiditiesNoPneumo['Sepsis'] = sepsisNoPneumo
    morbiditiesNoPneumo['BPD'] = bpdNoPneumo
    morbiditiesNoPneumo['NEC'] = necNoPneumo
    morbiditiesNoPneumo['Hemorrhage'] = ivhNoPneumo
    morbiditiesNoPneumo['Only RDS'] = onlyNoPneumo
    morbiditiesNoPneumo['Apnea'] = apneaNoPneumo
    morbiditiesNoPneumo['PPHN'] = pphnNoPneumo
    morbiditiesNoPneumo['Hypothermia'] = hypothermiaNoPneumo
    morbiditiesNoPneumo['ROP'] = ropNoPneumo
    morbiditiesNoPneumo['Jaundice'] = jaundiceNoPneumo
    morbiditiesNoPneumo['CVS'] = cvsNoPneumo
    morbiditiesNoPneumo['GI'] = giNoPneumo
    morbiditiesNoPneumo['Asphyxia'] = asphyxiaNoPneumo
    morbiditiesNoPneumo['Hypoglycemia'] = hypoglycemiaNoPneumo
    morbiditiesNoPneumo['HIE'] = hieNoPneumo
    morbiditiesNoPneumo['Others'] = otherNoPneumo

    return morbiditiesPneumo, morbiditiesNoPneumo


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

morbiditiesPneumo1, morbiditiesNoPneumo1 = DRFCodeDistribution(drgCodeGreaterthan500Lessthan750)
morbiditiesPneumo2, morbiditiesNoPneumo2 = DRFCodeDistribution(drgCodeGreaterthan750Lessthan1000)
morbiditiesPneumo3, morbiditiesNoPneumo3 = DRFCodeDistribution(drgCodeLessthan1000Only)
morbiditiesPneumo4, morbiditiesNoPneumo4 = DRFCodeDistribution(drgCodeLessthan1000)
morbiditiesPneumo5, morbiditiesNoPneumo5 = DRFCodeDistribution(drgCodeGreaterthan1000Lessthan1250)
morbiditiesPneumo6, morbiditiesNoPneumo6 = DRFCodeDistribution(drgCodeGreaterthan1250Lessthan1500)
morbiditiesPneumo7, morbiditiesNoPneumo7 = DRFCodeDistribution(drgCodeLessthan1500Only)
morbiditiesPneumo8, morbiditiesNoPneumo8 = DRFCodeDistribution(drgCodeLessthan1500)
morbiditiesPneumo9, morbiditiesNoPneumo9 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2000)
morbiditiesPneumo10, morbiditiesNoPneumo10 = DRFCodeDistribution(drgCodeGreaterthan2000Lessthan2500)
morbiditiesPneumo11, morbiditiesNoPneumo11 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500Only)
morbiditiesPneumo12, morbiditiesNoPneumo12 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500)
morbiditiesPneumo13, morbiditiesNoPneumo13 = DRFCodeDistribution(drgCodeGreaterthan2500)
morbiditiesPneumo14, morbiditiesNoPneumo14 = DRFCodeDistribution(drgAll)

morbiditiesPneumoTable = PrettyTable(["Morbidities",
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

morbiditiesPneumoTable.add_row(['Sepsis', morbiditiesPneumo1['Sepsis'], morbiditiesPneumo2['Sepsis'],
      morbiditiesPneumo3['Sepsis'], morbiditiesPneumo4['Sepsis'],
      morbiditiesPneumo5['Sepsis'], morbiditiesPneumo6['Sepsis'], morbiditiesPneumo7['Sepsis'],
      morbiditiesPneumo8['Sepsis'], morbiditiesPneumo9['Sepsis'], morbiditiesPneumo10['Sepsis'],
      morbiditiesPneumo11['Sepsis'], morbiditiesPneumo12['Sepsis'], morbiditiesPneumo13['Sepsis'],
      morbiditiesPneumo14['Sepsis']])
morbiditiesPneumoTable.add_row(['BPD', morbiditiesPneumo1['BPD'], morbiditiesPneumo2['BPD'],
      morbiditiesPneumo3['BPD'], morbiditiesPneumo4['BPD'],
      morbiditiesPneumo5['BPD'], morbiditiesPneumo6['BPD'], morbiditiesPneumo7['BPD'],
      morbiditiesPneumo8['BPD'], morbiditiesPneumo9['BPD'], morbiditiesPneumo10['BPD'],
      morbiditiesPneumo11['BPD'], morbiditiesPneumo12['BPD'], morbiditiesPneumo13['BPD'],
      morbiditiesPneumo14['BPD']])
morbiditiesPneumoTable.add_row(['NEC', morbiditiesPneumo1['NEC'], morbiditiesPneumo2['NEC'],
      morbiditiesPneumo3['NEC'], morbiditiesPneumo4['NEC'],
      morbiditiesPneumo5['NEC'], morbiditiesPneumo6['NEC'], morbiditiesPneumo7['NEC'],
      morbiditiesPneumo8['NEC'], morbiditiesPneumo9['NEC'], morbiditiesPneumo10['NEC'],
      morbiditiesPneumo11['NEC'], morbiditiesPneumo12['NEC'], morbiditiesPneumo13['NEC'],
      morbiditiesPneumo14['NEC']])
morbiditiesPneumoTable.add_row(['Hemorrhage', morbiditiesPneumo1['Hemorrhage'], morbiditiesPneumo2['Hemorrhage'],
      morbiditiesPneumo3['Hemorrhage'], morbiditiesPneumo4['Hemorrhage'],
      morbiditiesPneumo5['Hemorrhage'], morbiditiesPneumo6['Hemorrhage'], morbiditiesPneumo7['Hemorrhage'],
      morbiditiesPneumo8['Hemorrhage'], morbiditiesPneumo9['Hemorrhage'], morbiditiesPneumo10['Hemorrhage'],
      morbiditiesPneumo11['Hemorrhage'], morbiditiesPneumo12['Hemorrhage'], morbiditiesPneumo13['Hemorrhage'],
      morbiditiesPneumo14['Hemorrhage']])
morbiditiesPneumoTable.add_row(['Only Pneumothorax', morbiditiesPneumo1['Only Pneumothorax'], morbiditiesPneumo2['Only Pneumothorax'],
      morbiditiesPneumo3['Only Pneumothorax'], morbiditiesPneumo4['Only Pneumothorax'],
      morbiditiesPneumo5['Only Pneumothorax'], morbiditiesPneumo6['Only Pneumothorax'], morbiditiesPneumo7['Only Pneumothorax'],
      morbiditiesPneumo8['Only Pneumothorax'], morbiditiesPneumo9['Only Pneumothorax'], morbiditiesPneumo10['Only Pneumothorax'],
      morbiditiesPneumo11['Only Pneumothorax'], morbiditiesPneumo12['Only Pneumothorax'], morbiditiesPneumo13['Only Pneumothorax'],
      morbiditiesPneumo14['Only Pneumothorax']])
morbiditiesPneumoTable.add_row(['Apnea', morbiditiesPneumo1['Apnea'], morbiditiesPneumo2['Apnea'],
      morbiditiesPneumo3['Apnea'], morbiditiesPneumo4['Apnea'],
      morbiditiesPneumo5['Apnea'], morbiditiesPneumo6['Apnea'], morbiditiesPneumo7['Apnea'],
      morbiditiesPneumo8['Apnea'], morbiditiesPneumo9['Apnea'], morbiditiesPneumo10['Apnea'],
      morbiditiesPneumo11['Apnea'], morbiditiesPneumo12['Apnea'], morbiditiesPneumo13['Apnea'],
      morbiditiesPneumo14['Apnea']])
morbiditiesPneumoTable.add_row(['PPHN', morbiditiesPneumo1['PPHN'], morbiditiesPneumo2['PPHN'],
      morbiditiesPneumo3['PPHN'], morbiditiesPneumo4['PPHN'],
      morbiditiesPneumo5['PPHN'], morbiditiesPneumo6['PPHN'], morbiditiesPneumo7['PPHN'],
      morbiditiesPneumo8['PPHN'], morbiditiesPneumo9['PPHN'], morbiditiesPneumo10['PPHN'],
      morbiditiesPneumo11['PPHN'], morbiditiesPneumo12['PPHN'], morbiditiesPneumo13['PPHN'],
      morbiditiesPneumo14['PPHN']])
morbiditiesPneumoTable.add_row(['Hypothermia', morbiditiesPneumo1['Hypothermia'], morbiditiesPneumo2['Hypothermia'],
      morbiditiesPneumo3['Hypothermia'], morbiditiesPneumo4['Hypothermia'],
      morbiditiesPneumo5['Hypothermia'], morbiditiesPneumo6['Hypothermia'], morbiditiesPneumo7['Hypothermia'],
      morbiditiesPneumo8['Hypothermia'], morbiditiesPneumo9['Hypothermia'], morbiditiesPneumo10['Hypothermia'],
      morbiditiesPneumo11['Hypothermia'], morbiditiesPneumo12['Hypothermia'], morbiditiesPneumo13['Hypothermia'],
      morbiditiesPneumo14['Hypothermia']])
morbiditiesPneumoTable.add_row(['ROP', morbiditiesPneumo1['ROP'], morbiditiesPneumo2['ROP'],
      morbiditiesPneumo3['ROP'], morbiditiesPneumo4['ROP'],
      morbiditiesPneumo5['ROP'], morbiditiesPneumo6['ROP'], morbiditiesPneumo7['ROP'],
      morbiditiesPneumo8['ROP'], morbiditiesPneumo9['ROP'], morbiditiesPneumo10['ROP'],
      morbiditiesPneumo11['ROP'], morbiditiesPneumo12['ROP'], morbiditiesPneumo13['ROP'],
      morbiditiesPneumo14['ROP']])
morbiditiesPneumoTable.add_row(['Jaundice', morbiditiesPneumo1['Jaundice'], morbiditiesPneumo2['Jaundice'],
      morbiditiesPneumo3['Jaundice'], morbiditiesPneumo4['Jaundice'],
      morbiditiesPneumo5['Jaundice'], morbiditiesPneumo6['Jaundice'], morbiditiesPneumo7['Jaundice'],
      morbiditiesPneumo8['Jaundice'], morbiditiesPneumo9['Jaundice'], morbiditiesPneumo10['Jaundice'],
      morbiditiesPneumo11['Jaundice'], morbiditiesPneumo12['Jaundice'], morbiditiesPneumo13['Jaundice'],
      morbiditiesPneumo14['Jaundice']])
morbiditiesPneumoTable.add_row(['GI', morbiditiesPneumo1['GI'], morbiditiesPneumo2['GI'],
      morbiditiesPneumo3['GI'], morbiditiesPneumo4['GI'],
      morbiditiesPneumo5['GI'], morbiditiesPneumo6['GI'], morbiditiesPneumo7['GI'],
      morbiditiesPneumo8['GI'], morbiditiesPneumo9['GI'], morbiditiesPneumo10['GI'],
      morbiditiesPneumo11['GI'], morbiditiesPneumo12['GI'], morbiditiesPneumo13['GI'],
      morbiditiesPneumo14['GI']])
morbiditiesPneumoTable.add_row(['Asphyxia', morbiditiesPneumo1['Asphyxia'], morbiditiesPneumo2['Asphyxia'],
      morbiditiesPneumo3['Asphyxia'], morbiditiesPneumo4['Asphyxia'],
      morbiditiesPneumo5['Asphyxia'], morbiditiesPneumo6['Asphyxia'], morbiditiesPneumo7['Asphyxia'],
      morbiditiesPneumo8['Asphyxia'], morbiditiesPneumo9['Asphyxia'], morbiditiesPneumo10['Asphyxia'],
      morbiditiesPneumo11['Asphyxia'], morbiditiesPneumo12['Asphyxia'], morbiditiesPneumo13['Asphyxia'],
      morbiditiesPneumo14['Asphyxia']])
morbiditiesPneumoTable.add_row(['Hypoglycemia', morbiditiesPneumo1['Hypoglycemia'], morbiditiesPneumo2['Hypoglycemia'],
      morbiditiesPneumo3['Hypoglycemia'], morbiditiesPneumo4['Hypoglycemia'],
      morbiditiesPneumo5['Hypoglycemia'], morbiditiesPneumo6['Hypoglycemia'], morbiditiesPneumo7['Hypoglycemia'],
      morbiditiesPneumo8['Hypoglycemia'], morbiditiesPneumo9['Hypoglycemia'], morbiditiesPneumo10['Hypoglycemia'],
      morbiditiesPneumo11['Hypoglycemia'], morbiditiesPneumo12['Hypoglycemia'], morbiditiesPneumo13['Hypoglycemia'],
      morbiditiesPneumo14['Hypoglycemia']])
morbiditiesPneumoTable.add_row(['HIE', morbiditiesPneumo1['HIE'], morbiditiesPneumo2['HIE'],
      morbiditiesPneumo3['HIE'], morbiditiesPneumo4['HIE'],
      morbiditiesPneumo5['HIE'], morbiditiesPneumo6['HIE'], morbiditiesPneumo7['HIE'],
      morbiditiesPneumo8['HIE'], morbiditiesPneumo9['HIE'], morbiditiesPneumo10['HIE'],
      morbiditiesPneumo11['HIE'], morbiditiesPneumo12['HIE'], morbiditiesPneumo13['HIE'],
      morbiditiesPneumo14['HIE']])
morbiditiesPneumoTable.add_row(['Others', morbiditiesPneumo1['Others'], morbiditiesPneumo2['Others'],
      morbiditiesPneumo3['Others'], morbiditiesPneumo4['Others'],
      morbiditiesPneumo5['Others'], morbiditiesPneumo6['Others'], morbiditiesPneumo7['Others'],
      morbiditiesPneumo8['Others'], morbiditiesPneumo9['Others'], morbiditiesPneumo10['Others'],
      morbiditiesPneumo11['Others'], morbiditiesPneumo12['Others'], morbiditiesPneumo13['Others'],
      morbiditiesPneumo14['Others']])

print(morbiditiesPneumoTable)

morbiditiesNoPneumoTable = PrettyTable(["Morbidities",
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

morbiditiesNoPneumoTable.add_row(['Sepsis', morbiditiesNoPneumo1['Sepsis'], morbiditiesNoPneumo2['Sepsis'],
      morbiditiesNoPneumo3['Sepsis'], morbiditiesNoPneumo4['Sepsis'],
      morbiditiesNoPneumo5['Sepsis'], morbiditiesNoPneumo6['Sepsis'], morbiditiesNoPneumo7['Sepsis'],
      morbiditiesNoPneumo8['Sepsis'], morbiditiesNoPneumo9['Sepsis'], morbiditiesNoPneumo10['Sepsis'],
      morbiditiesNoPneumo11['Sepsis'], morbiditiesNoPneumo12['Sepsis'], morbiditiesNoPneumo13['Sepsis'],
      morbiditiesNoPneumo14['Sepsis']])
morbiditiesNoPneumoTable.add_row(['BPD', morbiditiesNoPneumo1['BPD'], morbiditiesNoPneumo2['BPD'],
      morbiditiesNoPneumo3['BPD'], morbiditiesNoPneumo4['BPD'],
      morbiditiesNoPneumo5['BPD'], morbiditiesNoPneumo6['BPD'], morbiditiesNoPneumo7['BPD'],
      morbiditiesNoPneumo8['BPD'], morbiditiesNoPneumo9['BPD'], morbiditiesNoPneumo10['BPD'],
      morbiditiesNoPneumo11['BPD'], morbiditiesNoPneumo12['BPD'], morbiditiesNoPneumo13['BPD'],
      morbiditiesNoPneumo14['BPD']])
morbiditiesNoPneumoTable.add_row(['NEC', morbiditiesNoPneumo1['NEC'], morbiditiesNoPneumo2['NEC'],
      morbiditiesNoPneumo3['NEC'], morbiditiesNoPneumo4['NEC'],
      morbiditiesNoPneumo5['NEC'], morbiditiesNoPneumo6['NEC'], morbiditiesNoPneumo7['NEC'],
      morbiditiesNoPneumo8['NEC'], morbiditiesNoPneumo9['NEC'], morbiditiesNoPneumo10['NEC'],
      morbiditiesNoPneumo11['NEC'], morbiditiesNoPneumo12['NEC'], morbiditiesNoPneumo13['NEC'],
      morbiditiesNoPneumo14['NEC']])
morbiditiesNoPneumoTable.add_row(['Hemorrhage', morbiditiesNoPneumo1['Hemorrhage'], morbiditiesNoPneumo2['Hemorrhage'],
      morbiditiesNoPneumo3['Hemorrhage'], morbiditiesNoPneumo4['Hemorrhage'],
      morbiditiesNoPneumo5['Hemorrhage'], morbiditiesNoPneumo6['Hemorrhage'], morbiditiesNoPneumo7['Hemorrhage'],
      morbiditiesNoPneumo8['Hemorrhage'], morbiditiesNoPneumo9['Hemorrhage'], morbiditiesNoPneumo10['Hemorrhage'],
      morbiditiesNoPneumo11['Hemorrhage'], morbiditiesNoPneumo12['Hemorrhage'], morbiditiesNoPneumo13['Hemorrhage'],
      morbiditiesNoPneumo14['Hemorrhage']])
morbiditiesNoPneumoTable.add_row(['Only RDS', morbiditiesNoPneumo1['Only RDS'], morbiditiesNoPneumo2['Only RDS'],
      morbiditiesNoPneumo3['Only RDS'], morbiditiesNoPneumo4['Only RDS'],
      morbiditiesNoPneumo5['Only RDS'], morbiditiesNoPneumo6['Only RDS'], morbiditiesNoPneumo7['Only RDS'],
      morbiditiesNoPneumo8['Only RDS'], morbiditiesNoPneumo9['Only RDS'], morbiditiesNoPneumo10['Only RDS'],
      morbiditiesNoPneumo11['Only RDS'], morbiditiesNoPneumo12['Only RDS'], morbiditiesNoPneumo13['Only RDS'],
      morbiditiesNoPneumo14['Only RDS']])
morbiditiesNoPneumoTable.add_row(['Apnea', morbiditiesNoPneumo1['Apnea'], morbiditiesNoPneumo2['Apnea'],
      morbiditiesNoPneumo3['Apnea'], morbiditiesNoPneumo4['Apnea'],
      morbiditiesNoPneumo5['Apnea'], morbiditiesNoPneumo6['Apnea'], morbiditiesNoPneumo7['Apnea'],
      morbiditiesNoPneumo8['Apnea'], morbiditiesNoPneumo9['Apnea'], morbiditiesNoPneumo10['Apnea'],
      morbiditiesNoPneumo11['Apnea'], morbiditiesNoPneumo12['Apnea'], morbiditiesNoPneumo13['Apnea'],
      morbiditiesNoPneumo14['Apnea']])
morbiditiesNoPneumoTable.add_row(['PPHN', morbiditiesNoPneumo1['PPHN'], morbiditiesNoPneumo2['PPHN'],
      morbiditiesNoPneumo3['PPHN'], morbiditiesNoPneumo4['PPHN'],
      morbiditiesNoPneumo5['PPHN'], morbiditiesNoPneumo6['PPHN'], morbiditiesNoPneumo7['PPHN'],
      morbiditiesNoPneumo8['PPHN'], morbiditiesNoPneumo9['PPHN'], morbiditiesNoPneumo10['PPHN'],
      morbiditiesNoPneumo11['PPHN'], morbiditiesNoPneumo12['PPHN'], morbiditiesNoPneumo13['PPHN'],
      morbiditiesNoPneumo14['PPHN']])
morbiditiesNoPneumoTable.add_row(['Hypothermia', morbiditiesNoPneumo1['Hypothermia'], morbiditiesNoPneumo2['Hypothermia'],
      morbiditiesNoPneumo3['Hypothermia'], morbiditiesNoPneumo4['Hypothermia'],
      morbiditiesNoPneumo5['Hypothermia'], morbiditiesNoPneumo6['Hypothermia'], morbiditiesNoPneumo7['Hypothermia'],
      morbiditiesNoPneumo8['Hypothermia'], morbiditiesNoPneumo9['Hypothermia'], morbiditiesNoPneumo10['Hypothermia'],
      morbiditiesNoPneumo11['Hypothermia'], morbiditiesNoPneumo12['Hypothermia'], morbiditiesNoPneumo13['Hypothermia'],
      morbiditiesNoPneumo14['Hypothermia']])
morbiditiesNoPneumoTable.add_row(['ROP', morbiditiesNoPneumo1['ROP'], morbiditiesNoPneumo2['ROP'],
      morbiditiesNoPneumo3['ROP'], morbiditiesNoPneumo4['ROP'],
      morbiditiesNoPneumo5['ROP'], morbiditiesNoPneumo6['ROP'], morbiditiesNoPneumo7['ROP'],
      morbiditiesNoPneumo8['ROP'], morbiditiesNoPneumo9['ROP'], morbiditiesNoPneumo10['ROP'],
      morbiditiesNoPneumo11['ROP'], morbiditiesNoPneumo12['ROP'], morbiditiesNoPneumo13['ROP'],
      morbiditiesNoPneumo14['ROP']])
morbiditiesNoPneumoTable.add_row(['Jaundice', morbiditiesNoPneumo1['Jaundice'], morbiditiesNoPneumo2['Jaundice'],
      morbiditiesNoPneumo3['Jaundice'], morbiditiesNoPneumo4['Jaundice'],
      morbiditiesNoPneumo5['Jaundice'], morbiditiesNoPneumo6['Jaundice'], morbiditiesNoPneumo7['Jaundice'],
      morbiditiesNoPneumo8['Jaundice'], morbiditiesNoPneumo9['Jaundice'], morbiditiesNoPneumo10['Jaundice'],
      morbiditiesNoPneumo11['Jaundice'], morbiditiesNoPneumo12['Jaundice'], morbiditiesNoPneumo13['Jaundice'],
      morbiditiesNoPneumo14['Jaundice']])
morbiditiesNoPneumoTable.add_row(['GI', morbiditiesNoPneumo1['GI'], morbiditiesNoPneumo2['GI'],
      morbiditiesNoPneumo3['GI'], morbiditiesNoPneumo4['GI'],
      morbiditiesNoPneumo5['GI'], morbiditiesNoPneumo6['GI'], morbiditiesNoPneumo7['GI'],
      morbiditiesNoPneumo8['GI'], morbiditiesNoPneumo9['GI'], morbiditiesNoPneumo10['GI'],
      morbiditiesNoPneumo11['GI'], morbiditiesNoPneumo12['GI'], morbiditiesNoPneumo13['GI'],
      morbiditiesNoPneumo14['GI']])
morbiditiesNoPneumoTable.add_row(['Asphyxia', morbiditiesNoPneumo1['Asphyxia'], morbiditiesNoPneumo2['Asphyxia'],
      morbiditiesNoPneumo3['Asphyxia'], morbiditiesNoPneumo4['Asphyxia'],
      morbiditiesNoPneumo5['Asphyxia'], morbiditiesNoPneumo6['Asphyxia'], morbiditiesNoPneumo7['Asphyxia'],
      morbiditiesNoPneumo8['Asphyxia'], morbiditiesNoPneumo9['Asphyxia'], morbiditiesNoPneumo10['Asphyxia'],
      morbiditiesNoPneumo11['Asphyxia'], morbiditiesNoPneumo12['Asphyxia'], morbiditiesNoPneumo13['Asphyxia'],
      morbiditiesNoPneumo14['Asphyxia']])
morbiditiesNoPneumoTable.add_row(['Hypoglycemia', morbiditiesNoPneumo1['Hypoglycemia'], morbiditiesNoPneumo2['Hypoglycemia'],
      morbiditiesNoPneumo3['Hypoglycemia'], morbiditiesNoPneumo4['Hypoglycemia'],
      morbiditiesNoPneumo5['Hypoglycemia'], morbiditiesNoPneumo6['Hypoglycemia'], morbiditiesNoPneumo7['Hypoglycemia'],
      morbiditiesNoPneumo8['Hypoglycemia'], morbiditiesNoPneumo9['Hypoglycemia'], morbiditiesNoPneumo10['Hypoglycemia'],
      morbiditiesNoPneumo11['Hypoglycemia'], morbiditiesNoPneumo12['Hypoglycemia'], morbiditiesNoPneumo13['Hypoglycemia'],
      morbiditiesNoPneumo14['Hypoglycemia']])
morbiditiesNoPneumoTable.add_row(['HIE', morbiditiesNoPneumo1['HIE'], morbiditiesNoPneumo2['HIE'],
      morbiditiesNoPneumo3['HIE'], morbiditiesNoPneumo4['HIE'],
      morbiditiesNoPneumo5['HIE'], morbiditiesNoPneumo6['HIE'], morbiditiesNoPneumo7['HIE'],
      morbiditiesNoPneumo8['HIE'], morbiditiesNoPneumo9['HIE'], morbiditiesNoPneumo10['HIE'],
      morbiditiesNoPneumo11['HIE'], morbiditiesNoPneumo12['HIE'], morbiditiesNoPneumo13['HIE'],
      morbiditiesNoPneumo14['HIE']])
morbiditiesNoPneumoTable.add_row(['Others', morbiditiesNoPneumo1['Others'], morbiditiesNoPneumo2['Others'],
      morbiditiesNoPneumo3['Others'], morbiditiesNoPneumo4['Others'],
      morbiditiesNoPneumo5['Others'], morbiditiesNoPneumo6['Others'], morbiditiesNoPneumo7['Others'],
      morbiditiesNoPneumo8['Others'], morbiditiesNoPneumo9['Others'], morbiditiesNoPneumo10['Others'],
      morbiditiesNoPneumo11['Others'], morbiditiesNoPneumo12['Others'], morbiditiesNoPneumo13['Others'],
      morbiditiesNoPneumo14['Others']])

print(morbiditiesNoPneumoTable)
