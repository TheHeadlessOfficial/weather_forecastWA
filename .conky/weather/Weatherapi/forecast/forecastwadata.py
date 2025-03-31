# Lock file to tell conky that the script is running
lock_file = "/tmp/script_waforecast.lock"
try:
    # Check for file lock
    open(lock_file, 'w').close()
    import os
    import time
    import requests
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude, city and APPID
    mylat = 
    mylon = 
    mycity = '' # type between apostrophes
    myAPPID = '' # type between apostrophes
    ################################ pattern url forecast
    #                  my API url forecast
    url = 'https://api.weatherapi.com/v1/forecast.json?key=' + myAPPID + '&q=' + mycity + '&days=10&aqi=yes&alerts=yes'
    res = requests.get(url).json()
    data = res
    ################################ set variables
    forecastday = 3
    grouph = 24 # 24 hours
    temporary = ''
    vtext = 'n/a'
    ################################ set default conky folder (change it if needed)
    home = '/home/'
    conky = '/.conky/'
    ################################ set the paths for the API files
    ptemp = conky + '/weather/Weatherapi/forecast/'
    ################################ set paths
    ptemp2 = conky + "/weather/Weatherapi/"
    ptemp3 = " $HOME" + conky + "/weather/Weatherapi/"
    ptemp4 = " $HOME" + conky + "/weather/Weatherapi/forecast/"
    #                   set the paths for the DAILY and HOURLY UV INDEX
    puvid = home + homename + ptemp + 'forecastdaylyuv.txt'
    puvih = home + homename + ptemp + 'forecasthourlyyuv.txt'
    #                   set the paths for the HOURLY DEW POINT
    pdewp = home + homename + ptemp + 'forecasthourlydewpt.txt'
    ################################################################ FUNCTIONS SECTION
    ################################ calculate forecast DAILY and HOURLY UV index color and write it
    def uvindexDH(path, uvf):
        #fo = open(path, 'w')
        for i in range(0, forecastday):
            value = uvf
            if (value >=0 and value < 3):
                color = 6
            elif (value >=3 and value < 6):
                color = 9
            elif (value >=6 and value < 8):
                color = 3
            elif (value >=8 and value < 11):
                color = 4
            elif (value >= 11):
                color = 0
            else:
                color = 2
            return(value, color)
    ################################ calculate HOURLY forecast dew point color and write it
        color = 'white'
    def dewpointH(path, dpf):    
        #fof = open(path, 'w')
        for i in range(0, grouph):
            value = dpf
            if (value < 19):
                color = 6
            elif (value >=19 and value < 22):
                color = 9
            elif (value >=22):
                color = 4
            else:
                color = 'white'
            return(value, color)
    ################################ create the path for weatherapi logo
    #                   set the path for the Weatherapi logo
    pwblogo = home + homename + ptemp + 'walogo.txt'
    pi = '${image ' + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherapi/walogo2'
    est = '.png -p '
    x = 265
    virg = ','
    y = 0
    pf = ' -s 15x15}'
    fo = open(pwblogo, 'w')
    tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
    fo.write('{}\n'.format(tot))
    fo.close()
    ################################ insert angle of your North in 'myd'
    myd = 0
    tdeg = 0
    ################################ get data for ERROR section
    #                   set the paths for the ERROR
    perr = home + homename + ptemp + '-error.txt'
    #                    get data for ERROR section
    responseHTTP = requests.get(url)
    # get status code
    status_code = responseHTTP.status_code
    #                    write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(status_code))
    fo.close()
    ################################ START
    if status_code == 200:
        ################################ get data for GENERAL section
        cityname = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        lat = data['location']['lat']
        lon = data['location']['lon']
        timezone = data['location']['tz_id']
        timezone = timezone + '        '
        et = data['location']['localtime_epoch']
        lt = time.strftime("%d-%B-%Y", time.localtime(et))
        ################################ write raw data for GENERAL section
        #                   set the paths for the GENERAL section
        pgen = home + homename + ptemp + '-general.txt'
        fo = open(pgen, 'w')
        fo.write('cityname: {}\n'.format(cityname))
        fo.write('region: {}\n'.format(region))
        fo.write('country: {}\n'.format(country))
        fo.write('lat: {}\n'.format(lat))
        fo.write('lon: {}\n'.format(lon))
        fo.write('timezone: {}\n'.format(timezone))
        fo.write('epochtime: {}\n'.format(et))
        fo.write('localtime: {}\n'.format(lt))
        ################################ write GENERAL clean data on a file
        #                   set the path for general today clean data
        pgen = home + homename + ptemp + 'general.txt'
        fo = open(pgen, 'w')
        fo.write('{}\n'.format(cityname))
        fo.write('{}\n'.format(region))
        fo.write('{}\n'.format(country))
        fo.write('{}\n'.format(lat))
        fo.write('{}\n'.format(lon))
        fo.write('{}\n'.format(timezone))
        fo.write('{}\n'.format(et))
        fo.write('{}\n'.format(lt))
        ################################ get data for CURRENT
        lue = data['current']['last_updated_epoch']
        lu = data['current']['last_updated']
        tempc = data['current']['temp_c']
        tempf = data['current']['temp_f']
        isday = data['current']['is_day']
        text = data['current']['condition']['text']
        icon = data['current']['condition']['icon']
        code = data['current']['condition']['code']
        windspeedmph = data['current']['wind_mph']
        windspeedkmh = data['current']['wind_kph']
        winddeg = data['current']['wind_degree']
        winddegabb = data['current']['wind_dir']
        pressuremb = data['current']['pressure_mb']
        pressurein = data['current']['pressure_in']
        precipmm = data['current']['precip_mm']
        precipin = data['current']['precip_in']
        humidity = data['current']['humidity']
        clouds = data['current']['cloud']
        tempfeelslikec = data['current']['feelslike_c']
        tempfeelslikef = data['current']['feelslike_f']
        windchillc = data['current']['windchill_c']
        windchillf = data['current']['windchill_f']
        heatindexc = data['current']['heatindex_c']
        heatindexf = data['current']['heatindex_f']
        dewpointc = data['current']['dewpoint_c']
        dewpointf = data['current']['dewpoint_f']
        viskm = data['current']['vis_km']
        vismh = data['current']['vis_miles']
        uv = data['current']['uv']
        windgustmph = data['current']['gust_mph']
        windgustkmh = data['current']['gust_kph']
        co = data['current']['air_quality']['co']
        co = round(co, 2)
        no2 = data['current']['air_quality']['no2']
        no2 = round(no2, 2)
        o3 = data['current']['air_quality']['o3']
        o3 = round(o3, 2)
        so2 = data['current']['air_quality']['so2']
        so2 = round(so2, 2)
        pm25 = data['current']['air_quality']['pm2_5']
        pm25 = round(pm25, 2)
        pm10 = data['current']['air_quality']['pm10']
        pm10 = round(pm10, 2)
        usepaindex = data['current']['air_quality']['us-epa-index']
        gbdefraindex = data['current']['air_quality']['gb-defra-index']
        ################################ write CURRENT raw data on a file
        #                   set the path for CURRENT raw data
        ptodayraw = home + homename + ptemp + 'watodayraw.txt'
        fo = open(ptodayraw, 'w')
        fo.write('lastupdatedepoch: {}\n'.format(lue))
        fo.write('lastupdated: {}\n'.format(lu))
        fo.write('tempc: {}\n'.format(tempc))
        fo.write('tempf: {}\n'.format(tempf))
        fo.write('day-night: {}\n'.format(isday))
        fo.write('weathertext: {}\n'.format(text))
        fo.write('icon: {}\n'.format(icon))
        fo.write('code: {}\n'.format(code))
        fo.write('windspeedmph: {}\n'.format(windspeedmph))
        fo.write('windspeedkmh: {}\n'.format(windspeedkmh))
        fo.write('winddeg: {}\n'.format(winddeg))
        fo.write('winddegabb: {}\n'.format(winddegabb))
        fo.write('presmb: {}\n'.format(pressuremb))
        fo.write('presin: {}\n'.format(pressurein))
        fo.write('precipmm: {}\n'.format(precipmm))
        fo.write('precipin: {}\n'.format(precipin))
        fo.write('humidity: {}\n'.format(humidity))
        fo.write('clouds: {}\n'.format(clouds))
        fo.write('tempfeelsc: {}\n'.format(tempfeelslikec))
        fo.write('tempfeelsf: {}\n'.format(tempfeelslikef))
        fo.write('windchillc: {}\n'.format(windchillc))
        fo.write('windchillf: {}\n'.format(windchillf))
        fo.write('heatindexc: {}\n'.format(heatindexc))
        fo.write('heatindexf: {}\n'.format(heatindexf))
        fo.write('dewpointc: {}\n'.format(dewpointc))
        fo.write('dewpointf: {}\n'.format(dewpointf))
        fo.write('viskm: {}\n'.format(viskm))
        fo.write('vismph: {}\n'.format(vismh))
        fo.write('uvindex: {}\n'.format(uv))
        fo.write('windgustmph: {}\n'.format(windgustmph))
        fo.write('windgustkmh: {}\n'.format(windgustkmh))
        fo.write('co: {}\n'.format(co))
        fo.write('no2: {}\n'.format(no2))
        fo.write('o3: {}\n'.format(o3))
        fo.write('so2: {}\n'.format(so2))
        fo.write('pm2-5: {}\n'.format(pm25))
        fo.write('pm10: {}\n'.format(pm10))
        fo.write('us-epa-index: {}\n'.format(usepaindex))
        fo.write('gb-defra-index: {}\n'.format(gbdefraindex))
        fo.close()
        ################################ write CURRENT clean data on a file
        #                   set the path for CURRENT clean data
        ptodayclean = home + homename + ptemp + 'watodayclean.txt'
        fo = open(ptodayclean, 'w')
        fo.write('{}\n'.format(lue))
        fo.write('{}\n'.format(lu))
        fo.write('{}\n'.format(tempc))
        fo.write('{}\n'.format(tempf))
        fo.write('{}\n'.format(isday))
        fo.write('{}\n'.format(text))
        fo.write('{}\n'.format(icon))
        fo.write('{}\n'.format(code))
        fo.write('{}\n'.format(windspeedmph))
        fo.write('{}\n'.format(windspeedkmh))
        fo.write('{}\n'.format(winddeg))
        fo.write('{}\n'.format(winddegabb))
        fo.write('{}\n'.format(pressuremb))
        fo.write('{}\n'.format(pressurein))
        fo.write('{}\n'.format(precipmm))
        fo.write('{}\n'.format(precipin))
        fo.write('{}\n'.format(humidity))
        fo.write('{}\n'.format(clouds))
        fo.write('{}\n'.format(tempfeelslikec))
        fo.write('{}\n'.format(tempfeelslikef))
        fo.write('{}\n'.format(windchillc))
        fo.write('{}\n'.format(windchillf))
        fo.write('{}\n'.format(heatindexc))
        fo.write('{}\n'.format(heatindexf))
        fo.write('{}\n'.format(dewpointc))
        fo.write('{}\n'.format(dewpointf))
        fo.write('{}\n'.format(viskm))
        fo.write('{}\n'.format(vismh))
        fo.write('{}\n'.format(uv))
        fo.write('{}\n'.format(windgustmph))
        fo.write('{}\n'.format(windgustkmh))
        fo.write('{}\n'.format(co))
        fo.write('{}\n'.format(no2))
        fo.write('{}\n'.format(o3))
        fo.write('{}\n'.format(so2))
        fo.write('{}\n'.format(pm25))
        fo.write('{}\n'.format(pm10))
        fo.write('{}\n'.format(usepaindex))
        fo.write('{}\n'.format(gbdefraindex))
        fo.close()
        ################################ create array for FORECAST data
        #                   day (block=2+22)
        fdt = []
        fep = []
        dmaxc = []
        dmaxf = []
        dminc = []
        dminf = []
        davgc = []
        davgf = []
        dmaxwm = []
        dmaxwk = []
        dprem = []
        dprei = []
        dsnowcm = []
        dvisk = []
        dvism = []
        dhum = []
        drain = []
        drainprob = []
        dsnow = []
        dsnowprob = []
        dtext = []
        dicon = []
        dcode = []
        duv = []
        #                   astro (block=8)
        dsunrise = []
        dsunset = []
        dmoonrise = []
        dmoonset = []
        dmoonphase = []
        dmoonillu = []
        moonup = []
        sunup = []
        #                   hourly (block=36)
        hep = []
        hdt = []
        htc = []
        htf = []
        hisday = []
        htext = []
        hicon = []
        hcode = []
        hwm = []
        hwk = []
        hwd = []
        hwdir = []
        hpresm = []
        hpresi = []
        hprecm = []
        hpreci = []
        hsnowcm = []
        hhum = []
        hcloud = []
        htfeelc = []
        htfeelf = []
        hwchillc = []
        hwchillf = []
        hhic = []
        hhif = []
        hdpc = []
        hdpf = []
        hrain = []
        hrainprob = []
        hsnow = []
        hsnowpro = []
        hvisk = []
        hvism = []
        hwgustm = []
        hwgustk = []
        huv = []
        ################################ get data for FORECAST section
        fouvd = open(puvid, 'w')
        fouvh = open(puvih, 'w')
        fodp = open(pdewp, 'w')
        #                   set the paths for the DAY+ASTRO section (raw data)
        pforecastrawd = home + homename + ptemp + '-daily.txt'
        fodr = open(pforecastrawd, 'w')
        #                   set the paths for the HOUR section(raw data)
        pforecastrawh = home + homename + ptemp + '-hourly.txt'
        fohr = open(pforecastrawh, 'w')
        #                   set the paths for the DAY+ASTRO section (clean data)
        pforecastcleand = home + homename + ptemp + 'daily.txt'
        fodc = open(pforecastcleand, 'w')
        #                   set the paths for the HOUR section (clean data)
        pforecastcleanh = home + homename + ptemp + 'hourly.txt'
        fohc = open(pforecastcleanh, 'w')
        for i in range(0, forecastday):
            fdt.append(data['forecast']['forecastday'][i]['date'])
            fodr.write('date: {}\n'.format(fdt[-1]))
            fodc.write('{}\n'.format(fdt[-1]))
            fep.append(data['forecast']['forecastday'][i]['date_epoch'])
            fodr.write('epochdate: {}\n'.format(fep[-1]))
            fodc.write('{}\n'.format(fep[-1]))
            dmaxc.append(data['forecast']['forecastday'][i]['day']['maxtemp_c'])
            fodr.write('maxtempc: {}\n'.format(dmaxc[-1]))
            fodc.write('{}\n'.format(dmaxc[-1]))
            dmaxf.append(data['forecast']['forecastday'][i]['day']['maxtemp_f'])
            fodr.write('maxtempf: {}\n'.format(dmaxf[-1]))
            fodc.write('{}\n'.format(dmaxf[-1]))
            dminc.append(data['forecast']['forecastday'][i]['day']['mintemp_c'])
            fodr.write('mintempc: {}\n'.format(dminc[-1]))
            fodc.write('{}\n'.format(dminc[-1]))
            dminf.append(data['forecast']['forecastday'][i]['day']['mintemp_f'])
            fodr.write('mintempf: {}\n'.format(dminf[-1]))
            fodc.write('{}\n'.format(dminf[-1]))
            davgc.append(data['forecast']['forecastday'][i]['day']['avgtemp_c'])
            fodr.write('avgtempc: {}\n'.format(davgc[-1]))
            fodc.write('{}\n'.format(davgc[-1]))
            davgf.append(data['forecast']['forecastday'][i]['day']['avgtemp_f'])
            fodr.write('avgtempf: {}\n'.format(davgf[-1]))
            fodc.write('{}\n'.format(davgf[-1]))
            dmaxwm.append(data['forecast']['forecastday'][i]['day']['maxwind_mph'])
            fodr.write('maxwindm: {}\n'.format(dmaxwm[-1]))
            fodc.write('{}\n'.format(dmaxwm[-1]))
            dmaxwk.append(data['forecast']['forecastday'][i]['day']['maxwind_kph'])
            fodr.write('maxwindk: {}\n'.format(dmaxwk[-1]))
            fodc.write('{}\n'.format(dmaxwk[-1]))
            dprem.append(data['forecast']['forecastday'][i]['day']['totalprecip_mm'])
            fodr.write('totalprecm: {}\n'.format(dprem[-1]))
            fodc.write('{}\n'.format(dprem[-1]))
            dprei.append(data['forecast']['forecastday'][i]['day']['totalprecip_in'])
            fodr.write('totalpreci: {}\n'.format(dprei[-1]))
            fodc.write('{}\n'.format(dprei[-1]))
            dsnowcm.append(data['forecast']['forecastday'][i]['day']['totalsnow_cm'])
            fodr.write('totalsnow_cm: {}\n'.format(dsnowcm[-1]))
            fodc.write('{}\n'.format(dsnowcm[-1])) 
            dvisk.append(data['forecast']['forecastday'][i]['day']['avgvis_km'])
            fodr.write('avgvisk: {}\n'.format(dvisk[-1]))
            fodc.write('{}\n'.format(dvisk[-1]))
            dvism.append(data['forecast']['forecastday'][i]['day']['avgvis_miles'])
            fodr.write('avgvism: {}\n'.format(dvism[-1]))
            fodc.write('{}\n'.format(dvism[-1]))
            dhum.append(data['forecast']['forecastday'][i]['day']['avghumidity'])
            fodr.write('humidity: {}\n'.format(dhum[-1]))
            fodc.write('{}\n'.format(dhum[-1]))
            drain.append(data['forecast']['forecastday'][i]['day']['daily_will_it_rain'])
            fodr.write('willitrain: {}\n'.format(drain[-1]))
            fodc.write('{}\n'.format(drain[-1]))
            drainprob.append(data['forecast']['forecastday'][i]['day']['daily_chance_of_rain'])
            fodr.write('chanceofrain: {}\n'.format(drainprob[-1]))
            fodc.write('{}\n'.format(drainprob[-1]))
            dsnow.append(data['forecast']['forecastday'][i]['day']['daily_will_it_snow'])
            fodr.write('willitsnow: {}\n'.format(dsnow[-1]))
            fodc.write('{}\n'.format(dsnow[-1]))
            dsnowprob.append(data['forecast']['forecastday'][i]['day']['daily_chance_of_snow'])
            fodr.write('chanceofsnow: {}\n'.format(dsnowprob[-1]))
            fodc.write('{}\n'.format(dsnowprob[-1]))
            dtext.append(data['forecast']['forecastday'][i]['day']['condition']['text'])
            fodr.write('text: {}\n'.format(dtext[-1]))
            fodc.write('{}\n'.format(dtext[-1]))
            dicon.append(data['forecast']['forecastday'][i]['day']['condition']['icon'])
            dicon2 = data['forecast']['forecastday'][i]['day']['condition']['icon']
            fodr.write('icon: {}\n'.format(dicon[-1]))
            dicon[i] = dicon[i][-7:]
            dicon2 = dicon2[-7:]
            fodc.write('{}\n'.format(dicon2))
            dcode.append(data['forecast']['forecastday'][i]['day']['condition']['code'])
            fodr.write('code: {}\n'.format(dcode[-1]))
            fodc.write('{}\n'.format(dcode[-1]))
            duv.append(data['forecast']['forecastday'][i]['day']['uv'])
            fodr.write('uvindex: {}\n'.format(duv[-1]))
            fodc.write('{}\n'.format(duv[-1]))
            duv2 = data['forecast']['forecastday'][i]['day']['uv']
            resvalue, rescolor = uvindexDH(puvid, duv2)
            fouvd.write('{}\n'.format(resvalue))
            fouvd.write('{}\n'.format(rescolor))
            dsunrise.append(data['forecast']['forecastday'][i]['astro']['sunrise'])
            fodr.write('sunrise: {}\n'.format(dsunrise[-1]))
            fodc.write('{}\n'.format(dsunrise[-1]))
            dsunset.append(data['forecast']['forecastday'][i]['astro']['sunset'])
            fodr.write('sunset: {}\n'.format(dsunset[-1]))
            fodc.write('{}\n'.format(dsunset[-1]))
            dmoonrise.append(data['forecast']['forecastday'][i]['astro']['moonrise'])
            fodr.write('moonrise: {}\n'.format(dmoonrise[-1]))
            fodc.write('{}\n'.format(dmoonrise[-1]))
            dmoonset.append(data['forecast']['forecastday'][i]['astro']['moonset'])
            fodr.write('moonset: {}\n'.format(dmoonset[-1]))
            fodc.write('{}\n'.format(dmoonset[-1]))
            dmoonphase.append(data['forecast']['forecastday'][i]['astro']['moon_phase'])
            fodr.write('moonphase: {}\n'.format(dmoonphase[-1]))
            fodc.write('{}\n'.format(dmoonphase[-1]))
            dmoonillu.append(data['forecast']['forecastday'][i]['astro']['moon_illumination'])
            fodr.write('moonillumi: {}\n'.format(dmoonillu[-1]))
            fodc.write('{}\n'.format(dmoonillu[-1]))
            moonup.append(data['forecast']['forecastday'][i]['astro']['is_moon_up'])
            fodr.write('ismoonup: {}\n'.format(moonup[-1]))
            fodc.write('{}\n'.format(moonup[-1]))
            sunup.append(data['forecast']['forecastday'][i]['astro']['is_sun_up'])
            fodr.write('ismoonup: {}\n'.format(sunup[-1]))
            fodc.write('{}\n'.format(sunup[-1]))
            for y in range(0, grouph):
                hep.append(data['forecast']['forecastday'][i]['hour'][y]['time_epoch'])
                fohr.write('date_epoch: {}\n'.format(hep[-1]))
                fohc.write('{}\n'.format(hep[-1]))
                hdt.append(data['forecast']['forecastday'][i]['hour'][y]['time'])
                fohr.write('date: {}\n'.format(hdt[-1]))
                fohc.write('{}\n'.format(hdt[-1]))
                htc.append(data['forecast']['forecastday'][i]['hour'][y]['temp_c'])
                fohr.write('temp_c: {}\n'.format(htc[-1]))
                fohc.write('{}\n'.format(htc[-1]))
                htf.append(data['forecast']['forecastday'][i]['hour'][y]['temp_f'])
                fohr.write('temp_f: {}\n'.format(htf[-1]))
                fohc.write('{}\n'.format(htf[-1]))
                hisday.append(data['forecast']['forecastday'][i]['hour'][y]['is_day'])
                fohr.write('is_day: {}\n'.format(hisday[-1]))
                fohc.write('{}\n'.format(hisday[-1]))
                htext.append(data['forecast']['forecastday'][i]['hour'][y]['condition']['text'])
                fohr.write('text: {}\n'.format(htext[-1]))
                fohc.write('{}\n'.format(htext[-1]))
                hicon.append(data['forecast']['forecastday'][i]['hour'][y]['condition']['icon'])
                hicon2 = data['forecast']['forecastday'][i]['hour'][y]['condition']['icon']
                fohr.write('icon: {}\n'.format(hicon[-1]))
                hicon[y] = hicon[y][-7:]
                hicon2 = hicon2[-7:]
                fohc.write('{}\n'.format(hicon2))
                hcode.append(data['forecast']['forecastday'][i]['hour'][y]['condition']['code'])
                fohr.write('code: {}\n'.format(hcode[-1]))
                fohc.write('{}\n'.format(hcode[-1]))
                hwm.append(data['forecast']['forecastday'][i]['hour'][y]['wind_mph'])
                fohr.write('wind_mph: {}\n'.format(hwm[-1]))
                fohc.write('{}\n'.format(hwm[-1]))
                hwk.append(data['forecast']['forecastday'][i]['hour'][y]['wind_kph'])
                fohr.write('wind_kph: {}\n'.format(hwk[-1]))
                fohc.write('{}\n'.format(hwk[-1]))
                hwd.append(data['forecast']['forecastday'][i]['hour'][y]['wind_degree'])
                fohr.write('wind_degree: {}\n'.format(hwd[-1]))
                fohc.write('{}\n'.format(hwd[-1]))
                hwdir.append(data['forecast']['forecastday'][i]['hour'][y]['wind_dir'])
                fohr.write('wind_dir: {}\n'.format(hwdir[-1]))
                fohc.write('{}\n'.format(hwdir[-1]))
                hpresm.append(data['forecast']['forecastday'][i]['hour'][y]['pressure_mb'])
                fohr.write('pressure_mb: {}\n'.format(hpresm[-1]))
                fohc.write('{}\n'.format(hpresm[-1]))
                hpresi.append(data['forecast']['forecastday'][i]['hour'][y]['pressure_in'])
                fohr.write('pressure_in: {}\n'.format(hpresi[-1]))
                fohc.write('{}\n'.format(hpresi[-1]))
                hprecm.append(data['forecast']['forecastday'][i]['hour'][y]['precip_mm'])
                fohr.write('precip_mm: {}\n'.format(hprecm[-1]))
                fohc.write('{}\n'.format(hprecm[-1]))
                hpreci.append(data['forecast']['forecastday'][i]['hour'][y]['precip_in'])
                fohr.write('precip_in: {}\n'.format(hpreci[-1]))
                fohc.write('{}\n'.format(hpreci[-1]))
                hsnowcm.append(data['forecast']['forecastday'][i]['hour'][y]['snow_cm'])
                fohr.write('snow_cm: {}\n'.format(hsnowcm[-1]))
                fohc.write('{}\n'.format(hsnowcm[-1]))
                hhum.append(data['forecast']['forecastday'][i]['hour'][y]['humidity'])
                fohr.write('humidity: {}\n'.format(hhum[-1]))
                fohc.write('{}\n'.format(hhum[-1]))
                hcloud.append(data['forecast']['forecastday'][i]['hour'][y]['cloud'])
                fohr.write('cloud: {}\n'.format(hcloud[-1]))
                fohc.write('{}\n'.format(hcloud[-1]))
                htfeelc.append(data['forecast']['forecastday'][i]['hour'][y]['feelslike_c'])
                fohr.write('feelslike_c: {}\n'.format(htfeelc[-1]))
                fohc.write('{}\n'.format(htfeelc[-1]))
                htfeelf.append(data['forecast']['forecastday'][i]['hour'][y]['feelslike_f'])
                fohr.write('feelslike_f: {}\n'.format(htfeelf[-1]))
                fohc.write('{}\n'.format(htfeelf[-1]))
                hwchillc.append(data['forecast']['forecastday'][i]['hour'][y]['windchill_c'])
                fohr.write('windchill_c: {}\n'.format(hwchillc[-1]))
                fohc.write('{}\n'.format(hwchillc[-1]))
                hwchillf.append(data['forecast']['forecastday'][i]['hour'][y]['windchill_f'])
                fohr.write('windchill_f: {}\n'.format(hwchillf[-1]))
                fohc.write('{}\n'.format(hwchillf[-1]))
                hhic.append(data['forecast']['forecastday'][i]['hour'][y]['heatindex_c'])
                fohr.write('heatindex_c: {}\n'.format(hhic[-1]))
                fohc.write('{}\n'.format(hhic[-1]))
                hhif.append(data['forecast']['forecastday'][i]['hour'][y]['heatindex_f'])
                fohr.write('heatindex_f: {}\n'.format(hhif[-1]))
                fohc.write('{}\n'.format(hhif[-1]))
                hdpc.append(data['forecast']['forecastday'][i]['hour'][y]['dewpoint_c'])
                hdpc2 = data['forecast']['forecastday'][i]['hour'][y]['dewpoint_c']
                fohr.write('dewpoint_c: {}\n'.format(hdpc[-1]))
                fohc.write('{}\n'.format(hdpc[-1]))
                resvalue, rescolor = dewpointH(pdewp, hdpc2)
                fodp.write('{}\n'.format(resvalue))
                fodp.write('{}\n'.format(rescolor))
                hdpf.append(data['forecast']['forecastday'][i]['hour'][y]['dewpoint_f'])
                fohr.write('dewpoint_f: {}\n'.format(hdpf[-1]))
                fohc.write('{}\n'.format(hdpf[-1]))
                hrain.append(data['forecast']['forecastday'][i]['hour'][y]['will_it_rain'])
                fohr.write('will_it_rain: {}\n'.format(hrain[-1]))
                fohc.write('{}\n'.format(hrain[-1]))
                hrainprob.append(data['forecast']['forecastday'][i]['hour'][y]['chance_of_rain'])
                fohr.write('chance_of_rain: {}\n'.format(hrainprob[-1]))
                fohc.write('{}\n'.format(hrainprob[-1]))
                hsnow.append(data['forecast']['forecastday'][i]['hour'][y]['will_it_snow'])
                fohr.write('will_it_snow: {}\n'.format(hsnow[-1]))
                fohc.write('{}\n'.format(hsnow[-1]))
                hsnowpro.append(data['forecast']['forecastday'][i]['hour'][y]['chance_of_snow'])
                fohr.write('chance_of_snow: {}\n'.format(hsnowpro[-1]))
                fohc.write('{}\n'.format(hsnowpro[-1]))
                hvisk.append(data['forecast']['forecastday'][i]['hour'][y]['vis_km'])
                fohr.write('vis_km: {}\n'.format(hvisk[-1]))
                fohc.write('{}\n'.format(hvisk[-1]))
                hvism.append(data['forecast']['forecastday'][i]['hour'][y]['vis_miles'])
                fohr.write('vis_miles: {}\n'.format(hvism[-1]))
                fohc.write('{}\n'.format(hvism[-1]))
                hwgustm.append(data['forecast']['forecastday'][i]['hour'][y]['gust_mph'])
                fohr.write('gust_mph: {}\n'.format(hwgustm[-1]))
                fohc.write('{}\n'.format(hwgustm[-1]))
                hwgustk.append(data['forecast']['forecastday'][i]['hour'][y]['gust_kph'])
                fohr.write('gust_kph: {}\n'.format(hwgustk[-1]))
                fohc.write('{}\n'.format(hwgustk[-1]))
                huv.append(data['forecast']['forecastday'][i]['hour'][y]['uv'])
                huv2 = data['forecast']['forecastday'][i]['hour'][y]['uv']
                fohr.write('uv: {}\n'.format(huv[-1]))
                fohc.write('{}\n'.format(huv[-1]))
                resvalue, rescolor = uvindexDH(puvih, huv2)
                fouvh.write('{}\n'.format(resvalue))
                fouvh.write('{}\n'.format(rescolor))
        fodr.close()
        fohr.close()
        fodc.close()
        fohc.close()
        fouvd.close()
        fouvh.close()
        fodp.close()
    else:
        fo = open(pforecastrawd, 'w')
        fo.write('error: {}\n'.format(status_code))
        fo.close()
        fo = open(pforecastrawh, 'w')
        fo.write('error: {}\n'.format(status_code))
        fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed