import operator
import pandas as pd
import matplotlib.pyplot as plt
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

    pneumoPatients = []
    pneumoNonPatients = []

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
                isPneumo = False
                isRDS = False
                isPatientICD = False

                for code in hypothermiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break

                for code in sepsisICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break

                for code in necICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in ropICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in bpdICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
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
                        break
                for code in cvsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in giICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in hemorrhageICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in asphyxiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in apneaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in hypoglycemiaICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in hieICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
                        break
                for code in pphnICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPatientICD = True
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
                        break

                los.append(row['LOS'])
                for index1, encounter in encounterRows.iterrows():

                    if (encounter['Total Direct Variable Cost'] > 0):
                        if (encounter['Activity Desc'] in surfactantList):
                            isSurfactant = True

                if isSurfactant and isRDS:
                    if (isPneumo):

                        if (not isPatientICD):
                            pneumoPatients.append(row['Hashed MRN'])
                    else:
                        if (not isPatientICD):
                            pneumoNonPatients.append(row['Hashed MRN'])
    dictCost = {}
    subDictCost = {}
    subsubDictCost = {}

    subDictCount = {}
    subsubDictCount = {}

    mappingL1L2 = {}
    mappingL2L3 = {}

    activityList = ["Room and Board","Statistics","Resp Therapy","Pharmacy","Lab","OT/PT/ST","Rehab","Radiology","Supply","All Other","OR/Anesthesia","Blood","Cardiac Services"]

    #Calculating cost of pneumoPatients
    for uhid in pneumoPatients:
        sb = encounterofPatients[encounterofPatients['Hashed MRN'] == uhid]
        for obj in set(activityList):
            sb1 = sb[sb['UB Revenue Activity Group'] == obj]
            if obj in dictCost:
                prevCost = dictCost[obj]
                dictCost[obj] = prevCost + sum(sb1['Total Direct Variable Cost'])
            else:
                dictCost[obj] = sum(sb1['Total Direct Variable Cost'])

            for index, encounter in sb1.iterrows():
                obj1 = encounter['UB Rev Desc']
                if obj1 in subDictCost:
                    prevCost = subDictCost[obj1]
                    subDictCost[obj1] = prevCost + encounter['Total Direct Variable Cost']
                else:
                    subDictCost[obj1] = encounter['Total Direct Variable Cost']

                if obj in mappingL1L2:
                    currentList = mappingL1L2[obj]
                    currentList.append(obj1)
                    mappingL1L2[obj] = currentList
                else:
                    currentList = []
                    currentList.append(obj1)
                    mappingL1L2[obj] = currentList

                if obj1 in subDictCount:
                    currentList = subDictCount[obj1]
                    currentList.append(uhid)
                    subDictCount[obj1] = currentList
                else:
                    currentList = []
                    currentList.append(uhid)
                    subDictCount[obj1] = currentList

                obj2 = encounter['Activity Desc']
                if obj2 in subsubDictCost:
                    prevCost = subsubDictCost[obj2]
                    subsubDictCost[obj2] = prevCost + (encounter['Total Direct Variable Cost'])
                else:
                    subsubDictCost[obj2] = (encounter['Total Direct Variable Cost'])

                if obj1 in mappingL2L3:
                    currentList = mappingL2L3[obj1]
                    currentList.append(obj2)
                    mappingL2L3[obj1] = currentList
                else:
                    currentList = []
                    currentList.append(obj2)
                    mappingL2L3[obj1] = currentList

                if obj2 in subsubDictCount:
                    currentList = subsubDictCount[obj2]
                    currentList.append(uhid)
                    subDictCount[obj2] = currentList
                else:
                    currentList = []
                    currentList.append(uhid)
                    subsubDictCount[obj2] = currentList

    for obj in dictCost:
        dictCost[obj] = dictCost[obj] / len(pneumoPatients)

    for obj in subDictCost:
        subDictCost[obj] = subDictCost[obj] / len(set(subDictCount[obj]))

    for obj in subsubDictCost:
        subsubDictCost[obj] = subsubDictCost[obj] / len(set(subsubDictCount[obj]))

    sorted_d = dict(sorted(dictCost.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted_d)

    dictCostNo = {}
    subdictCostNo = {}
    subsubdictCostNo = {}

    subdictCountNo = {}
    subsubdictCountNo = {}

    mappingNoL1L2 = {}
    mappingNoL2L3 = {}

    # Calculating cost of Non pneumoPatients
    for uhid in pneumoNonPatients:
        sb = encounterofPatients[encounterofPatients['Hashed MRN'] == uhid]
        for obj in set(activityList):
            sb1 = sb[sb['UB Revenue Activity Group'] == obj]
            if obj in dictCostNo:
                prevCost = dictCostNo[obj]
                dictCostNo[obj] = prevCost + sum(sb1['Total Direct Variable Cost'])
            else:
                dictCostNo[obj] = sum(sb1['Total Direct Variable Cost'])

            for index, encounter in sb1.iterrows():
                obj1 = encounter['UB Rev Desc']
                if obj1 in subdictCostNo:
                    prevCost = subdictCostNo[obj1]
                    subdictCostNo[obj1] = prevCost + encounter['Total Direct Variable Cost']
                else:
                    subdictCostNo[obj1] = encounter['Total Direct Variable Cost']

                if obj in mappingNoL1L2:
                    currentList = mappingNoL1L2[obj]
                    currentList.append(obj1)
                    mappingNoL1L2[obj] = currentList
                else:
                    currentList = []
                    currentList.append(obj1)
                    mappingNoL1L2[obj] = currentList

                if obj1 in subdictCountNo:
                    currentList = subdictCountNo[obj1]
                    currentList.append(uhid)
                    subdictCountNo[obj1] = currentList
                else:
                    currentList = []
                    currentList.append(uhid)
                    subdictCountNo[obj1] = currentList

                obj2 = encounter['Activity Desc']
                if obj2 in subsubdictCostNo:
                    prevCost = subsubdictCostNo[obj2]
                    subsubdictCostNo[obj2] = prevCost + (encounter['Total Direct Variable Cost'])
                else:
                    subsubdictCostNo[obj2] = (encounter['Total Direct Variable Cost'])

                if obj1 in mappingNoL2L3:
                    currentList = mappingNoL2L3[obj1]
                    currentList.append(obj2)
                    mappingNoL2L3[obj1] = currentList
                else:
                    currentList = []
                    currentList.append(obj2)
                    mappingNoL2L3[obj1] = currentList

                if obj2 in subsubdictCountNo:
                    currentList = subsubdictCountNo[obj2]
                    currentList.append(uhid)
                    subdictCountNo[obj2] = currentList
                else:
                    currentList = []
                    currentList.append(uhid)
                    subsubdictCountNo[obj2] = currentList

    for obj in dictCostNo:
        dictCostNo[obj] = dictCostNo[obj] / len(pneumoNonPatients)

    for obj in subdictCostNo:
        subdictCostNo[obj] = subdictCostNo[obj] / len(set(subdictCountNo[obj]))

    for obj in subsubdictCostNo:
        subsubdictCostNo[obj] = subsubdictCostNo[obj] / len(set(subsubdictCountNo[obj]))

    sorted_dNo = dict(sorted(dictCostNo.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted_dNo)

    df = pd.DataFrame([['Pneumothorax', round(sorted_d['Room and Board']/1000),  round(sorted_d['Statistics']/1000),  round(sorted_d['Resp Therapy']/1000),  round(sorted_d['Pharmacy']/1000), round(sorted_d['Lab']/1000), round(sorted_d['OT/PT/ST']/1000)], ['Normal', round(sorted_dNo['Room and Board']/1000), round(sorted_dNo['Statistics']/1000), round(sorted_dNo['Resp Therapy']/1000), round(sorted_dNo['Pharmacy']/1000),round(sorted_dNo['Lab']/1000),round(sorted_dNo['OT/PT/ST']/1000)]],
                      columns=['Services', 'Room and Board', 'Statistics', 'Resp Therapy', 'Pharmacy','Lab','OT/PT/ST'])
    # view data
    print(df)

    # plot data in stack manner of bar type
    df.plot(x='Services',




            kind='bar', stacked=True,
            title='Comparison between Pneumothorax and Normal Patient in terms of cost')
    plt.show()

    # Calculating difference of cost in Pneumo and Non-pneumo patients
    diffL1 = {}
    for obj in sorted_dNo:

        diffL1[obj] = sorted_d[obj] - sorted_dNo[obj]
        print(obj, ' : ', round(abs(diffL1[obj])/1000,2))
        if (obj in mappingNoL1L2):
            if (obj in mappingL1L2):
                currentList = mappingL1L2[obj]
                currentListNo = mappingNoL1L2[obj]
                tempDict = {}
                tempDictNo = {}
                for item in currentListNo:
                    tempDictNo[item] = subdictCostNo[item]
                for item in currentList:
                    tempDict[item] = subDictCost[item]

                sorted_1 = dict(sorted(tempDict.items(), key=operator.itemgetter(1), reverse=True))
                sorted_1No = dict(sorted(tempDictNo.items(), key=operator.itemgetter(1), reverse=True))

                diffL2 = {}
                for itemobj1 in sorted_1No:
                    if (itemobj1 in sorted_1):
                        diffL2[itemobj1] = sorted_1[itemobj1] - sorted_1No[itemobj1]

                sorted_diffL2 = dict(sorted(diffL2.items(), key=operator.itemgetter(1), reverse=True))

                counter = 0
                for itemobj1 in sorted_diffL2:
                    if (counter >= 3):
                        continue

                    if (itemobj1 in mappingNoL2L3 and itemobj1 in mappingL2L3):
                        print('.', itemobj1, ' : ', round(abs(sorted_diffL2[itemobj1])/1000,2))
                        counter = counter + 1
                        currentListL2No = mappingNoL2L3[itemobj1]
                        currentListL2 = mappingL2L3[itemobj1]
                        tempDictL2 = {}
                        tempDictL2No = {}
                        for item in currentListL2No:
                            tempDictL2No[item] = subsubdictCostNo[item]
                        for item in currentListL2:
                            tempDictL2[item] = subsubDictCost[item]

                        sorted_2 = dict(sorted(tempDictL2.items(), key=operator.itemgetter(1), reverse=True))
                        sorted_2No = dict(sorted(tempDictL2No.items(), key=operator.itemgetter(1), reverse=True))

                        diffL3 = {}
                        for itemobj2 in sorted_2No:
                            if (itemobj2 in sorted_2):
                                diffL3[itemobj2] = sorted_2[itemobj2] - sorted_2No[itemobj2]

                        sorted_diffL3 = dict(sorted(diffL3.items(), key=operator.itemgetter(1), reverse=True))

                        counter1 = 0
                        for itemobj2 in sorted_diffL3:
                            if (counter1 >= 3):
                                continue
                            counter1 = counter1 + 1
                            print('..', itemobj2, ' : ', round(abs(sorted_diffL3[itemobj2])/1000,2))

excelPathHospitalCost = 'Hospital Costs.xlsx'
providerCost = loadData('451502252_texas-health-harris-methodist-hospital-alliance_standardcharges 10-28-22.csv')
hospitalCostExcel = loadExcel(excelPathHospitalCost)
patientMaster = hospitalCostExcel.parse("PatientMaster")
encounterofPatients = hospitalCostExcel.parse("Encounter Level")
itemizedFinancials = hospitalCostExcel.parse("Financials Itemized")

drgAll = [626, 622, 625, 621, 623, 609, 614, 612, 611, 613, 588, 607, 602, 593, 591, 589, 608, 603, 640, 634, 639, 633,
          631, 636]

DRFCodeDistribution(drgAll)