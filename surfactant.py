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

    rdsICD = ['P22.0', 'P22.1', 'P22.8', 'P22.9', 'P28.5', 'P28.89', 'P28.9']

    pneumothoraxICD = ['P25.1']

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

    surfactantRDSCost = []
    nonsurfactantRDSCost = []

    surfactantLOS = []
    nonsurfactantLOS = []

    surfactantLOSPneumothorax = []
    nonsurfactantLOSPneumothorax = []
    surfactantCost = 0

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
                currsurfactantCost = 0
                dictDates = {}



                for code in pneumothoraxICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isPneumo = True
                        break

                los.append(row['LOS'])

                for index1, encounter in encounterRows.iterrows():

                    dictDates[encounter['Service Dt']] = 1

                    if (encounter['Total Direct Variable Cost'] > 0):

                        if (encounter['Activity Desc'] in surfactantList):
                            isSurfactant = True
                            currsurfactantCost = currsurfactantCost + encounter['Total Direct Variable Cost']

                for code in rdsICD:
                    if (value1.__contains__(code) or value2.__contains__(code) or value3.__contains__(
                            code) or value4.__contains__(code) or value5.__contains__(code)):
                        isRDS = True
                        break
                if isSurfactant and isRDS:

                    surfactantRDSCost.append(row['Total_Direct_Variable_Cost'])

                    surfactantCost = surfactantCost + currsurfactantCost
                    surfactantLOS.append(row['LOS'])
                    if (isPneumo):
                        surfactantLOSPneumothorax.append(row['LOS'])

                elif isRDS and not isSurfactant:
                    nonsurfactantRDSCost.append(row['Total_Direct_Variable_Cost'])
                    nonsurfactantLOS.append(row['LOS'])

                    if isPneumo:
                        nonsurfactantLOSPneumothorax.append(row['LOS'])

    morbidityDict = {}
    morbidityDict['Surfactant Count'] = len(surfactantLOS)
    if(len(surfactantLOS) > 0):
        morbidityDict['Surfactant Average LOS'] = round(sum(surfactantLOS) / len(surfactantLOS), 2)
    else:
        morbidityDict['Surfactant Average LOS'] = '-'
    if(len(surfactantLOS) > 0):
        morbidityDict['Pneumothorax Count'] = len(surfactantLOSPneumothorax), '/', round((len(surfactantLOSPneumothorax)/len(surfactantLOS))*100,2)
    else:
        morbidityDict['Pneumothorax Count'] = '-'
    if (len(surfactantLOS) > 0):
        morbidityDict['Surfactant Cost per patient'] = round((surfactantCost) / len(surfactantLOS), 2)
    else:
        morbidityDict['Surfactant Cost per patient'] = '-'
    if (len(surfactantRDSCost) > 0):
        morbidityDict['Average Total Cost'] = round((sum(surfactantRDSCost)) / len(surfactantRDSCost) / 1000, 2)
    else:
        morbidityDict['Average Total Cost'] = '-'
    morbidityDict['Non Surfactant Count'] = len(nonsurfactantLOS)
    if (len(nonsurfactantLOS) > 0):
        morbidityDict['Non Surfactant Average LOS'] = round(sum(nonsurfactantLOS) / len(nonsurfactantLOS), 2)
    else:
        morbidityDict['Non Surfactant Average LOS'] = '-'
    if(len(nonsurfactantLOS) > 0):
        morbidityDict['Non Surfactant Pneumothorax Count'] = len(nonsurfactantLOSPneumothorax) , '/', round((len(nonsurfactantLOSPneumothorax)/len(nonsurfactantLOS))*100,2)
    else:
        morbidityDict['Non Surfactant Pneumothorax Count'] = '-'
    if (len(nonsurfactantRDSCost) > 0):
        morbidityDict['Non Surfactant Average Total Cost'] = round((sum(nonsurfactantRDSCost)) / len(nonsurfactantRDSCost) / 1000, 2)
    else:
        morbidityDict['Non Surfactant Average Total Cost'] = '-'

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

surfactantTable1 = DRFCodeDistribution(drgCodeGreaterthan500Lessthan750)
surfactantTable2 = DRFCodeDistribution(drgCodeGreaterthan750Lessthan1000)
surfactantTable3 = DRFCodeDistribution(drgCodeLessthan1000Only)
surfactantTable4 = DRFCodeDistribution(drgCodeLessthan1000)
surfactantTable5 = DRFCodeDistribution(drgCodeGreaterthan1000Lessthan1250)
surfactantTable6 = DRFCodeDistribution(drgCodeGreaterthan1250Lessthan1500)
surfactantTable7 = DRFCodeDistribution(drgCodeLessthan1500Only)
surfactantTable8 = DRFCodeDistribution(drgCodeLessthan1500)
surfactantTable9 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2000)
surfactantTable10 = DRFCodeDistribution(drgCodeGreaterthan2000Lessthan2500)
surfactantTable11 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500Only)
surfactantTable12 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500)
surfactantTable13 = DRFCodeDistribution(drgCodeGreaterthan2500)
surfactantTable14 = DRFCodeDistribution(drgAll)

surfactantTable = PrettyTable(["Weight categories (gm)",
    "Surfactant Count",
    "Surfactant Average LOS",
    "Pneumothorax Count",
    "Surfactant Cost per patient",
    "Average Total Cost",
    "Non Surfactant Count",
    "Non Surfactant Average LOS",
    "Non Surfactant Pneumothorax Count",
    "Non Surfactant Average Total Cost"])

surfactantTable.add_row(['500-750', surfactantTable1['Surfactant Count'], surfactantTable1['Surfactant Average LOS'],
      surfactantTable1['Pneumothorax Count'], surfactantTable1['Surfactant Cost per patient'],
      surfactantTable1['Average Total Cost'], surfactantTable1['Non Surfactant Count'], surfactantTable1['Non Surfactant Average LOS'],
      surfactantTable1['Non Surfactant Pneumothorax Count'], surfactantTable1['Non Surfactant Average Total Cost']])

surfactantTable.add_row(['750-1000', surfactantTable2['Surfactant Count'], surfactantTable2['Surfactant Average LOS'],
      surfactantTable2['Pneumothorax Count'], surfactantTable2['Surfactant Cost per patient'],
      surfactantTable2['Average Total Cost'], surfactantTable2['Non Surfactant Count'], surfactantTable2['Non Surfactant Average LOS'],
      surfactantTable2['Non Surfactant Pneumothorax Count'], surfactantTable2['Non Surfactant Average Total Cost']])

surfactantTable.add_row(['<1000', surfactantTable3['Surfactant Count'], surfactantTable3['Surfactant Average LOS'],
      surfactantTable3['Pneumothorax Count'], surfactantTable3['Surfactant Cost per patient'],
      surfactantTable3['Average Total Cost'], surfactantTable3['Non Surfactant Count'], surfactantTable3['Non Surfactant Average LOS'],
      surfactantTable3['Non Surfactant Pneumothorax Count'], surfactantTable3['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['Total 500-1000', surfactantTable4['Surfactant Count'], surfactantTable4['Surfactant Average LOS'],
      surfactantTable4['Pneumothorax Count'], surfactantTable4['Surfactant Cost per patient'],
      surfactantTable4['Average Total Cost'], surfactantTable4['Non Surfactant Count'], surfactantTable4['Non Surfactant Average LOS'],
      surfactantTable4['Non Surfactant Pneumothorax Count'], surfactantTable4['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['1000-1250', surfactantTable5['Surfactant Count'], surfactantTable5['Surfactant Average LOS'],
      surfactantTable5['Pneumothorax Count'], surfactantTable5['Surfactant Cost per patient'],
      surfactantTable5['Average Total Cost'], surfactantTable5['Non Surfactant Count'], surfactantTable5['Non Surfactant Average LOS'],
      surfactantTable5['Non Surfactant Pneumothorax Count'], surfactantTable5['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['1250-1500', surfactantTable6['Surfactant Count'], surfactantTable6['Surfactant Average LOS'],
      surfactantTable6['Pneumothorax Count'], surfactantTable6['Surfactant Cost per patient'],
      surfactantTable6['Average Total Cost'], surfactantTable6['Non Surfactant Count'], surfactantTable6['Non Surfactant Average LOS'],
      surfactantTable6['Non Surfactant Pneumothorax Count'], surfactantTable6['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['<1500', surfactantTable7['Surfactant Count'], surfactantTable7['Surfactant Average LOS'],
      surfactantTable7['Pneumothorax Count'], surfactantTable7['Surfactant Cost per patient'],
      surfactantTable7['Average Total Cost'], surfactantTable7['Non Surfactant Count'], surfactantTable7['Non Surfactant Average LOS'],
      surfactantTable7['Non Surfactant Pneumothorax Count'], surfactantTable7['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['Total 500-1500', surfactantTable8['Surfactant Count'], surfactantTable8['Surfactant Average LOS'],
      surfactantTable8['Pneumothorax Count'], surfactantTable8['Surfactant Cost per patient'],
      surfactantTable8['Average Total Cost'], surfactantTable8['Non Surfactant Count'], surfactantTable8['Non Surfactant Average LOS'],
      surfactantTable8['Non Surfactant Pneumothorax Count'], surfactantTable8['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['1500-2000', surfactantTable9['Surfactant Count'], surfactantTable9['Surfactant Average LOS'],
      surfactantTable9['Pneumothorax Count'], surfactantTable9['Surfactant Cost per patient'],
      surfactantTable9['Average Total Cost'], surfactantTable9['Non Surfactant Count'], surfactantTable9['Non Surfactant Average LOS'],
      surfactantTable9['Non Surfactant Pneumothorax Count'], surfactantTable9['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['2000-2500', surfactantTable10['Surfactant Count'], surfactantTable10['Surfactant Average LOS'],
      surfactantTable10['Pneumothorax Count'], surfactantTable10['Surfactant Cost per patient'],
      surfactantTable10['Average Total Cost'], surfactantTable10['Non Surfactant Count'], surfactantTable10['Non Surfactant Average LOS'],
      surfactantTable10['Non Surfactant Pneumothorax Count'], surfactantTable10['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['1500-2500', surfactantTable11['Surfactant Count'], surfactantTable11['Surfactant Average LOS'],
      surfactantTable11['Pneumothorax Count'], surfactantTable11['Surfactant Cost per patient'],
      surfactantTable11['Average Total Cost'], surfactantTable11['Non Surfactant Count'], surfactantTable11['Non Surfactant Average LOS'],
      surfactantTable11['Non Surfactant Pneumothorax Count'], surfactantTable11['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['Total 1500-2500', surfactantTable12['Surfactant Count'], surfactantTable12['Surfactant Average LOS'],
      surfactantTable12['Pneumothorax Count'], surfactantTable12['Surfactant Cost per patient'],
      surfactantTable12['Average Total Cost'], surfactantTable12['Non Surfactant Count'], surfactantTable12['Non Surfactant Average LOS'],
      surfactantTable12['Non Surfactant Pneumothorax Count'], surfactantTable12['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['>2500', surfactantTable13['Surfactant Count'], surfactantTable13['Surfactant Average LOS'],
      surfactantTable13['Pneumothorax Count'], surfactantTable13['Surfactant Cost per patient'],
      surfactantTable13['Average Total Cost'], surfactantTable13['Non Surfactant Count'], surfactantTable13['Non Surfactant Average LOS'],
      surfactantTable13['Non Surfactant Pneumothorax Count'], surfactantTable13['Non Surfactant Average Total Cost']])
surfactantTable.add_row(['All', surfactantTable14['Surfactant Count'], surfactantTable14['Surfactant Average LOS'],
      surfactantTable14['Pneumothorax Count'], surfactantTable14['Surfactant Cost per patient'],
      surfactantTable14['Average Total Cost'], surfactantTable14['Non Surfactant Count'], surfactantTable14['Non Surfactant Average LOS'],
      surfactantTable14['Non Surfactant Pneumothorax Count'], surfactantTable14['Non Surfactant Average Total Cost']])



print(surfactantTable)