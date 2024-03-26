# AuST
# 3-21-24 
# Created By : Jared Brinkman

# Foundation for a 510K Data Manager. The Data Manager actively 
# updates its database with the most current 510k Data. Based
# on user input, it allows you to see various data represented 
# by graphs, tables, etc... to make more informed decisions 
# regarding future development efforts
import sys

from UploadData.FiveTenEntry import FiveTenEntry
from UploadData.FiveTenEntries import FiveTenEntries
from Client.Repl import Repl

fiveTenEntries = FiveTenEntries()

# Load in Data
with open('pmn96cur.txt', 'r') as file:
    for line in file:
       entry= FiveTenEntry(line)
       fiveTenEntries.add(entry)

fiveTenEntries.calcProperties()

# Prompt user input
repl = Repl()
repl.eval(fiveTenEntries)
# return desired graph/charts


    


#    print(len(fiveTenEntries.entryList))

# test = ['K173442', 'electroCore, LLC', 'Mike  Romaniw', '150 Allen Road, Suite 201', '', 'Basking Ridge', 'NJ', 'US', '07920', '07920', '11/06/2017', '01/23/2018', 'SESE', 'NE', 'PKR', 'Summary', 'NE', '', 'Traditional', 'N', '', 'gammaCore-S\n']
# dataVariable = FiveTenEntry(test)
# DEVICENAME = dataVariable.DEVICENAME
# print(DEVICENAME)