import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
from bs4 import BeautifulSoup

# ----------------------------------------------------------------------

"""
    Get allergen info from website using web scraping
    Created by Diana Beltran
    Sat May  2 14:42:55 2020
"""
# Allergen info
def allergenCount(zipcode):
    httpString ='https://weather.com/forecast/allergy/l/' + zipcode
    print(httpString)
    page = requests.get(httpString)
    page.raise_for_status()
    soup = BeautifulSoup(page.content, 'html.parser')

    pollen = soup.find(id="WxuPollenBreakdown-main-c1dadebb-ed45-4199-a7ab-4a3ca6163a2c")
    firstClass = pollen.find(class_ = "_-_-components-src-organism-PollenBreakdown-PollenBreakdown--body--OrmOR")
##################
    for i in firstClass:
        if None in (i):
            continue
        print(i.get_text(separator=' ' ))
# ----------------------------------------------------------------------

"""
    Get information of PM2.5 and Ozone from csv files and API and plot the PM2.5 trend
    Created by Shuwei He
    Mon May 4 2020
"""
# Forecast trend of PM2.5 in 2020
# Data Source: https://www.epa.gov/outdoor-air-quality-data/download-daily-data
def Statesdata():
    AK = pd.read_csv('PM2.5_data_2020/AK.csv')
    AL = pd.read_csv('PM2.5_data_2020/AL.csv')
    AR = pd.read_csv('PM2.5_data_2020/AR.csv')
    AZ = pd.read_csv('PM2.5_data_2020/AZ.csv')
    CA = pd.read_csv('PM2.5_data_2020/CA.csv')
    CO = pd.read_csv('PM2.5_data_2020/CO.csv')
    CT = pd.read_csv('PM2.5_data_2020/CT.csv')
    DC = pd.read_csv('PM2.5_data_2020/DC.csv')
    DE = pd.read_csv('PM2.5_data_2020/DE.csv')
    FL = pd.read_csv('PM2.5_data_2020/FL.csv')
    GA = pd.read_csv('PM2.5_data_2020/GA.csv')
    HI = pd.read_csv('PM2.5_data_2020/HI.csv')
    IA = pd.read_csv('PM2.5_data_2020/IA.csv')
    ID = pd.read_csv('PM2.5_data_2020/ID.csv')
    IL = pd.read_csv('PM2.5_data_2020/IL.csv')
    IN = pd.read_csv('PM2.5_data_2020/IN.csv')
    KS = pd.read_csv('PM2.5_data_2020/KS.csv')
    KY = pd.read_csv('PM2.5_data_2020/KY.csv')
    LA = pd.read_csv('PM2.5_data_2020/LA.csv')
    MA = pd.read_csv('PM2.5_data_2020/MA.csv')
    MD = pd.read_csv('PM2.5_data_2020/MD.csv')
    ME = pd.read_csv('PM2.5_data_2020/ME.csv')
    MI = pd.read_csv('PM2.5_data_2020/MI.csv')
    MN = pd.read_csv('PM2.5_data_2020/MN.csv')
    MO = pd.read_csv('PM2.5_data_2020/MO.csv')
    MS = pd.read_csv('PM2.5_data_2020/MS.csv')
    MT = pd.read_csv('PM2.5_data_2020/MT.csv')
    NC = pd.read_csv('PM2.5_data_2020/NC.csv')
    ND = pd.read_csv('PM2.5_data_2020/ND.csv')
    NE = pd.read_csv('PM2.5_data_2020/NE.csv')
    NH = pd.read_csv('PM2.5_data_2020/NH.csv')
    NJ = pd.read_csv('PM2.5_data_2020/NJ.csv')
    NM = pd.read_csv('PM2.5_data_2020/NM.csv')
    NV = pd.read_csv('PM2.5_data_2020/NV.csv')
    NY = pd.read_csv('PM2.5_data_2020/NY.csv')
    OH = pd.read_csv('PM2.5_data_2020/OH.csv')
    OK = pd.read_csv('PM2.5_data_2020/OK.csv')
    OR = pd.read_csv('PM2.5_data_2020/OR.csv')
    PA = pd.read_csv('PM2.5_data_2020/PA.csv')
    RI = pd.read_csv('PM2.5_data_2020/RI.csv')
    SC = pd.read_csv('PM2.5_data_2020/SC.csv')
    SD = pd.read_csv('PM2.5_data_2020/SD.csv')
    TN = pd.read_csv('PM2.5_data_2020/TN.csv')
    TX = pd.read_csv('PM2.5_data_2020/TX.csv')
    UT = pd.read_csv('PM2.5_data_2020/UT.csv')
    VA = pd.read_csv('PM2.5_data_2020/VA.csv')
    VT = pd.read_csv('PM2.5_data_2020/VT.csv')
    WA = pd.read_csv('PM2.5_data_2020/WA.csv')
    WI = pd.read_csv('PM2.5_data_2020/WI.csv')
    WV = pd.read_csv('PM2.5_data_2020/WV.csv')
    WY = pd.read_csv('PM2.5_data_2020/WY.csv')

    States = [AK, AL, AR, AZ, CA, CO, CT, DC, DE, FL, GA, HI, IA,
              ID, IL, IN, KS, KY, LA, MA, MD, ME, MI, MN, MO, MS,
              MT, NC, ND, NE, NH, NJ, NM, NV, NY, OH, OK, OR, PA,
              RI, SC, SD, TN, TX, UT, VA, VT, WA, WI, WV, WY]

    States_data = pd.concat(States, ignore_index=True)
    return States_data
# Guide for O3
def guideforO3(quality):
    if quality == 'Good':
        print('Air Quality Guide for Ozone: It’s a great day to be active outside.')
    elif quality == 'Moderate':
        print('Air Quality Guide for Ozone: Some people who may be unusually sensitive to ozone should be concerned.')
        print('Unusually sensitive people: Consider reducing prolonged or heavy outdoor exertion. Watch for symptoms such as coughing or shortness of breath. These are signs to take it easier.')
        print('Everyone else: It’s a good day to be active outside.')
    elif quality == 'Unhealthy for Sensitive Groups':
        print('Air Quality Guide for Ozone: Sensitive groups include people with lung disease such as asthma, older adults, children and teenagers, and people who are active outdoors should be concerned.')
        print('Sensitive groups: Reduce prolonged or heavy outdoor exertion. Take more breaks, do less intense activities. Watch for symptoms such as coughing or shortness of breath. Schedule outdoor activities in the morning when ozone is lower.')
        print('People with asthma should follow their asthma action plans and keep quick- relief medicine handy.')
    elif quality == 'Unhealthy':
        print('Air Quality Guide for Ozone: Everyone should be concerned.')
        print('Sensitive groups: Avoid prolonged or heavy outdoor exertion. Schedule outdoor activities in the morning when ozone is lower. Consider moving activities indoors. People with asthma, keep quick-relief medicine handy.')
        print('Everyone else: Reduce prolonged or heavy outdoor exertion. Take more breaks, do less intense activities. Schedule outdoor activities in the morning when ozone is lower.')
    elif quality == 'Very Unhealthy':
        print('Air Quality Guide for Ozone: Everyone should be concerned.')
        print('Sensitive groups: Avoid all physical activity outdoors. Move activities indoors or reschedule to a time when air quality is better. People with asthma, keep quick-relief medicine handy.')
        print('Everyone else: Avoid prolonged or heavy outdoor exertion. Schedule outdoor activities in the morning when ozone is lower. Consider moving activities indoors.')
    elif quality == 'Hazardous':
        print('Air Quality Guide for Ozone: Everyone should be concerned.')
        print('Everyone: Avoid all physical activity outdoors.')
# Guide for PM2.5
def guideforPM25(quality):
    if quality == 'Good':
        print('Air Quality Guide for Particle Pollution: It’s a great day to be active outside.')
    elif quality == 'Moderate':
        print(
            'Air Quality Guide for Particle Pollution: Some people who may be unusually sensitive to particle pollution should be concerned.')
        print(
            'Unusually sensitive people: Consider reducing prolonged or heavy exertion. Watch for symptoms such as coughing or shortness of breath. These are signs to take it easier.')
        print('Everyone else: It’s a good day to be active outside.')
    elif quality == 'Unhealthy for Sensitive Groups':
        print(
            'Air Quality Guide for Particle Pollution: Sensitive groups include people with heart or lung disease, older adults,children and teenagers should be concerned.')
        print(
            'Sensitive groups: Reduce prolonged or heavy exertion. It’s OK to be active outside, but take more breaks and do less intense activities. Watch for symptoms such as coughing or shortness of breath.')
        print('People with asthma should follow their asthma action plans and keep quick relief medicine handy.')
        print(
            'If you have heart disease: Symptoms such as palpitations, shortness of breath, or unusual fatigue may indicate a serious problem. If you have any of these, contact your heath care provider.')
    elif quality == 'Unhealthy':
        print('Air Quality Guide for Particle Pollution: Everyone should be concerned.')
        print(
            'Sensitive groups: Avoid prolonged or heavy exertion. Consider moving activities indoors or rescheduling.')
        print('Everyone else: Reduce prolonged or heavy exertion. Take more breaks during outdoor activities.')
    elif quality == 'Very Unhealthy':
        print('Air Quality Guide for Particle Pollution: Everyone should be concerned.')
        print(
            'Sensitive groups: Avoid all physical activity outdoors. Move activities indoors or reschedule to a time when air quality is better.')
        print(
            'Everyone else: Avoid prolonged or heavy exertion. Consider moving activities indoors or rescheduling to a time when air quality is better.')
    elif quality == 'Hazardous':
        print('Air Quality Guide for Particle Pollution: Everyone should be concerned.')
        print('Everyone: Avoid all physical activity outdoors.')
        print(
            'Sensitive groups: Remain indoors and keep activity levels low. Follow tips for keeping particle levels low indoors. ')
# current observation
def GetPM25andO3(zipcode):
    headers = {'Content-Type': 'application/json'}
    url = 'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={}&distance=25&API_KEY=F4A0D299-0B24-4798-AC36-E311E5ADFFB8'.format(
        zipcode)
    error = 0
    try:
        # Notice that there would be something wrong about APIs because the data source website
        # ( https://www.airnow.gov/) has some technical issues. To confirm that, you can go to this website to see that
        # whether this is an alert on website The most recent data outage happened on May 7. So, if there is till an
        # issue when you are running, it would take one or two minutes to jump into the exception and continue the
        # menu.
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = json.loads(response.content.decode('utf-8'))
            if len(data) != 0:
                O3 = data[0]
                PM25 = data[1]
                print('----------------------------------------------------------------------')
                print('Get PM2.5 and Ozone info:')
                print('Date: ', O3['DateObserved'])
                if O3['HourObserved'] > 12:
                    time = O3['HourObserved'] - 12
                    print('Time: {}:00 PM {}'.format(time, O3['LocalTimeZone']))
                else:
                    time = O3['HourObserved']
                    print('Time: {}:00 AM {}'.format(time, O3['LocalTimeZone']))
                print('Location: {}, {}'.format(O3['ReportingArea'], O3['StateCode']))
                print('Latitude and Longitude: {}, {}'.format(O3['Latitude'], O3['Longitude']))
                print('----------------------------------------------------------------------')
                print('AQI of {}:'.format(O3['ParameterName']), O3['AQI'])
                print('Quality:', O3['Category']['Name'])
                guideforO3(O3['Category']['Name'])
                print('----------------------------------------------------------------------')
                print('AQI of {}:'.format(PM25['ParameterName']), PM25['AQI'])
                print('Quality:', PM25['Category']['Name'])
                # Air Quality Guide for Particle Pollution
                guideforPM25(PM25['Category']['Name'])
                print('----------------------------------------------------------------------')
                print('')
            else:
                print('')
                print('----------------------------------------------------------------------')
                print('There is no data about this area. Please try another zip code.')
                print('----------------------------------------------------------------------')
                print('')

    except requests.exceptions.ConnectionError:
        error = 1
        print('')
        print('----------------------------------------------------------------------')
        print('AirNow is experiencing an outage in its national data center and cannot report data at this time. We '
              'are working to resolve the issue. We are sorry for the inconvenience.')
        print('----------------------------------------------------------------------')
        print('')


# ----------------------------------------------------------------------

"""
    Get water pollution info from website using API
    Created by Eric Rasmussen
    Tue May 5 2020
"""
# Get the water info
def water(State, county):
    operator = '=/'
    table_name_samples = 'LCR_SAMPLE_RESULT/'
    where_table = 'GEOGRAPHIC_AREA/'
    all_table = 'WATER_SYSTEM/'
    state_col = 'PRIMACY_AGENCY_CODE/'
    county_col = '/COUNTY_SERVED/'
    ID = 'PWSID/'
    code_type = '/JSON'
    date_table = 'LCR_SAMPLE/'
    headers = {'Content-Type': 'application/json'}
    #url based on information inputted by user
    url = 'http://enviro.epa.gov/enviro/efservice/' + where_table + state_col + State + county_col + county + code_type
    response = requests.get(url, headers=headers)
    # query geographical table to find ID numbers for area of interest
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        Data_frame_geographic = pd.json_normalize(data)
    # ----------------------------------------------------------------------
    # querying sample data based on PWSID from Geographic data

    pwsid_list = []
    #make list of all IDs from area
    for line in Data_frame_geographic['PWSID']:
        pwsid = line
        pwsid_list.append(pwsid)

    
    sample_result_list = []
    units_list = []
    PWSID_list_post = []
    headers = {'Content-Type': 'application/json'}
    for value in pwsid_list:
        url_sample = 'http://data.epa.gov/efservice/' + table_name_samples + ID + operator + value + code_type
        response2 = requests.get(url_sample, headers=headers)

        if response2.status_code == 200:
            sample_data_prelim = json.loads(response2.content.decode('utf-8'))
            #if there is a sample for the id listed, create a datatable for that id and sample
            if len(sample_data_prelim) > 0:
                data_frame_sample = pd.json_normalize(sample_data_prelim)
                #append the sample results and correlated ID to seperate lists 
                for line in data_frame_sample['SAMPLE_MEASURE']:
                    sample = float(line)
                    sample_result_list.append(sample)
                    PWSID_list_post.append(value)

    

    # compiling sample and respective ID into a dataframe
    all_data_compiled = pd.DataFrame(PWSID_list_post, columns=['PWSID'])
    all_data_compiled['Sample results'] = sample_result_list
    sum_sample = sum(sample_result_list)
    avg_sample = sum_sample / len(sample_result_list)
    #return dataframe and the avg concentration of copper and lead of area back to main function
    return (all_data_compiled, avg_sample)

# ----------------------------------------------------------------------


def menu():
    print('This is the menu:\n'
          '1. Display the allergen info.\n'
          '2. Display the current observation of PM2.5 and Ozone.\n'
          '3. Display the forecast trend of PM2.5 in 2020.\n'
          '4. Display the average amount of copper/lead in water. \n'
          '(NOTICE: it would take a couple of minutes to run choice 4 because of large datasets and API requests.)\n'
          '0. Quit this menu and start searching information of other locations.')
    n = input('Please enter a numeric choice: ')
    return int(n)


def main():
    # Get useful data from datasets
    States_data = Statesdata()
    county_data = States_data[['Date', 'DAILY_AQI_VALUE', 'COUNTY']]
    # Let users input data
    while True:
        # Users input
        print('If you want to end this app, please enter -1')
        print('You need to enter a county name, a state abbreviation and a zip code of the place of interest.') # These things should be coresponding with each other
        print('')
        county = input('Please enter the name of county starting with uppercase: (-1 for quit) ')

        if county != '-1':
            # input
            State_input = input('Enter a state abbreviation: ').upper()
            zipcode = input('Please enter the zip code: ')
            print('----------------------------------------------------------------------')
            n = menu()
            while True:
                if n == 0:
                    print('Quit the menu')
                    print('----------------------------------------------------------------------')
                    print('')
                    break
                elif n == 1:
                    # Get allergen info
                    print('')
                    print('----------------------------------------------------------------------')
                    print('Get allergen info in {} {} {}:'.format(county,State_input,zipcode))
                    allergenCount(zipcode)
                    print('----------------------------------------------------------------------')
                    print('')
                    n = menu()
                elif n == 2:
                    # Display the current PM2.5 and O3 data
                    GetPM25andO3(zipcode)
                    n = menu()
                elif n == 3:
                    # Plot the forecast trend of PM2.5 in 2020
                    aqi = county_data['DAILY_AQI_VALUE'][county_data['COUNTY'] == county]
                    if len(aqi) != 0:
                        print('')
                        print('----------------------------------------------------------------------')
                        print('Get The forecast trend of PM2.5 AQI value in {} {} {} from Jan1 2020'.format(county, State_input, zipcode))
                        print('----------------------------------------------------------------------')
                        print('')
                        plt.title('The forecast trend of PM2.5 AQI value in %s from Jan1 2020' % (county))
                        plt.plot(range(len(aqi)), aqi)
                        plt.xlabel('Year: 2020')
                        plt.ylabel('DAILY AQI VALUE')
                        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                        tick = []
                        for i in range(len(months)):
                            tick.append(sum(months[:i]))
                        plt.xticks(tick, Month)
                        plt.show()
                        print('-----------------------------------------------------------------------------------')
                    else:
                        print('')
                        print('-----------------------------------------------------------------------------------')
                        print('This county is not included in the dataset. Please try another county of interest.')
                        print('-----------------------------------------------------------------------------------')
                        print('')
                    n = menu()
                elif n == 4:
                    # water info
                    all_data, avg_sample = water(State_input, county)
                    print('')
                    print('----------------------------------------------------------------------')
                    print(all_data)
                    print('----------------------------------------------------------------------')
                    print(
                        'The average concentration of copper/lead in water in ' + county + ' ' + State_input + ' is %6.3f mg/L' % (
                            avg_sample))
                    if float(avg_sample) > 0.015:
                        print('You may want to filter your water prior to drinking.')
                    else:
                        print('The water should be safe to drink!')
                    print('----------------------------------------------------------------------')
                    print('')
                    n = menu()
        else:
            break

if __name__ == '__main__':
    main()
