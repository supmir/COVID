isLinux = True
import csv
import plotly
import plotly.offline as plo
import plotly.graph_objs as go
import requests
import time
import fileinput

def downloadData(dPath):
    print("Downloading data")
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    myfile = requests.get(url, allow_redirects=True)
    open(dPath+"data.csv", 'wb').write(myfile.content)
    url = "https://ocgptweb.azurewebsites.net/CSVDownload"
    myfile = requests.get(url, allow_redirects=True)
    open(dPath+"data2.csv", 'wb').write(myfile.content)

def loadData(dPath):
    print("Loading data")
    with open(dPath+"data.csv") as f:
        reader = csv.reader(f)
        data = list(reader)
        # data[row][collumn]
        # (lat, lon, countries, days) = (2, 3, len(data), len(data[0]))
    
    with open(dPath+"data2.csv") as f:
        reader = csv.reader(f)
        data2 = list(reader)
    return data, data2

def normaliseData(data,cleanedData):
    print("Normalising data (1/2)")
    for x in range(1, len(data)):
        row = data[x]
        currentCountry = row[1]
        length = len(cleanedData)
        inside = False
        for i in range(length):
            if cleanedData[i][0] == currentCountry:
                # print(cleanedData[i][0],currentCountry)
                for z in range(len(cleanedData[i])-1):
                    cleanedData[i][z+1] += int(row[z+4])
                inside = True
                break

        if inside == False:
            newL = [int(n) for n in row[4:]]
            cleanedData.append(newL)
            cleanedData[len(cleanedData)-1].insert(0, currentCountry)
    return cleanedData

def normaliseData2(data2,cleanedData):
    print("Normalising data (2/2)")
    for x in cleanedData:
        cur = x[0]
        strictness = "NA"
        for y in data2:
            if y[0] == cur:
                # print(y[len(y)-1])
                strictness = y[len(y)-2]
        x[0] = cur +" ("+ strictness+")"
    return cleanedData

def loadNormalised(cleanedData,dates):
    print("Loading normalised data")
    cases, zeroCases, daily = [],[],[]
    for x in range(1, len(cleanedData)):
        s = str(cleanedData[x][0])
        case = go.Scatter(
            x=dates,
            y=cleanedData[x][1:],
            mode='lines',
            name=s
        )
        firstCase = 1
        for i in range(1, len(cleanedData[x][1:])):
            if cleanedData[x][i] != 0:
                firstCase = i
                break

        zeroCase = go.Scatter(
            x=dates,
            y=cleanedData[x][firstCase:],
            mode='lines',
            name=s
        )

        changes = []
        for i in range(2, len(cleanedData[x][1:])):
            changes.append(cleanedData[x][i]-cleanedData[x][i-1])
        day = go.Scatter(
            x=dates,
            y=changes,
            mode='lines',
            name=s
        )
        cases.append(case)
        daily.append(day)
        zeroCases.append(zeroCase)
    return cases, zeroCases, daily

def autoLay(code):
    title,y,x,legend_title = "Title",dict(title="y"),dict(title="x"),"<b>Country (Strictness of Movement)</b>"
    if code == "cc":
        title,y,x = "COVID-19 Confirmed Cases",dict(title="Confirmed Cases"),dict(title="Days Since 22nd January 2020")
    if code == "pzc":
        title,y,x = "COVID-19 Confirmed Cases with Fixed Orgin",dict(title="Daily Confirmed Cases"),dict(title="Days Since Patient Zero")
    if code == "dcc":
        title,y,x = "COVID-19 Daily Confirmed Cases",dict(title="Daily Confirmed Cases"),dict(title="Days Since 22nd January 2020")
    return go.Layout(
        title=title,
        yaxis=y,
        xaxis=x,
        # legend_orientation = "h",
        legend=dict(
            # yanchor="top",
            # y=-1,
            title=legend_title
        )
    )

def fixForMobile(path):
    with fileinput.FileInput(path, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('class="plotly-graph-div" style="', 'class="plotly-graph-div" style="touch-action:manipulation;'), end='')

def func():
    if isLinux:
        # dPath , wPath = "/home/iskandar_amir/covid/","/var/www/html/"
        dPath , wPath = "/home/iskandar_amir/covid/","/home/iskandar_amir/covid2/information/templates/information/"
    else:
        dPath, wPath = "/Users/amir/Desktop/covid/","/Users/amir/Desktop/covid/"

    downloadData(dPath)
    data, data2 = loadData(dPath)

    dates = list(range(len(data[0][4:])))
    cleanedData = [["Sample", 0, 0, 0]]  # col1 is country name
    cleanedData = normaliseData(data, cleanedData)
    cleanedData = normaliseData2(data2,cleanedData)
    cases, zeroCases, daily = loadNormalised(cleanedData,dates)
    print("Creating graph layouts, inputting figures")
    caseLay,zeroLay,dayLay = autoLay("cc"),autoLay("pzc"),autoLay("dcc")

    caseFig = go.Figure(data=cases, layout=caseLay)
    zeroFig = go.Figure(data=zeroCases, layout=zeroLay)
    dayFig = go.Figure(data=daily, layout=dayLay)

    print("Plotting graphs")
    plo.plot(caseFig, filename=wPath+"cc.html", auto_open=False)
    plo.plot(zeroFig, filename=wPath+"pzc.html", auto_open=False)
    plo.plot(dayFig, filename=wPath+"dcc.html", auto_open=False)

    print("Fixing html code for mobile")
    fixForMobile(wPath+"cc.html")
    fixForMobile(wPath+"pzc.html")
    fixForMobile(wPath+"dcc.html")

while True:
    print("Starting update process at ", time.ctime(time.time()))
    func()
    print("Updated at",time.ctime(time.time()))
    interval = 4
    for x in range(int(24/interval)):
        time.sleep(60*60*interval)
        print("The time is", time.ctime(time.time()))

    

