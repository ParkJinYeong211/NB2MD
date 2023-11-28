from parsedoctable import DTParser
#from parsexltable import XTParser

parsetype = input("1) Word Doc\n2) Excel Workbook\n\nEnter Selection: ")

match parsetype:
    case "1":
        my_dtp = DTParser()
        my_dtp.gen_output()
        
    case "2":
        pass