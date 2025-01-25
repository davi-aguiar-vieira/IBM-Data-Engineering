# Practice Project: Historical Weather Forecast Comparison to Actuals

## Learning objectives

- Initialize your log file
- Write a Bash script to download, extract, and load raw data into a report
- Add some basic analytics to your report
- Schedule your report to update daily
- Measure and report on historical forecasting accuracy
---

## Exercise 1 - Initialize your weather report log file
### 1.1 Create a text file called `rx_poc.log`
```bash
touch rx_poc.log
```
### 1.2 Add a header to your weather report
```bash
echo -e "year\tmonth\tday\tobs_temp\tfc_temp">rx_poc.log
```
---

## Exercise 2 - Download the raw weather data
### 2.1. Create a text file called rx_poc.sh and make it an executable Bash script
```bash

touch rx_poc.sh

echo "#! /bin/bash" >> rx_poc.sh

chmod u+x rx_poc.sh

ls -l
```

### 2.2. Assign the city name to Casablanca for accessing the weather report
```bash
city=Casablanca
```

### 2.3 Obtain the weather information for Casablanca
```bash
curl -s wttr.in/$city?T --output weather_report
```
---


## Exercise 3 - Extract and load the required data
### Full script for `rx_poc.sh`
```bash
#! /bin/bash
 
#Assign city name as Casablanca
city=Casablanca

#Obtain the weather report for Casablanca
curl -s wttr.in/$city?T --output weather_report

#To extract Current Temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].*')
echo "The current Temperature of $city: $obs_temp"

# To extract the forecast tempearature for noon tomorrow
fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"

#Assign Country and City to variable TZ
TZ='Morocco/Casablanca'


# Use command substitution to store the current day, month, and year in corresponding shell variables:
day=$(TZ='Morocco/Casablanca' date -u +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)


# Log the weather
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo $record>>rx_poc.log
```
---
## Exercise 4 - Schedule your Bash script rx_poc.sh to run every day at noon local time
### 4.1 Create a cron job that runs your script
```bash
crontab -e
```
### Add `0 8 * * * /home/project/rx_poc.sh` to the end of the file
---

