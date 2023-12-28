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
    congenital_lunSupplyCD = ['Q33.0', 'Q33.2', 'Q33.6', 'Q33.8']
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

    costAnalysisTable = {}
    costAnalysisTable["Room and Board"] = []
    costAnalysisTable["Statistics"] = []
    costAnalysisTable["Resp Therapy"] = []
    costAnalysisTable["Pharmacy"] = []
    costAnalysisTable["Lab"] = []
    costAnalysisTable["OT/PT/ST"] = []
    costAnalysisTable["Rehab"] = []
    costAnalysisTable["Radiology"] = []
    costAnalysisTable["Supply"] = []
    costAnalysisTable["All Other"] = []
    costAnalysisTable["OR/Anesthesia"] = []
    costAnalysisTable["Blood"] = []
    costAnalysisTable["Cardiac Services"] = []

    activityList = ["Room and Board","Statistics","Resp Therapy","Pharmacy","Lab","OT/PT/ST","Rehab","Radiology","Supply","All Other","OR/Anesthesia","Blood","Cardiac Services"]

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
            for code in congenital_lunSupplyCD:
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
                los.append(row['LOS'])
                totalCost = totalCost + sum(encounterRows['Total Direct Variable Cost'])

                for activity in activityList:
                    encounterRowsFilter = encounterRows[encounterRows['UB Revenue Activity Group'] == activity]
                    costAnalysisTable[activity].append(sum(encounterRowsFilter['Total Direct Cost']))

    costAnalysisTable['DRG Code'] = drgList
    costAnalysisTable['Patient Count'] = len(los)
    costAnalysisTable['Average LOS'] = round(sum(los) / len(los), 2)
    costAnalysisTable['Cost per patient in $K'] = round(totalCost / (1000 * len(los)), 2)

    costAnalysisTable["Room and Board"] = round(sum(costAnalysisTable["Room and Board"]) / 1000 / len(costAnalysisTable["Room and Board"]),2)
    costAnalysisTable["Statistics"] = round(sum(costAnalysisTable["Statistics"]) / 1000 / len(costAnalysisTable["Statistics"]),2)
    costAnalysisTable["Resp Therapy"] = round(sum(costAnalysisTable["Resp Therapy"]) / 1000 / len(costAnalysisTable["Resp Therapy"]),2)
    costAnalysisTable["Pharmacy"] = round(sum(costAnalysisTable["Pharmacy"]) / 1000 / len(costAnalysisTable["Pharmacy"]),2)
    costAnalysisTable["Lab"] = round(sum(costAnalysisTable["Lab"]) / 1000 / len(costAnalysisTable["Lab"]),2)
    costAnalysisTable["OT/PT/ST"] = round(sum(costAnalysisTable["OT/PT/ST"]) / 1000 / len(costAnalysisTable["OT/PT/ST"]),2)
    costAnalysisTable["Rehab"] = round(sum(costAnalysisTable["Rehab"]) / 1000 / len(costAnalysisTable["Rehab"]),2)
    costAnalysisTable["Radiology"] = round(sum(costAnalysisTable["Radiology"]) / 1000 / len(costAnalysisTable["Radiology"]),2)
    costAnalysisTable["Supply"] = round(sum(costAnalysisTable["Supply"]) / 1000 / len(costAnalysisTable["Supply"]),2)
    costAnalysisTable["All Other"] = round(sum(costAnalysisTable["All Other"]) / 1000 / len(costAnalysisTable["All Other"]),2)
    costAnalysisTable["OR/Anesthesia"] = round(sum(costAnalysisTable["OR/Anesthesia"]) / 1000 / len(costAnalysisTable["OR/Anesthesia"]),2)
    costAnalysisTable["Blood"] = round(sum(costAnalysisTable["Blood"]) / 1000 / len(costAnalysisTable["Blood"]),2)
    costAnalysisTable["Cardiac Services"] = round(sum(costAnalysisTable["Cardiac Services"]) / 1000 / len(costAnalysisTable["Cardiac Services"]),2)
    return costAnalysisTable

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

costAnalysisTable1 = DRFCodeDistribution(drgCodeGreaterthan500Lessthan750)
costAnalysisTable2 = DRFCodeDistribution(drgCodeGreaterthan750Lessthan1000)
costAnalysisTable3 = DRFCodeDistribution(drgCodeLessthan1000Only)
costAnalysisTable4 = DRFCodeDistribution(drgCodeLessthan1000)
costAnalysisTable5 = DRFCodeDistribution(drgCodeGreaterthan1000Lessthan1250)
costAnalysisTable6 = DRFCodeDistribution(drgCodeGreaterthan1250Lessthan1500)
costAnalysisTable7 = DRFCodeDistribution(drgCodeLessthan1500Only)
costAnalysisTable8 = DRFCodeDistribution(drgCodeLessthan1500)
costAnalysisTable9 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2000)
costAnalysisTable10 = DRFCodeDistribution(drgCodeGreaterthan2000Lessthan2500)
costAnalysisTable11 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500Only)
costAnalysisTable12 = DRFCodeDistribution(drgCodeGreaterthan1500Lessthan2500)
costAnalysisTable13 = DRFCodeDistribution(drgCodeGreaterthan2500)
costAnalysisTable14 = DRFCodeDistribution(drgAll)

costAnalysisTable = PrettyTable(["Weight categories (gm)",
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

costAnalysisTable.add_row(['DRG Code', costAnalysisTable1['DRG Code'], costAnalysisTable2['DRG Code'],
      costAnalysisTable3['DRG Code'], costAnalysisTable4['DRG Code'],
      costAnalysisTable5['DRG Code'], costAnalysisTable6['DRG Code'], costAnalysisTable7['DRG Code'],
      costAnalysisTable8['DRG Code'], costAnalysisTable9['DRG Code'], costAnalysisTable10['DRG Code'],
      costAnalysisTable11['DRG Code'], costAnalysisTable12['DRG Code'], costAnalysisTable13['DRG Code'],
      costAnalysisTable14['DRG Code']])

costAnalysisTable.add_row(['Patient Count', costAnalysisTable1['Patient Count'], costAnalysisTable2['Patient Count'],
      costAnalysisTable3['Patient Count'], costAnalysisTable4['Patient Count'],
      costAnalysisTable5['Patient Count'], costAnalysisTable6['Patient Count'], costAnalysisTable7['Patient Count'],
      costAnalysisTable8['Patient Count'], costAnalysisTable9['Patient Count'], costAnalysisTable10['Patient Count'],
      costAnalysisTable11['Patient Count'], costAnalysisTable12['Patient Count'], costAnalysisTable13['Patient Count'],
      costAnalysisTable14['Patient Count']])

costAnalysisTable.add_row(['Average LOS', costAnalysisTable1['Average LOS'], costAnalysisTable2['Average LOS'],
      costAnalysisTable3['Average LOS'], costAnalysisTable4['Average LOS'],
      costAnalysisTable5['Average LOS'], costAnalysisTable6['Average LOS'], costAnalysisTable7['Average LOS'],
      costAnalysisTable8['Average LOS'], costAnalysisTable9['Average LOS'], costAnalysisTable10['Average LOS'],
      costAnalysisTable11['Average LOS'], costAnalysisTable12['Average LOS'], costAnalysisTable13['Average LOS'],
      costAnalysisTable14['Average LOS']])
costAnalysisTable.add_row(['Cost per patient in $K', costAnalysisTable1['Cost per patient in $K'], costAnalysisTable2['Cost per patient in $K'],
      costAnalysisTable3['Cost per patient in $K'], costAnalysisTable4['Cost per patient in $K'],
      costAnalysisTable5['Cost per patient in $K'], costAnalysisTable6['Cost per patient in $K'], costAnalysisTable7['Cost per patient in $K'],
      costAnalysisTable8['Cost per patient in $K'], costAnalysisTable9['Cost per patient in $K'], costAnalysisTable10['Cost per patient in $K'],
      costAnalysisTable11['Cost per patient in $K'], costAnalysisTable12['Cost per patient in $K'], costAnalysisTable13['Cost per patient in $K'],
      costAnalysisTable14['Cost per patient in $K']])
costAnalysisTable.add_row(['Room and Board', costAnalysisTable1['Room and Board'], costAnalysisTable2['Room and Board'],
      costAnalysisTable3['Room and Board'], costAnalysisTable4['Room and Board'],
      costAnalysisTable5['Room and Board'], costAnalysisTable6['Room and Board'], costAnalysisTable7['Room and Board'],
      costAnalysisTable8['Room and Board'], costAnalysisTable9['Room and Board'], costAnalysisTable10['Room and Board'],
      costAnalysisTable11['Room and Board'], costAnalysisTable12['Room and Board'], costAnalysisTable13['Room and Board'],
      costAnalysisTable14['Room and Board']])
costAnalysisTable.add_row(['Statistics', costAnalysisTable1['Statistics'], costAnalysisTable2['Statistics'],
      costAnalysisTable3['Statistics'], costAnalysisTable4['Statistics'],
      costAnalysisTable5['Statistics'], costAnalysisTable6['Statistics'], costAnalysisTable7['Statistics'],
      costAnalysisTable8['Statistics'], costAnalysisTable9['Statistics'], costAnalysisTable10['Statistics'],
      costAnalysisTable11['Statistics'], costAnalysisTable12['Statistics'], costAnalysisTable13['Statistics'],
      costAnalysisTable14['Statistics']])
costAnalysisTable.add_row(['Resp Therapy', costAnalysisTable1['Resp Therapy'], costAnalysisTable2['Resp Therapy'],
      costAnalysisTable3['Resp Therapy'], costAnalysisTable4['Resp Therapy'],
      costAnalysisTable5['Resp Therapy'], costAnalysisTable6['Resp Therapy'], costAnalysisTable7['Resp Therapy'],
      costAnalysisTable8['Resp Therapy'], costAnalysisTable9['Resp Therapy'], costAnalysisTable10['Resp Therapy'],
      costAnalysisTable11['Resp Therapy'], costAnalysisTable12['Resp Therapy'], costAnalysisTable13['Resp Therapy'],
      costAnalysisTable14['Resp Therapy']])
costAnalysisTable.add_row(['Pharmacy', costAnalysisTable1['Pharmacy'], costAnalysisTable2['Pharmacy'],
      costAnalysisTable3['Pharmacy'], costAnalysisTable4['Pharmacy'],
      costAnalysisTable5['Pharmacy'], costAnalysisTable6['Pharmacy'], costAnalysisTable7['Pharmacy'],
      costAnalysisTable8['Pharmacy'], costAnalysisTable9['Pharmacy'], costAnalysisTable10['Pharmacy'],
      costAnalysisTable11['Pharmacy'], costAnalysisTable12['Pharmacy'], costAnalysisTable13['Pharmacy'],
      costAnalysisTable14['Pharmacy']])
costAnalysisTable.add_row(['Lab', costAnalysisTable1['Lab'], costAnalysisTable2['Lab'],
      costAnalysisTable3['Lab'], costAnalysisTable4['Lab'],
      costAnalysisTable5['Lab'], costAnalysisTable6['Lab'], costAnalysisTable7['Lab'],
      costAnalysisTable8['Lab'], costAnalysisTable9['Lab'], costAnalysisTable10['Lab'],
      costAnalysisTable11['Lab'], costAnalysisTable12['Lab'], costAnalysisTable13['Lab'],
      costAnalysisTable14['Lab']])
costAnalysisTable.add_row(['OT/PT/ST', costAnalysisTable1['OT/PT/ST'], costAnalysisTable2['OT/PT/ST'],
      costAnalysisTable3['OT/PT/ST'], costAnalysisTable4['OT/PT/ST'],
      costAnalysisTable5['OT/PT/ST'], costAnalysisTable6['OT/PT/ST'], costAnalysisTable7['OT/PT/ST'],
      costAnalysisTable8['OT/PT/ST'], costAnalysisTable9['OT/PT/ST'], costAnalysisTable10['OT/PT/ST'],
      costAnalysisTable11['OT/PT/ST'], costAnalysisTable12['OT/PT/ST'], costAnalysisTable13['OT/PT/ST'],
      costAnalysisTable14['OT/PT/ST']])
costAnalysisTable.add_row(['Rehab', costAnalysisTable1['Rehab'], costAnalysisTable2['Rehab'],
      costAnalysisTable3['Rehab'], costAnalysisTable4['Rehab'],
      costAnalysisTable5['Rehab'], costAnalysisTable6['Rehab'], costAnalysisTable7['Rehab'],
      costAnalysisTable8['Rehab'], costAnalysisTable9['Rehab'], costAnalysisTable10['Rehab'],
      costAnalysisTable11['Rehab'], costAnalysisTable12['Rehab'], costAnalysisTable13['Rehab'],
      costAnalysisTable14['Rehab']])

costAnalysisTable.add_row(['Radiology', costAnalysisTable1['Radiology'], costAnalysisTable2['Radiology'],
      costAnalysisTable3['Radiology'], costAnalysisTable4['Radiology'],
      costAnalysisTable5['Radiology'], costAnalysisTable6['Radiology'], costAnalysisTable7['Radiology'],
      costAnalysisTable8['Radiology'], costAnalysisTable9['Radiology'], costAnalysisTable10['Radiology'],
      costAnalysisTable11['Radiology'], costAnalysisTable12['Radiology'], costAnalysisTable13['Radiology'],
      costAnalysisTable14['Radiology']])
costAnalysisTable.add_row(['Supply', costAnalysisTable1['Supply'], costAnalysisTable2['Supply'],
      costAnalysisTable3['Supply'], costAnalysisTable4['Supply'],
      costAnalysisTable5['Supply'], costAnalysisTable6['Supply'], costAnalysisTable7['Supply'],
      costAnalysisTable8['Supply'], costAnalysisTable9['Supply'], costAnalysisTable10['Supply'],
      costAnalysisTable11['Supply'], costAnalysisTable12['Supply'], costAnalysisTable13['Supply'],
      costAnalysisTable14['Supply']])
costAnalysisTable.add_row(['All Other', costAnalysisTable1['All Other'], costAnalysisTable2['All Other'],
      costAnalysisTable3['All Other'], costAnalysisTable4['All Other'],
      costAnalysisTable5['All Other'], costAnalysisTable6['All Other'], costAnalysisTable7['All Other'],
      costAnalysisTable8['All Other'], costAnalysisTable9['All Other'], costAnalysisTable10['All Other'],
      costAnalysisTable11['All Other'], costAnalysisTable12['All Other'], costAnalysisTable13['All Other'],
      costAnalysisTable14['All Other']])
costAnalysisTable.add_row(['OR/Anesthesia', costAnalysisTable1['OR/Anesthesia'], costAnalysisTable2['OR/Anesthesia'],
      costAnalysisTable3['OR/Anesthesia'], costAnalysisTable4['OR/Anesthesia'],
      costAnalysisTable5['OR/Anesthesia'], costAnalysisTable6['OR/Anesthesia'], costAnalysisTable7['OR/Anesthesia'],
      costAnalysisTable8['OR/Anesthesia'], costAnalysisTable9['OR/Anesthesia'], costAnalysisTable10['OR/Anesthesia'],
      costAnalysisTable11['OR/Anesthesia'], costAnalysisTable12['OR/Anesthesia'], costAnalysisTable13['OR/Anesthesia'],
      costAnalysisTable14['OR/Anesthesia']])
costAnalysisTable.add_row(['Blood', costAnalysisTable1['Blood'], costAnalysisTable2['Blood'],
      costAnalysisTable3['Blood'], costAnalysisTable4['Blood'],
      costAnalysisTable5['Blood'], costAnalysisTable6['Blood'], costAnalysisTable7['Blood'],
      costAnalysisTable8['Blood'], costAnalysisTable9['Blood'], costAnalysisTable10['Blood'],
      costAnalysisTable11['Blood'], costAnalysisTable12['Blood'], costAnalysisTable13['Blood'],
      costAnalysisTable14['Blood']])
costAnalysisTable.add_row(['Cardiac Services', costAnalysisTable1['Cardiac Services'], costAnalysisTable2['Cardiac Services'],
      costAnalysisTable3['Cardiac Services'], costAnalysisTable4['Cardiac Services'],
      costAnalysisTable5['Cardiac Services'], costAnalysisTable6['Cardiac Services'], costAnalysisTable7['Cardiac Services'],
      costAnalysisTable8['Cardiac Services'], costAnalysisTable9['Cardiac Services'], costAnalysisTable10['Cardiac Services'],
      costAnalysisTable11['Cardiac Services'], costAnalysisTable12['Cardiac Services'], costAnalysisTable13['Cardiac Services'],
      costAnalysisTable14['Cardiac Services']])

print(costAnalysisTable)