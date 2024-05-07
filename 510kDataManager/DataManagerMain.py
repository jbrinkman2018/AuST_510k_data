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

# Prompt user input and print desired graphs
repl = Repl()
repl.eval(fiveTenEntries)