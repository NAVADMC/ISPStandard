import sys, os, string, random

fclassl = ['cow_calf_small','feedlot_small','goats','sheep','stockers','swine_enterprise_small','swine_grower_finisher_small','swine_nursery_small','swine_other_small']


ifile = open("C:\\FMD_Modelling\\USA\data\\us_farm_file4.txt","r") #input file
ofile = open("C:\\FMD_Modelling\\USA\data\\us_farm_file5.txt","w") #output file
for line in ifile: #each record
    line = line.strip()
    id,fclass,cattle,goats,sheep,swine,coords = line.split()
    if fclass in fclassl:
        rand = random.random()
        if rand <= 0.00195913:
            fclass = "dealer"
            ofile.write(id+" "+fclass+" "+cattle+" "+goats+" "+sheep+" "+swine+" "+coords+"\n")
        else:
            ofile.write(line+"\n")
    else:
        ofile.write(line+"\n")
ifile.close()
ofile.close()

    