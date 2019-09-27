import requests
import urllib3
from string import digits
import csv
import json
import datetime

stock_name_array = [None]
stock_attribute1_array = [None]
stock_attribute2_array= [None]
date_array = [None]
close_price=0

tend_array=[None]
twentyd_array=[None]
thirtyd_array=[None]
fortyd_array=[None]
fiftyd_array=[None]
with open('stocks_dates.csv', 'rt') as csv_file:
    spamreader= csv.reader(csv_file, delimiter=',')
    for row in spamreader:
        str_date_start_for_gain_losers=row[1]
        new_date = str_date_start_for_gain_losers[0:4] + "-" + str_date_start_for_gain_losers[4:6] + "-" + str_date_start_for_gain_losers[6:8]

        response = requests.get("https://api.iextrading.com/1.0/stock/" + row[0] + "/chart/2y")

        json_response = response.json()

        stock_name = row[0]
        print (stock_name)

        #if (stock_name=='MNLO'):
         #   print (json_response)
          #  print (response_date)
           # print (new_date)
        stock_name_array.append(stock_name)

        date=row[1]
        date_array.append(date)
        f=0
        x=0

        while (x<1):
            response_date = json_response[f]['date']
            if response_date == new_date:
#                changePercent = json_response[f]['changePercent']
#                stock_attribute1_array.append(changePercent)

                #declaring places
                ten_days_place=f-10
                twenty_days_place=f-20
                thirty_days_place=f-30
                forty_days_place=f-40
                fifty_days_place=f-50

                if (f + len(json_response)) > 10:
                    ten_days_value = json_response[ten_days_place]['close']
                    tend_array.append(ten_days_value)
                else:
                    ten_days_value = 'N/A'
                    tend_array.append(ten_days_value)
                if (f + len(json_response)) > 20:
                    twenty_days_value=json_response[twenty_days_place]['close']
                    twentyd_array.append(twenty_days_value)
                else:
                    twenty_days_value = 'N/A'
                    twentyd_array.append(twenty_days_value)
                if (f + len(json_response)) > 30:
                    thirty_days_value = json_response[thirty_days_place]['close']
                    thirtyd_array.append(thirty_days_value)
                else:
                    thirty_days_value = 'N/A'
                    thirtyd_array.append(thirty_days_value)

                if (f+len(json_response))>40:
                    forty_days_value = json_response[forty_days_place]['close']
                    fortyd_array.append(forty_days_value)
                else:
                    forty_days_value= 'N/A'
                    fortyd_array.append(forty_days_value)
                if (f+len(json_response))>50:
                    fifty_days_value = json_response[fifty_days_place]['close']
                    fiftyd_array.append(fifty_days_value)
                else:
                    fifty_days_value= 'N/A'
                    fiftyd_array.append(fifty_days_value)





                x+=1
            f= f+1




  #  with open('index.csv', 'a') as csv_file:

 #       writer = csv.writer(csv_file)
csv_file.close

with open('all_attributes.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    z=1
    while (z < len(stock_name_array)):
        print(stock_name_array[z])
        writer.writerow([stock_name_array[z], date_array[z],tend_array[z],twentyd_array[z],thirtyd_array[z], fortyd_array[z], fiftyd_array[z]])
        z += 1



        #writer.writerow([stock_name[0], str_date_start_for_gain_losers, close_price_array])


