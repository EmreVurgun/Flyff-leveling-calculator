import re

exp_req = [0,14,20,36,90,152,250,352,480,591,743,973,1290,1632,1928,2340,3480,4125,4995,5880,
           7840,6875,8243,10380,13052,16450,20700,26143,31950,38640,57035,65000,69125,72000,87239,105863,128694,182307,221450,269042,
           390368,438550,458137,468943,560177,669320,799963,1115396,1331100,1590273,2306878,2594255,2711490,2777349,3318059,3963400,4735913,6600425,7886110,9421875,
           13547310,15099446,15644776,15885934,18817757,22280630,26392968,36465972,43184958,51141217,73556918,81991117,84966758,86252845,102171368,120995493,143307208,198000645,234477760,277716683,
           381795797,406848219,403044458,391191019,442876559,501408635,567694433,749813704,849001357,961154774,
           1309582668,1382799035,1357505030,1305632790,1464862605,1628695740,1810772333,2348583653,2611145432,2903009208,
           3919352097,4063358600,3916810682,4314535354,4752892146,5235785988,5767741845,6353744416,6999284849,7710412189,
           8493790068,9356759139,10307405867,11354638303,12508269555,13779109742,15179067292,16721260528,18420140598,20291626883,
           22353256174,24624347002,27126180657,29882200612,32918232194,36262724585,39947017402,44005634371,48476606823,53401830076,
           58827456011,64804325542,71388445017,78641511031,86631488552,95433247789,105129265764,115810399166,127576735721,140538532070,
           154817246928,170546679216,187874221825,206962242762,227989606627,251153350660,276670531087,304780257046,335745931162,369857717768,
           554786576652,832179864978,1248269797467,1872404696201,2808607044301,3089467748731,3182151781193,3277616334629,3375944824668,3477223169408,
           3581539864490,3688986060425,3799655642237,3913645311505,4031054670850,4151986310975,5812780835365,7556615085975,9823599611767,12770679495297]

exp_req_universe = exp_req[:140]

exp_rew_normal = [0,2,4,5,9,9,11,12,13,14,15,
                  18,20,22,25,29,32,36,41,46,53,
                  61,69,79,90,103,119,136,156,177,201,
                  229,261,297,338,384,437,497,567,646,723,
                  809,905,1013,1134,1269,1421,1592,1782,2501,2501,
                  2501,2801,3136,3512,3934,4406,4934,5525,6188,6867,
                  11570,12841,14254,15821,21074,23391,25964,28819,31988,35506,
                  35506,36786,40832,45323,50308,55841,61983,68801,76369,84764,
                  94093,104443,115931,128683,141551,155706,155706,188403,207243,225894,
                  246224,268384,292538,318866,347563,375368,405397,437828,472854,496756,
                  579415,625767,592105,690630,756880,686512,800746,864805,774266,903102,
                  975349,975349,1100000,1250000,1250000,1356336,1412850,1471719,1533041,1596917,
                  1663456,1663456,1663456,1559786,1624778,1692477,1762997,1836455,1912974,1912974,
                  1912974,1912974,1949733,2030972,2115596,2302568,2310568,2310568,2310568,2310568,
                  2310568,2310568,2310568,2310568,10567199,10567199,10567199,10567199,10567199,10567199,
                  10567199,10567199,16143996,16143996,18861914,18861914,18861914,18861914,18861914,31568337,
                  31568337,31568337,31568337,31568337,31568337,31568337,31568337,31568337,31568337]

exp_rew_prem = [0,2,4,5,9,9,11,12,13,14,15,
                18,20,22,25,29,32,36,41,46,53,
                61,69,79,90,103,119,136,156,177,201,
                229,261,297,338,384,437,497,567,646,723,
                809,905,1013,1134,1269,1421,1592,1782,2501,2501,
                2501,2801,3136,3512,3934,4406,4934,5525,6188,6867,
                7622,8460,9391,10424,11570,12841,14254,29081,29081,29081,
                29081,29081,29081,54388,54388,54388,54388,54388,54388,101723,
                101723,101723,101723,101723,101723,186847,186847,186847,186847,186847,
                186847,322061,322061,322061,322061,322061,322061,525394,525394,525394,
                525394,525394,525394,828756,828756,828756,828756,828756,828756,1787500,
                1787500,1787500,1966250,1966250,2162875,2162875,2379162,2379162,2617079,2617079,
                2878787,2878787,2878787,3324998,3324998,3324998,3324998,3324998,4626735,4626735,
                4626735,4626735,4626735,5598350,5598350,5598350,5598350,5598350,6774003,6774003,
                6774003,6774003,6774003,8196544,8196544,8196544,8196544,8196544,8196544,9917819,
                9917819,9917819,16143996,16143996,18861914,18861914,18861914,18861914,18861914,31568337,
                31568337,31568337,31568337,31568337,31568337,31568337,31568337,31568337,31568337]

exp_rew_universe = [0,2,4,5,9,9,11,12,13,14,15,
                    18,20,22,25,29,32,36,41,46,53,
                    61,69,79,90,103,119,136,156,177,201,
                    229,261,297,338,384,437,497,567,646,723,
                    809,905,1013,1134,1269,1421,1592,1782,2501,2501,
                    2501,2801,3136,3512,3934,4406,4934,5525,6188,6867,
                    11570,12841,14254,15821,21074,23391,25964,28819,31988,35506,
                    35506,36786,40832,45323,50308,55841,61983,68801,76369,84764,
                    94093,104443,115931,128683,141551,155706,155706,188403,207243,225894,
                    246224,268384,292538,318866,347563,375368,405397,437828,472854,534050,
                    576774,576774,594939,594939,594939,638827,638827,638827,780247,838766,
                    907038,1492224,1584878,1677532,1862841,1955496,2048150,2140805,2140805,2326113,
                    2423644,2516299,2516299,2979571,3072225,3164880,3164880,3164880,3164880,3910992,
                    4096301,4471795,4471795,4471795,4471795,4471795,4471795,4471795,4471795]

mob_normal = []
mob_prem = []
mob_universe = []

### adding mob amounts
for i in range(len(exp_req)-1):
  mob_normal.append(int(exp_req[i+1])/exp_rew_normal[i+1])

for i in range(len(exp_req)-1):
  mob_prem.append(int(exp_req[i+1])/exp_rew_prem[i+1])

for i in range(len(exp_req_universe)-1):
  mob_universe.append(int(exp_req_universe[i+1])/exp_rew_universe[i+1])

def calculatespesifictime():
  aoe = input("Do you aoe? (Enter Y for yes N for no)")
  if aoe == "Y":
    aoe_amount = int(input("How many mobs do you aoe?"))
    aoe_time = int(input("How many seconds does it take you to aoe?"))
    time_per_mob = aoe_time/aoe_amount
  if aoe == "N":
    time_per_mob = int(input("How many second does it take you to down 1 mob of your level?"))
  starting_level = input("What level are you at? (For example enter like 15, 70M or 130H)")
  end_level = input("What level do you want to get to? (Add H or M for hero and master. example: 130H)")
  version = input("What version of flyff do you play? (Enter P for flyff pc, U for flyff universe.)")
  prem = input("Do you have access to premium areas like azria,traseia? Enter Y for yes N for no (Coral island not necessary.)")
  amp = input("What is your exp amplification% ? (for example enter 250 if you level with 5 es amps active or 0 if you have no amps)")
  mobs = 0


 ### calculation
  if version =="P":
    if prem == "Y":
      mobs = sum(mob_prem[int(re.sub("M|H|\s", "", starting_level))-1:int(re.sub("M|H|\s", "",end_level))])
      if not("M" in starting_level) and not("H" in starting_level) and "M" in end_level:
        mobs += sum(mob_prem[59:int(re.sub("M|H|\s", "",end_level))]*2+sum(mob_prem[int(re.sub("M|H|\s", "",end_level))-1:120]))
      elif not("M" in starting_level) and not("H" in starting_level) and "H" in end_level:
        mobs += sum(mob_prem[59:120])*2
      elif "M" in starting_level and "M" in end_level:
        mobs += mobs
      elif "M" in starting_level and "H" in end_level:
        mobs += sum(mob_prem[int(re.sub("M|H|\s", "", starting_level))-1:120])
    if prem == "N":
      mobs = sum(mob_normal[int(re.sub("M|H|\s", "", starting_level))-1:int(re.sub("M|H|\s", "",end_level))])
      if not("M" in starting_level) and not("H" in starting_level) and "M" in end_level:
        mobs += sum(mob_normal[59:int(re.sub("M|H|\s", "",end_level))]*2+sum(mob_normal[int(re.sub("M|H|\s", "",end_level))-1:120]))
      elif not("M" in starting_level) and not("H" in starting_level) and "H" in end_level:
        mobs += sum(mob_normal[59:120])*2
      elif "M" in starting_level and "M" in end_level:
        mobs += mobs
      elif "M" in starting_level and "H" in end_level:
        mobs += sum(mob_normal[int(re.sub("M|H|\s", "", starting_level))-1:120])
  if version == "U":
    mobs = sum(mob_universe[int(re.sub("M|H|\s", "", starting_level))-1:int(re.sub("M|H|\s", "",end_level))])
    if not("M" in starting_level) and not("H" in starting_level) and "M" in end_level:
      mobs += sum(mob_universe[59:int(re.sub("M|H|\s", "",end_level))]*2+sum(mob_universe[int(re.sub("M|H|\s", "",end_level))-1:120]))
    elif not("M" in starting_level) and not("H" in starting_level) and "H" in end_level:
      mobs += sum(mob_universe[59:120])*2
    elif "M" in starting_level and "M" in end_level:
      mobs += mobs
    elif "M" in starting_level and "H" in end_level:
      mobs += sum(mob_universe[int(re.sub("M|H|\s", "", starting_level))-1:120])
  time = round((mobs*time_per_mob/((int(amp)+100)/100)/3600),2)
  ### results
  print("------------------------------------------")
  print(f"Total time to your goal is: {time} hours.")
  print("")

def calculate():
  try:
    calculatespesifictime()
  except Exception as e:
    print("")
    print("You entered inputs incorrectly (Be careful to capitalize Letters)")
    print("Try again")
    print("")
    calculate()

loop = True  
while loop == True:
  calculate()
  condition = input("Do you wish to calculate again? (Enter Y to continue N to exit.)")
  if condition == "N":
    loop = False