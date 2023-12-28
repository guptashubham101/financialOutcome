from prettytable import PrettyTable
import pandas as pd
import operator
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
    normalCases = []
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
    los = []

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
            if(isCongenital):
                continue
            mrn = row['Hashed MRN']
            encounterRows = encounterofPatients[encounterofPatients['Hashed MRN'] == mrn]
            if (len(encounterRows) > 0 and row['Total_Direct_Variable_Cost'] > 0 and row['APRDRG Code'] != 'NO DATA'):
                los.append(row['LOS'])

                # dictAll, dictAllSub, categoryMapping, dictAllSubL2, categoryMappingL2, dictAllParentCount, dictAllSubCount, dictAllL2Count, dictAllParentLOS, dictAllSubLOS, dictAllL2LOS,allUhids = createMappingforICD(row['PatientID'], allUhids, encounterRows, dictAll, dictAllSub, categoryMapping, dictAllSubL2, categoryMappingL2, dictAllParentCount, dictAllSubCount, dictAllL2Count, dictAllParentLOS, dictAllSubLOS, dictAllL2LOS, row['LOS'])
                totalCost = totalCost + sum(encounterRows['Total Direct Variable Cost'])

                for code in hypothermiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        hypothermiaCases.append(row['PatientID'])
                        break
                for code in sepsisICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        sepsisCases.append(row['PatientID'])
                        break
                for code in necICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        necCases.append(row['PatientID'])
                        break
                for code in ropICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        ropCases.append(row['PatientID'])
                        break
                for code in bpdICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        bpdCases.append(row['PatientID'])
                        break
                for code in rdsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        rdsCases.append(row['PatientID'])
                        break
                for code in jaundiceICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        jaundiceCases.append(row['PatientID'])
                        break
                for code in cvsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        cvsCases.append(row['PatientID'])
                        break
                for code in giICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        giCases.append(row['PatientID'])
                        break
                for code in hemorrhageICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        hemorrhageCases.append(row['PatientID'])
                        break
                for code in asphyxiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        asphyxiaCases.append(row['PatientID'])
                        break
                for code in apneaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        ApneaCases.append(row['PatientID'])
                        break
                for code in hypoglycemiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        HypoglycemiaCases.append(row['PatientID'])
                        break
                for code in pphnICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        PPHNCases.append(row['PatientID'])
                        break
                for code in pneumothoraxICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        PneumothoraxCases.append(row['PatientID'])
                        break
                for code in pneumothoraxICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        PneumothoraxCases.append(row['PatientID'])
                        break
                for code in hieICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        HIECases.append(row['PatientID'])
                        break

    baselineTable = {}
    baselineTable['DRG Code'] = drgList
    baselineTable['Patient Count'] = len(los)
    baselineTable['Average LOS'] = round(sum(los) / len(los), 2)
    baselineTable['Total Cost (MM)'] = round(totalCost / 1000000, 2)
    baselineTable['Cost per day in $K'] = round(totalCost / (1000 * sum(los)), 2)
    baselineTable['Cost per patient in $K'] = round(totalCost / (1000 * len(los)), 2)

    morbidityDict = {}
    morbidityDict["Hypothermia"] = len(hypothermiaCases)
    morbidityDict["Sepsis"] = len(sepsisCases)
    morbidityDict["ROP"] = len(ropCases)
    morbidityDict["BPD"] = len(bpdCases)
    morbidityDict["NEC"] = len(necCases)
    morbidityDict["RDS"] = len(rdsCases)
    morbidityDict["Jaundice"] = len(jaundiceCases)
    morbidityDict["CVS"] = len(cvsCases)
    morbidityDict["Asphyxia"] = len(asphyxiaCases)
    morbidityDict["Hemorrhage"] = len(hemorrhageCases)
    morbidityDict["GI"] = len(giCases)
    morbidityDict["Normal"] = len(normalCases)
    morbidityDict["Apnea"] = len(ApneaCases)
    morbidityDict["Hypoglycemia"] = len(HypoglycemiaCases)
    morbidityDict["PPHN"] = len(PPHNCases)
    morbidityDict["Pneumothorax"] = len(PneumothoraxCases)
    morbidityDict["HIE"] = len(HIECases)

    sorted_morbidity = dict(sorted(morbidityDict.items(), key=operator.itemgetter(1), reverse=True))
    topK = 20
    i = 0

    baselineTable["Hypothermia"] = 0
    baselineTable["Sepsis"] = 0
    baselineTable["ROP"] = 0
    baselineTable["BPD"] = 0
    baselineTable["NEC"] = 0
    baselineTable["RDS"] = 0
    baselineTable["Jaundice"] = 0
    baselineTable["CVS"] = 0
    baselineTable["Asphyxia"] = 0
    baselineTable["Hemorrhage"] = 0
    baselineTable["GI"] = 0
    baselineTable["Normal"] = 0
    baselineTable["Apnea"] = 0
    baselineTable["Hypoglycemia"] = 0
    baselineTable["PPHN"] = 0
    baselineTable["Pneumothorax"] = 0
    baselineTable["HIE"] = 0

    for key in sorted_morbidity:
        if (morbidityDict.get(key)) > 0:
            if i == topK:
                break
            i = i + 1

            baselineTable[key] = sorted_morbidity.get(key)

    return baselineTable


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

baselineTable1 = DRFCodeDistribution(drgCodeGreaterthan500Lessthan750)
baselineTable2 = DRFCodeDistribution(drgCodeGreaterthan750Lessthan1000)
baselineTable3 = DRFCodeDistribution(drgCodeLessthan1000Only)
baselineTable4 = DRFCodeDistribution(drgCodeLessthan1000)
baselineTable5 = DRFCodeDistribution(drgCodeGreaterthan1000Lessthan1250)
baselineTable6 = DRFCodeDistribution(drgCodeGreaterthan1250Lessthan1500)
baselineTable7 = DRFCodeDistribution(drgCodeLessthan1500Only)
baselineTable8 = DRFCodeDistribution(drgCodeLessthan1500)
baselineTable9 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2000)
baselineTable10 = DRFCodeDistribution(drgCodeGreaterthan2000Lessthan2500)
baselineTable11 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500Only)
baselineTable12 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500)
baselineTable13 = DRFCodeDistribution(drgCodeGreaterthan2500)
baselineTable14 = DRFCodeDistribution(drgAll)

baselineTable = PrettyTable(["Weight categories (gm)",
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

baselineTable.add_row(['DRG Code', baselineTable1['DRG Code'], baselineTable2['DRG Code'],
      baselineTable3['DRG Code'], baselineTable4['DRG Code'],
      baselineTable5['DRG Code'], baselineTable6['DRG Code'], baselineTable7['DRG Code'],
      baselineTable8['DRG Code'], baselineTable9['DRG Code'], baselineTable10['DRG Code'],
      baselineTable11['DRG Code'], baselineTable12['DRG Code'], baselineTable13['DRG Code'],
      baselineTable14['DRG Code']])

baselineTable.add_row(['Patient Count', baselineTable1['Patient Count'], baselineTable2['Patient Count'],
      baselineTable3['Patient Count'], baselineTable4['Patient Count'],
      baselineTable5['Patient Count'], baselineTable6['Patient Count'], baselineTable7['Patient Count'],
      baselineTable8['Patient Count'], baselineTable9['Patient Count'], baselineTable10['Patient Count'],
      baselineTable11['Patient Count'], baselineTable12['Patient Count'], baselineTable13['Patient Count'],
      baselineTable14['Patient Count']])

baselineTable.add_row(['Average LOS', baselineTable1['Average LOS'], baselineTable2['Average LOS'],
      baselineTable3['Average LOS'], baselineTable4['Average LOS'],
      baselineTable5['Average LOS'], baselineTable6['Average LOS'], baselineTable7['Average LOS'],
      baselineTable8['Average LOS'], baselineTable9['Average LOS'], baselineTable10['Average LOS'],
      baselineTable11['Average LOS'], baselineTable12['Average LOS'], baselineTable13['Average LOS'],
      baselineTable14['Average LOS']])
baselineTable.add_row(['Total Cost (MM)', baselineTable1['Total Cost (MM)'], baselineTable2['Total Cost (MM)'],
      baselineTable3['Total Cost (MM)'], baselineTable4['Total Cost (MM)'],
      baselineTable5['Total Cost (MM)'], baselineTable6['Total Cost (MM)'], baselineTable7['Total Cost (MM)'],
      baselineTable8['Total Cost (MM)'], baselineTable9['Total Cost (MM)'], baselineTable10['Total Cost (MM)'],
      baselineTable11['Total Cost (MM)'], baselineTable12['Total Cost (MM)'], baselineTable13['Total Cost (MM)'],
      baselineTable14['Total Cost (MM)']])
baselineTable.add_row(['Cost per day in $K', baselineTable1['Cost per day in $K'], baselineTable2['Cost per day in $K'],
      baselineTable3['Cost per day in $K'], baselineTable4['Cost per day in $K'],
      baselineTable5['Cost per day in $K'], baselineTable6['Cost per day in $K'], baselineTable7['Cost per day in $K'],
      baselineTable8['Cost per day in $K'], baselineTable9['Cost per day in $K'], baselineTable10['Cost per day in $K'],
      baselineTable11['Cost per day in $K'], baselineTable12['Cost per day in $K'], baselineTable13['Cost per day in $K'],
      baselineTable14['Cost per day in $K']])
baselineTable.add_row(['Cost per patient in $K', baselineTable1['Cost per patient in $K'], baselineTable2['Cost per patient in $K'],
      baselineTable3['Cost per patient in $K'], baselineTable4['Cost per patient in $K'],
      baselineTable5['Cost per patient in $K'], baselineTable6['Cost per patient in $K'], baselineTable7['Cost per patient in $K'],
      baselineTable8['Cost per patient in $K'], baselineTable9['Cost per patient in $K'], baselineTable10['Cost per patient in $K'],
      baselineTable11['Cost per patient in $K'], baselineTable12['Cost per patient in $K'], baselineTable13['Cost per patient in $K'],
      baselineTable14['Cost per patient in $K']])
baselineTable.add_row(['RDS', baselineTable1['RDS'], baselineTable2['RDS'],
      baselineTable3['RDS'], baselineTable4['RDS'],
      baselineTable5['RDS'], baselineTable6['RDS'], baselineTable7['RDS'],
      baselineTable8['RDS'], baselineTable9['RDS'], baselineTable10['RDS'],
      baselineTable11['RDS'], baselineTable12['RDS'], baselineTable13['RDS'],
      baselineTable14['RDS']])
baselineTable.add_row(['Apnea', baselineTable1['Apnea'], baselineTable2['Apnea'],
      baselineTable3['Apnea'], baselineTable4['Apnea'],
      baselineTable5['Apnea'], baselineTable6['Apnea'], baselineTable7['Apnea'],
      baselineTable8['Apnea'], baselineTable9['Apnea'], baselineTable10['Apnea'],
      baselineTable11['Apnea'], baselineTable12['Apnea'], baselineTable13['Apnea'],
      baselineTable14['Apnea']])
baselineTable.add_row(['BPD', baselineTable1['BPD'], baselineTable2['BPD'],
      baselineTable3['BPD'], baselineTable4['BPD'],
      baselineTable5['BPD'], baselineTable6['BPD'], baselineTable7['BPD'],
      baselineTable8['BPD'], baselineTable9['BPD'], baselineTable10['BPD'],
      baselineTable11['BPD'], baselineTable12['BPD'], baselineTable13['BPD'],
      baselineTable14['BPD']])
baselineTable.add_row(['Sepsis', baselineTable1['Sepsis'], baselineTable2['Sepsis'],
      baselineTable3['Sepsis'], baselineTable4['Sepsis'],
      baselineTable5['Sepsis'], baselineTable6['Sepsis'], baselineTable7['Sepsis'],
      baselineTable8['Sepsis'], baselineTable9['Sepsis'], baselineTable10['Sepsis'],
      baselineTable11['Sepsis'], baselineTable12['Sepsis'], baselineTable13['Sepsis'],
      baselineTable14['Sepsis']])
baselineTable.add_row(['Hemorrhage', baselineTable1['Hemorrhage'], baselineTable2['Hemorrhage'],
      baselineTable3['Hemorrhage'], baselineTable4['Hemorrhage'],
      baselineTable5['Hemorrhage'], baselineTable6['Hemorrhage'], baselineTable7['Hemorrhage'],
      baselineTable8['Hemorrhage'], baselineTable9['Hemorrhage'], baselineTable10['Hemorrhage'],
      baselineTable11['Hemorrhage'], baselineTable12['Hemorrhage'], baselineTable13['Hemorrhage'],
      baselineTable14['Hemorrhage']])

baselineTable.add_row(['Pneumothorax', baselineTable1['Pneumothorax'], baselineTable2['Pneumothorax'],
      baselineTable3['Pneumothorax'], baselineTable4['Pneumothorax'],
      baselineTable5['Pneumothorax'], baselineTable6['Pneumothorax'], baselineTable7['Pneumothorax'],
      baselineTable8['Pneumothorax'], baselineTable9['Pneumothorax'], baselineTable10['Pneumothorax'],
      baselineTable11['Pneumothorax'], baselineTable12['Pneumothorax'], baselineTable13['Pneumothorax'],
      baselineTable14['Pneumothorax']])
baselineTable.add_row(['GI', baselineTable1['GI'], baselineTable2['GI'],
      baselineTable3['GI'], baselineTable4['GI'],
      baselineTable5['GI'], baselineTable6['GI'], baselineTable7['GI'],
      baselineTable8['GI'], baselineTable9['GI'], baselineTable10['GI'],
      baselineTable11['GI'], baselineTable12['GI'], baselineTable13['GI'],
      baselineTable14['GI']])
baselineTable.add_row(['Jaundice', baselineTable1['Jaundice'], baselineTable2['Jaundice'],
      baselineTable3['Jaundice'], baselineTable4['Jaundice'],
      baselineTable5['Jaundice'], baselineTable6['Jaundice'], baselineTable7['Jaundice'],
      baselineTable8['Jaundice'], baselineTable9['Jaundice'], baselineTable10['Jaundice'],
      baselineTable11['Jaundice'], baselineTable12['Jaundice'], baselineTable13['Jaundice'],
      baselineTable14['Jaundice']])
baselineTable.add_row(['NEC', baselineTable1['NEC'], baselineTable2['NEC'],
      baselineTable3['NEC'], baselineTable4['NEC'],
      baselineTable5['NEC'], baselineTable6['NEC'], baselineTable7['NEC'],
      baselineTable8['NEC'], baselineTable9['NEC'], baselineTable10['NEC'],
      baselineTable11['NEC'], baselineTable12['NEC'], baselineTable13['NEC'],
      baselineTable14['NEC']])
baselineTable.add_row(['ROP', baselineTable1['ROP'], baselineTable2['ROP'],
      baselineTable3['ROP'], baselineTable4['ROP'],
      baselineTable5['ROP'], baselineTable6['ROP'], baselineTable7['ROP'],
      baselineTable8['ROP'], baselineTable9['ROP'], baselineTable10['ROP'],
      baselineTable11['ROP'], baselineTable12['ROP'], baselineTable13['ROP'],
      baselineTable14['ROP']])
baselineTable.add_row(['PPHN', baselineTable1['PPHN'], baselineTable2['PPHN'],
      baselineTable3['PPHN'], baselineTable4['PPHN'],
      baselineTable5['PPHN'], baselineTable6['PPHN'], baselineTable7['PPHN'],
      baselineTable8['PPHN'], baselineTable9['PPHN'], baselineTable10['PPHN'],
      baselineTable11['PPHN'], baselineTable12['PPHN'], baselineTable13['PPHN'],
      baselineTable14['PPHN']])
baselineTable.add_row(['Asphyxia', baselineTable1['Asphyxia'], baselineTable2['Asphyxia'],
      baselineTable3['Asphyxia'], baselineTable4['Asphyxia'],
      baselineTable5['Asphyxia'], baselineTable6['Asphyxia'], baselineTable7['Asphyxia'],
      baselineTable8['Asphyxia'], baselineTable9['Asphyxia'], baselineTable10['Asphyxia'],
      baselineTable11['Asphyxia'], baselineTable12['Asphyxia'], baselineTable13['Asphyxia'],
      baselineTable14['Asphyxia']])
baselineTable.add_row(['Hypoglycemia', baselineTable1['Hypoglycemia'], baselineTable2['Hypoglycemia'],
      baselineTable3['Hypoglycemia'], baselineTable4['Hypoglycemia'],
      baselineTable5['Hypoglycemia'], baselineTable6['Hypoglycemia'], baselineTable7['Hypoglycemia'],
      baselineTable8['Hypoglycemia'], baselineTable9['Hypoglycemia'], baselineTable10['Hypoglycemia'],
      baselineTable11['Hypoglycemia'], baselineTable12['Hypoglycemia'], baselineTable13['Hypoglycemia'],
      baselineTable14['Hypoglycemia']])
baselineTable.add_row(['Hypothermia', baselineTable1['Hypothermia'], baselineTable2['Hypothermia'],
      baselineTable3['Hypothermia'], baselineTable4['Hypothermia'],
      baselineTable5['Hypothermia'], baselineTable6['Hypothermia'], baselineTable7['Hypothermia'],
      baselineTable8['Hypothermia'], baselineTable9['Hypothermia'], baselineTable10['Hypothermia'],
      baselineTable11['Hypothermia'], baselineTable12['Hypothermia'], baselineTable13['Hypothermia'],
      baselineTable14['Hypothermia']])
baselineTable.add_row(['HIE', baselineTable1['HIE'], baselineTable2['HIE'],
      baselineTable3['HIE'], baselineTable4['HIE'],
      baselineTable5['HIE'], baselineTable6['HIE'], baselineTable7['HIE'],
      baselineTable8['HIE'], baselineTable9['HIE'], baselineTable10['HIE'],
      baselineTable11['HIE'], baselineTable12['HIE'], baselineTable13['HIE'],
      baselineTable14['HIE']])

print(baselineTable)

rateTable = PrettyTable(["Weight categories",
    "Sepsis Rate","BPD Rate","NEC Rate","Pneumothorax Rate","Hemorrhage Rate"])

rateTable.add_row(['500- <1000', round((baselineTable4['Sepsis']/baselineTable4['Patient Count'])*100), round((baselineTable4['BPD']/baselineTable4['Patient Count'])*100),round((baselineTable4['NEC']/baselineTable4['Patient Count'])*100),round((baselineTable4['Pneumothorax']/baselineTable4['Patient Count'])*100),round((baselineTable4['Hemorrhage']/baselineTable4['Patient Count'])*100)])
rateTable.add_row(['1000- <1500', round((baselineTable8['Sepsis']/baselineTable8['Patient Count'])*100), round((baselineTable8['BPD']/baselineTable8['Patient Count'])*100),round((baselineTable8['NEC']/baselineTable8['Patient Count'])*100),round((baselineTable8['Pneumothorax']/baselineTable8['Patient Count'])*100),round((baselineTable8['Hemorrhage']/baselineTable8['Patient Count'])*100)])
rateTable.add_row(['1500- <2500', round((baselineTable12['Sepsis']/baselineTable12['Patient Count'])*100), round((baselineTable12['BPD']/baselineTable12['Patient Count'])*100),round((baselineTable12['NEC']/baselineTable12['Patient Count'])*100),round((baselineTable12['Pneumothorax']/baselineTable12['Patient Count'])*100),round((baselineTable12['Hemorrhage']/baselineTable12['Patient Count'])*100)])
rateTable.add_row(['>2500', round((baselineTable13['Sepsis']/baselineTable13['Patient Count'])*100), round((baselineTable13['BPD']/baselineTable13['Patient Count'])*100),round((baselineTable13['NEC']/baselineTable13['Patient Count'])*100),round((baselineTable13['Pneumothorax']/baselineTable13['Patient Count'])*100),round((baselineTable13['Hemorrhage']/baselineTable13['Patient Count'])*100)])
rateTable.add_row(['All', round((baselineTable14['Sepsis']/baselineTable14['Patient Count'])*100), round((baselineTable14['BPD']/baselineTable14['Patient Count'])*100),round((baselineTable14['NEC']/baselineTable14['Patient Count'])*100),round((baselineTable14['Pneumothorax']/baselineTable14['Patient Count'])*100),round((baselineTable14['Hemorrhage']/baselineTable14['Patient Count'])*100)])

print(rateTable)