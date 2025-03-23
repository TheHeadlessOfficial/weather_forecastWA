# Lock file to tell conky that the script is running
lock_file = "/tmp/script_waforecast.lock"
try:
    # Check for file lock
    open(lock_file, 'w').close()
    import os
    # from PIL import Image
    import time
    import requests
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude, city and APPID
    mylat = 45.40713
    mylon = 11.87680
    mycity = '' # type between apostrophes
    myAPPID = '' # type between apostrophes
    ################################ pattern url forecast
    #                  my API url forecast
    url = 'https://api.weatherapi.com/v1/forecast.json?key=' + myAPPID + '&q=' + mycity + '&days=10&aqi=yes&alerts=yes'
    res = requests.get(url).json()
    data = res
    ################################ set variables
    forecastday = 3
    grouph = 24
    temporary = ''
    vtext = 'n/a'
    ################################ set error variables
    coderr = 0
    ################################ set default conky folder (change it if needed)
    home = '/home/'
    conky = '/.conky/'
    ################################ set the paths for the API files
    ptemp = conky + '/weather/Weatherapi/forecast/'
    ################################ set paths
    ptemp2 = conky + "/weather/Weatherapi/"
    ptemp3 = " $HOME" + conky + "/weather/Weatherapi/"
    ptemp4 = " $HOME" + conky + "/weather/Weatherapi/forecast/"
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
    varerror = '200'
    try:
        coderr = data['error']
    except:
        coderr = varerror
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(coderr))
    fo.close()
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
    #                   day (block=23)
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
    #                   astro (block=6)
    dsunrise = []
    dsunset = []
    dmoonrise = []
    dmoonset = []
    dmoonphase = []
    dmoonillu = []
    #                   hourly (block=35)
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
    for i in range(0, forecastday):
        fdt.append(data['forecast']['forecastday'][i]['date'])
        fep.append(data['forecast']['forecastday'][i]['date_epoch'])
        dmaxc.append(data['forecast']['forecastday'][i]['day']['maxtemp_c'])
        dmaxf.append(data['forecast']['forecastday'][i]['day']['maxtemp_f'])
        dminc.append(data['forecast']['forecastday'][i]['day']['mintemp_c'])
        dminf.append(data['forecast']['forecastday'][i]['day']['mintemp_f'])
        davgc.append(data['forecast']['forecastday'][i]['day']['avgtemp_c'])
        davgf.append(data['forecast']['forecastday'][i]['day']['avgtemp_f'])
        dmaxwm.append(data['forecast']['forecastday'][i]['day']['maxwind_mph'])
        dmaxwk.append(data['forecast']['forecastday'][i]['day']['maxwind_kph'])
        dprem.append(data['forecast']['forecastday'][i]['day']['totalprecip_mm'])
        dprei.append(data['forecast']['forecastday'][i]['day']['totalprecip_in'])
        dvisk.append(data['forecast']['forecastday'][i]['day']['avgvis_km'])
        dvism.append(data['forecast']['forecastday'][i]['day']['avgvis_miles'])
        dhum.append(data['forecast']['forecastday'][i]['day']['avghumidity'])
        drain.append(data['forecast']['forecastday'][i]['day']['daily_will_it_rain'])
        drainprob.append(data['forecast']['forecastday'][i]['day']['daily_chance_of_rain'])
        dsnow.append(data['forecast']['forecastday'][i]['day']['daily_will_it_snow'])
        dsnowprob.append(data['forecast']['forecastday'][i]['day']['daily_chance_of_snow'])
        dtext.append(data['forecast']['forecastday'][i]['day']['condition']['text'])
        dicon.append(data['forecast']['forecastday'][i]['day']['condition']['icon'])
        dcode.append(data['forecast']['forecastday'][i]['day']['condition']['code'])
        duv.append(data['forecast']['forecastday'][i]['day']['uv'])
        dsunrise.append(data['forecast']['forecastday'][i]['astro']['sunrise'])
        dsunset.append(data['forecast']['forecastday'][i]['astro']['sunset'])
        dmoonrise.append(data['forecast']['forecastday'][i]['astro']['moonrise'])
        dmoonset.append(data['forecast']['forecastday'][i]['astro']['moonset'])
        dmoonphase.append(data['forecast']['forecastday'][i]['astro']['moon_phase'])
        dmoonillu.append(data['forecast']['forecastday'][i]['astro']['moon_illumination'])
        for y in range(0, grouph):
            hep.append(data['forecast']['forecastday'][i]['hour'][y]['time_epoch'])
            hdt.append(data['forecast']['forecastday'][i]['hour'][y]['time'])
            htc.append(data['forecast']['forecastday'][i]['hour'][y]['temp_c'])
            htf.append(data['forecast']['forecastday'][i]['hour'][y]['temp_f'])
            hisday.append(data['forecast']['forecastday'][i]['hour'][y]['is_day'])
            htext.append(data['forecast']['forecastday'][i]['hour'][y]['condition']['text'])
            hicon.append(data['forecast']['forecastday'][i]['hour'][y]['condition']['icon'])
            hcode.append(data['forecast']['forecastday'][i]['hour'][y]['condition']['code'])
            hwm.append(data['forecast']['forecastday'][i]['hour'][y]['wind_mph'])
            hwk.append(data['forecast']['forecastday'][i]['hour'][y]['wind_kph'])
            hwd.append(data['forecast']['forecastday'][i]['hour'][y]['wind_degree'])
            hwdir.append(data['forecast']['forecastday'][i]['hour'][y]['wind_dir'])
            hpresm.append(data['forecast']['forecastday'][i]['hour'][y]['pressure_mb'])
            hpresi.append(data['forecast']['forecastday'][i]['hour'][y]['pressure_in'])
            hprecm.append(data['forecast']['forecastday'][i]['hour'][y]['precip_mm'])
            hpreci.append(data['forecast']['forecastday'][i]['hour'][y]['precip_in'])
            hhum.append(data['forecast']['forecastday'][i]['hour'][y]['humidity'])
            hcloud.append(data['forecast']['forecastday'][i]['hour'][y]['cloud'])
            htfeelc.append(data['forecast']['forecastday'][i]['hour'][y]['feelslike_c'])
            htfeelf.append(data['forecast']['forecastday'][i]['hour'][y]['feelslike_f'])
            hwchillc.append(data['forecast']['forecastday'][i]['hour'][y]['windchill_c'])
            hwchillf.append(data['forecast']['forecastday'][i]['hour'][y]['windchill_f'])
            hhic.append(data['forecast']['forecastday'][i]['hour'][y]['heatindex_c'])
            hhif.append(data['forecast']['forecastday'][i]['hour'][y]['heatindex_f'])
            hdpc.append(data['forecast']['forecastday'][i]['hour'][y]['dewpoint_c'])
            hdpf.append(data['forecast']['forecastday'][i]['hour'][y]['dewpoint_f'])
            hrain.append(data['forecast']['forecastday'][i]['hour'][y]['will_it_rain'])
            hrainprob.append(data['forecast']['forecastday'][i]['hour'][y]['chance_of_rain'])
            hsnow.append(data['forecast']['forecastday'][i]['hour'][y]['will_it_snow'])
            hsnowpro.append(data['forecast']['forecastday'][i]['hour'][y]['chance_of_snow'])
            hvisk.append(data['forecast']['forecastday'][i]['hour'][y]['vis_km'])
            hvism.append(data['forecast']['forecastday'][i]['hour'][y]['vis_miles'])
            hwgustm.append(data['forecast']['forecastday'][i]['hour'][y]['gust_mph'])
            hwgustk.append(data['forecast']['forecastday'][i]['hour'][y]['gust_kph'])
            huv.append(data['forecast']['forecastday'][i]['hour'][y]['uv'])
    fo.close()
    ################################ write raw data for FORECAST section
    #                   set the paths for the DAY+ASTRO section
    pforecastrawd = home + homename + ptemp + '-daily.txt'
    fo = open(pforecastrawd, 'w')
    for i in range(0, forecastday):
        fo.write('date: {}\n'.format(fdt[i]))
        fo.write('epochdate: {}\n'.format(fep[i]))
        fo.write('maxtempc: {}\n'.format(dmaxc[i]))
        fo.write('maxtempf: {}\n'.format(dmaxf[i]))
        fo.write('mintempc: {}\n'.format(dminc[i]))
        fo.write('mintempf: {}\n'.format(dminf[i]))
        fo.write('avgtempc: {}\n'.format(davgc[i]))
        fo.write('avgtempf: {}\n'.format(davgf[i]))
        fo.write('maxwindm: {}\n'.format(dmaxwm[i]))
        fo.write('maxwindk: {}\n'.format(dmaxwk[i]))
        fo.write('totalprecm: {}\n'.format(dprem[i]))
        fo.write('totalpreci: {}\n'.format(dprei[i]))
        fo.write('avgvisk: {}\n'.format(dvisk[i]))
        fo.write('avgvism: {}\n'.format(dvism[i]))
        fo.write('humidity: {}\n'.format(dhum[i]))
        fo.write('willitrain: {}\n'.format(drain[i]))
        fo.write('chanceofrain: {}\n'.format(drainprob[i]))
        fo.write('willitsnow: {}\n'.format(dsnow[i]))
        fo.write('chanceofsnow: {}\n'.format(dsnowprob[i]))
        fo.write('text: {}\n'.format(dtext[i]))
        fo.write('icon: {}\n'.format(dicon[i]))
        fo.write('code: {}\n'.format(dcode[i]))
        fo.write('uvindex: {}\n'.format(duv[i]))
        fo.write('sunrise: {}\n'.format(dsunrise[i]))
        fo.write('sunset: {}\n'.format(dsunset[i]))
        fo.write('moonrise: {}\n'.format(dmoonrise[i]))
        fo.write('moonset: {}\n'.format(dmoonset[i]))
        fo.write('moonphase: {}\n'.format(dmoonphase[i]))
        fo.write('moonillumi: {}\n'.format(dmoonillu[i]))
    fo.close()
    #                   set the paths for the HOURLY section
    pforecastrawh = home + homename + ptemp + '-hourly.txt'
    fo = open(pforecastrawh, 'w')
    for y in range(0, grouph):
        fo.write('date_epoch: {}\n'.format(hep[y]))
        fo.write('date: {}\n'.format(hdt[y]))
        fo.write('temp_c: {}\n'.format(htc[y]))
        fo.write('temp_f: {}\n'.format(htf[y]))
        fo.write('is_day: {}\n'.format(hisday[y]))
        fo.write('text: {}\n'.format(htext[y]))
        fo.write('icon: {}\n'.format(hicon[y]))
        fo.write('code: {}\n'.format(hcode[y]))
        fo.write('wind_mph: {}\n'.format(hwm[y]))
        fo.write('wind_kph: {}\n'.format(hwk[y]))
        fo.write('wind_degree: {}\n'.format(hwd[y]))
        fo.write('wind_dir: {}\n'.format(hwdir[y]))
        fo.write('pressure_mb: {}\n'.format(hpresm[y]))
        fo.write('pressure_in: {}\n'.format(hpresi[y]))
        fo.write('precip_mm: {}\n'.format(hprecm[y]))
        fo.write('precip_in: {}\n'.format(hpreci[y]))
        fo.write('humidity: {}\n'.format(hhum[y]))
        fo.write('cloud: {}\n'.format(hcloud[y]))
        fo.write('feelslike_c: {}\n'.format(htfeelc[y]))
        fo.write('feelslike_f: {}\n'.format(htfeelf[y]))
        fo.write('windchill_c: {}\n'.format(hwchillc[y]))
        fo.write('windchill_f: {}\n'.format(hwchillf[y]))
        fo.write('heatindex_c: {}\n'.format(hhic[y]))
        fo.write('heatindex_f: {}\n'.format(hhif[y]))
        fo.write('dewpoint_c: {}\n'.format(hdpc[y]))
        fo.write('dewpoint_f: {}\n'.format(hdpf[y]))
        fo.write('will_it_rain: {}\n'.format(hrain[y]))
        fo.write('chance_of_rain: {}\n'.format(hrainprob[y]))
        fo.write('will_it_snow: {}\n'.format(hsnow[y]))
        fo.write('chance_of_snow: {}\n'.format(hsnowpro[y]))
        fo.write('vis_km: {}\n'.format(hvisk[y]))
        fo.write('vis_miles: {}\n'.format(hvism[y]))
        fo.write('gust_mph: {}\n'.format(hwgustm[y]))
        fo.write('gust_kph: {}\n'.format(hwgustk[y]))
        fo.write('uv: {}\n'.format(huv[y]))
    fo.close()
    ################################ write clean data for FORECAST section
    #                   set the paths for the DAY+ASTRO section
    pforecastcleand = home + homename + ptemp + 'daily.txt'
    fo = open(pforecastcleand, 'w')
    for i in range(0, forecastday):
        fo.write('{}\n'.format(fdt[i]))
        fo.write('{}\n'.format(fep[i]))
        fo.write('{}\n'.format(dmaxc[i]))
        fo.write('{}\n'.format(dmaxf[i]))
        fo.write('{}\n'.format(dminc[i]))
        fo.write('{}\n'.format(dminf[i]))
        fo.write('{}\n'.format(davgc[i]))
        fo.write('{}\n'.format(davgf[i]))
        fo.write('{}\n'.format(dmaxwm[i]))
        fo.write('{}\n'.format(dmaxwk[i]))
        fo.write('{}\n'.format(dprem[i]))
        fo.write('{}\n'.format(dprei[i]))
        fo.write('{}\n'.format(dvisk[i]))
        fo.write('{}\n'.format(dvism[i]))
        fo.write('{}\n'.format(dhum[i]))
        fo.write('{}\n'.format(drain[i]))
        fo.write('{}\n'.format(drainprob[i]))
        fo.write('{}\n'.format(dsnow[i]))
        fo.write('{}\n'.format(dsnowprob[i]))
        fo.write('{}\n'.format(dtext[i]))
        dicon[i] = dicon[i][-7:]
        fo.write('{}\n'.format(dicon[i]))
        fo.write('{}\n'.format(dcode[i]))
        fo.write('{}\n'.format(duv[i]))
        fo.write('{}\n'.format(dsunrise[i]))
        fo.write('{}\n'.format(dsunset[i]))
        fo.write('{}\n'.format(dmoonrise[i]))
        fo.write('{}\n'.format(dmoonset[i]))
        fo.write('{}\n'.format(dmoonphase[i]))
        fo.write('{}\n'.format(dmoonillu[i]))
    fo.close()
    #                   set the paths for the HOURLY section
    pforecastcleanh = home + homename + ptemp + 'hourly.txt'
    fo = open(pforecastcleanh, 'w')
    for y in range(0, grouph):
        fo.write('{}\n'.format(hep[y]))
        fo.write('{}\n'.format(hdt[y]))
        fo.write('{}\n'.format(htc[y]))
        fo.write('{}\n'.format(htf[y]))
        fo.write('{}\n'.format(hisday[y]))
        fo.write('{}\n'.format(htext[y]))
        hicon[y] = hicon[y][-7:]
        fo.write('{}\n'.format(hicon[y]))
        fo.write('{}\n'.format(hcode[y]))
        fo.write('{}\n'.format(hwm[y]))
        fo.write('{}\n'.format(hwk[y]))
        fo.write('{}\n'.format(hwd[y]))
        fo.write('{}\n'.format(hwdir[y]))
        fo.write('{}\n'.format(hpresm[y]))
        fo.write('{}\n'.format(hpresi[y]))
        fo.write('{}\n'.format(hprecm[y]))
        fo.write('{}\n'.format(hpreci[y]))
        fo.write('{}\n'.format(hhum[y]))
        fo.write('{}\n'.format(hcloud[y]))
        fo.write('{}\n'.format(htfeelc[y]))
        fo.write('{}\n'.format(htfeelf[y]))
        fo.write('{}\n'.format(hwchillc[y]))
        fo.write('{}\n'.format(hwchillf[y]))
        fo.write('{}\n'.format(hhic[y]))
        fo.write('{}\n'.format(hhif[y]))
        fo.write('{}\n'.format(hdpc[y]))
        fo.write('{}\n'.format(hdpf[y]))
        fo.write('{}\n'.format(hrain[y]))
        fo.write('{}\n'.format(hrainprob[y]))
        fo.write('{}\n'.format(hsnow[y]))
        fo.write('{}\n'.format(hsnowpro[y]))
        fo.write('{}\n'.format(hvisk[y]))
        fo.write('{}\n'.format(hvism[y]))
        fo.write('{}\n'.format(hwgustm[y]))
        fo.write('{}\n'.format(hwgustk[y]))
        fo.write('{}\n'.format(huv[y]))
    fo.close()
    ################################ calculate DAILY FORECAST UV index color and write it
    #                   set the paths for the UVI INDEX
    puvi = home + homename + ptemp + 'forecastdaylyuv.txt'
    fo = open(puvi, 'w')
    for i in range(0, forecastday):
        value = duv[i]
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
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate HOURLY FORECAST UV index color and write it
    #                   set the paths for the UVI INDEX
    puvi = home + homename + ptemp + 'forecasthourlyyuv.txt'
    fo = open(puvi, 'w')
    for i in range(0, grouph):
        value = huv[i]
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
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate HOURLY FORECAST dew point color and write it
    color = 'white'
    #                   set the paths for the DEW POINT
    pdewp = home + homename + ptemp + 'forecasthourlydewpt.txt'
    fo = open(pdewp, 'w')
    for i in range(0, grouph):
        value = hdpc[i]
        if (value < 19):
            color = 6
        elif (value >=19 and value < 22):
            color = 9
        elif (value >=22):
            color = 4
        else:
            color = 'white'
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
    ################################ create conky FORECAST statements
    #                 general variables
    firstd = 1
    firsth = 0
    blokd = 1
    blockh = 35
    #dashedline = '---------------------------------------------------------------------------------------------------------'
    #                 general settings
    rowgoto = '${goto '
    gotonumd = 60
    gotonumh = 95
    gotoplus = 0
    gotodelta = 20
    rowgraph = '}'
    rowcolor = '${color}'
    rowcolor1 = '${color1}'
    rowcolor2 = '${color2}'
    rowcolor3 = '${color3}'
    rowcolor4 = '${color4}'
    rowcolor5 = '${color5}'
    rowcolor6 = '${color6}'
    rowcolor9 = '${color9}'
    rowinfo = "${execpi 900 sed -n '"
    rowp = "p'"
    rowpathh = ptemp4 + 'hourly.txt'
    rowpathd = ptemp4 + 'daily.txt'
    rowprint2 = " | awk '{print $2}'"
    rowprint3 = " | awk '{print $3}'"
    rowbar = '/'
    rowfont6 = '${font URW Gothic L:size=6}'
    rowfont7 = '${font URW Gothic L:size=7}'
    rowfont8 = '${font URW Gothic L:size=8}'
    rowalignr = '${alignr}'
    rowalignc = '${alignc}'
    rowalignl = '${alignl}'
    rowvoffset = '${voffset 15}'
    #                 time settings
    gotohourh = 50
    gotohourd = 35
    rowhour = "h${execpi 900 sed -n '"
    rowcut = ' | cut -c1-5'
    #                 icons settings
    pi = '${image /home/'
    pi2 = homename
    pi3 = ptemp2 + 'icons/day/'
    pi3a = ptemp2 + 'icons/night/'
    pi4 = ptemp2 + 'iconsOWM/'
    est = ' -p '
    y = 0
    virg = ','
    zh = 0
    zhincrement = 87
    zd = 35
    size = 75 # icons size
    # use next 2 rows if you want WEATHERAPI icons
    pfh = ' -s ' + str(size) + 'x' + str(size) + '}'
    pfd = ' -s ' + str(size) + 'x' + str(size) + '}'
    # use next 2 rows if you want OWM icons
    #pfh = ' -s 95x65}'
    #pfd = ' -s 95x65}'
    #                 sunrise, sunset, moonrise, moonset
    rowsunrised = "Sr ${execpi 900 sed -n '"
    rowsunsetd = "Ss ${execpi 900 sed -n '"
    rowmoonrised = "Mr ${execpi 900 sed -n '"
    rowmoonsetd = "Ms ${execpi 900 sed -n '"
    #                 moon phase settings
    rowmoonphillud = "MoonLum ${execpi 900 sed -n '"
    rowmoonphphaseud = "Phase ${execpi 900 sed -n '"
    rowmoonlund = "MoonLun ${execpi 900 sed -n '"
    #                 wind settings
    rowwindsd= "Ws ${execpi 900 sed -n '"
    rowwindsd2= "Wg ${execpi 900 sed -n '"
    rowwindsd4= "Wdir ${execpi 900 sed -n '"
    rowwindsd4b= "W° ${execpi 900 sed -n '"
    rowwindsd5 = 'm/s'
    rowwindsd6 = 'Km/h'
    rowwindsd7 = 'mph'
    rowwindsd3 = "WC ${execpi 900 sed -n '"
    #                 wind gust settings
    rowwindgd= "Wg ${execpi 900 sed -n '"
    #                 humidity settings
    rowhumd = "H ${execpi 900 sed -n '"
    rowhumd2 = '%'
    #                 pressure settings
    rowpresd = "P ${execpi 900 sed -n '"
    rowpresd2 = 'hPa'
    rowpresd3 = 'mb'
    rowpresd4 = 'in'
    #                 temperature, feellike settings
    rowtempd = "${execpi 900 sed -n '"
    rowtemphid = "Thi ${execpi 900 sed -n '"
    rowtemplowd = "Tlow ${execpi 900 sed -n '"
    rowtempmind = "min ${execpi 900 sed -n '"
    rowtempmaxd = "max ${execpi 900 sed -n '"
    rowtempfmaxd = "fmax ${execpi 900 sed -n '"
    rowtempfmind = "fmin ${execpi 900 sed -n '"
    rowtempavg = "avg ${execpi 900 sed -n '"
    rowtempfd = "Tf ${execpi 900 sed -n '"
    rowtempdd = "Td ${execpi 900 sed -n '"
    rowtempnd = "Tn ${execpi 900 sed -n '"
    rowtemped = "Te ${execpi 900 sed -n '"
    rowtempmd = "Tm ${execpi 900 sed -n '"
    rowtempdfd = "Tdf ${execpi 900 sed -n '"
    rowtempnfd = "Tnf ${execpi 900 sed -n '"
    rowtempefd = "Tef ${execpi 900 sed -n '"
    rowtempmfd = "Tmf ${execpi 900 sed -n '"
    rowtempheat = "HI ${execpi 900 sed -n '"
    rowtempd2 = '°C'
    rowtempd2a = '°F'
    rowtempd3 = '°'
    #                 ozone settings
    rowozoned = "Oz ${execpi 900 sed -n '"
    rowozoned2 = 'Du'
    #                 maxDHI settings
    rowmaxdhi = "DHImax ${execpi 900 sed -n '"
    rowmaxdhi2 = 'W/m^2'
    #                 dew point settings
    rowdew = "Dp ${eval $${color${execpi 900 sed -n '"
    rowdewpathcolor1f = ptemp4 + "forecastdewpt.txt}}}"
    rowdewpathcolor1h = ptemp4 + "forecasthourlydewpt.txt}}}"
    rowdewpathcolor1d = ptemp4 + "dailyowmdewpoint.txt}}}"
    rowdewpathvalue1f = ptemp4 + "forecastdewpt.txt}"
    rowdewpathvalue1h = ptemp4 + "forecasthourlydewpt.txt}"
    rowdewpathvalue1d = ptemp4 + "dailyowmdewpoint.txt}"
    #                 uvi settings
    rowuvi = "UV ${eval $${color${execpi 900 sed -n '"
    rowuvipathcolor1f = ptemp4 + "forecastdaylyuv.txt}}}"
    rowuvipathcolor1h = ptemp4 + "forecasthourlyyuv.txt}}}"
    rowuvipathcolor1d = ptemp4 + "dailyuvindex.txt}}}"
    rowuvipathvalue1f = ptemp4 + "forecastdaylyuv.txt}"
    rowuvipathvalue1h = ptemp4 + "forecasthourlyyuv.txt}"
    rowuvipathvalue1d = ptemp4 + "dailyuvindex.txt}"
    #                 cloudness settings
    rowclo= "Cl ${execpi 900 sed -n '"
    rowclolow= "Cllow ${execpi 900 sed -n '"
    rowclomid= "Clmid ${execpi 900 sed -n '"
    rowclohi= "Clhi ${execpi 900 sed -n '"
    rowclo2 = '%'
    #                 visibility settings
    rowvis= "Vis ${execpi 900 sed -n '"
    rowvis2 = 'm'
    rowvis3 = 'Km'
    rowvis4 = 'miles'
    #                 pop settings
    rowpoprain = "PopR ${execpi 900 sed -n '"
    rowpoprainwill = "Rain? ${execpi 900 sed -n '"
    rowpopsnow = "PopS ${execpi 900 sed -n '"
    rowpopsnowwill = "Snow? ${execpi 900 sed -n '"
    #                 rain1h settings
    rowrain1 = "R1 ${execpi 900 sed -n '"
    rowrain1a = "Prec ${execpi 900 sed -n '"
    rowrain2 = 'mm'
    rowrain2a = 'in'
    #                 snow1h settings
    rowsnowd = "Snow ${execpi 900 sed -n '"
    rowsnowdepthd = "Sdepth:${execpi 900 sed -n '"
    rowsnow2 = 'mm'
    #                 forecast settings
    rowforecast = "${execpi 900 sed -n '"
    rowforecastval = "${execpi 900 sed -n '"
    #                                  main DAILY
    #                   set the paths for the FORECAST section
    pforecastcD = home + homename + ptemp + 'forecastconkyD.txt'
    y = 0
    counter = 0
    groupd = 29
    fo = open(pforecastcD, 'w')
    for i in range(firstd, forecastday):
        i2 = 1 + (groupd * i)
        vtemp = i2
        totrowdate = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowforecast + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowdate))
        vtemp = vtemp + 2
        #row n. 2 and multiples not present
        totrowtempmaxcd = rowgoto + str(gotonumd + gotoplus + gotodelta) + rowgraph + rowcolor4 + rowtempd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd3
        fo.write('{}\n'.format(totrowtempmaxcd))
        vtemp = vtemp + 1
        totrowtempmaxfd = rowgoto + str(gotonumd + gotoplus + gotodelta) + rowgraph + rowcolor4 + rowtempd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd3
        fo.write('{}\n'.format(totrowtempmaxfd))
        vtemp = vtemp + 1
        gotoplus = gotoplus + gotodelta
        totrowtempmincd = rowcolor1 + rowtempd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
        fo.write('{}\n'.format(totrowtempmincd))
        vtemp = vtemp + 1
        totrowtempminfd = rowcolor1 + rowtempd + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2a
        fo.write('{}\n'.format(totrowtempminfd))
        vtemp = vtemp + 1
        totrowtempavgcd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor + rowtempavg + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2
        fo.write('{}\n'.format(totrowtempavgcd))
        vtemp = vtemp + 1
        totrowtempavgfd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowcolor + rowtempavg + str(vtemp) + rowp + rowpathd + rowgraph + rowcolor + rowtempd2a
        fo.write('{}\n'.format(totrowtempavgfd))
        vtemp = vtemp + 1
        totrowwindscd = rowgoto + str(gotonumd + gotoplus - gotodelta) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathd + rowgraph + rowwindsd7
        fo.write('{}\n'.format(totrowwindscd))
        vtemp = vtemp + 1
        totrowwindsfd = rowgoto + str(gotonumd + gotoplus - gotodelta) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathd + rowgraph + rowwindsd6
        fo.write('{}\n'.format(totrowwindsfd))
        vtemp = vtemp + 1
        totrowrain1a = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathd + rowgraph + rowrain2
        fo.write('{}\n'.format(totrowrain1a))        
        vtemp = vtemp + 1
        totrowrain1a = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathd + rowgraph + rowrain2a
        fo.write('{}\n'.format(totrowrain1a))        
        vtemp = vtemp + 1
        gotodelta = 40
        totrowvis = rowvis + str(vtemp) + rowp + rowpathd + rowgraph + rowvis3
        fo.write('{}\n'.format(totrowvis))
        vtemp = vtemp + 1
        totrowvis = rowgoto + str(gotonumd + gotoplus + gotodelta) + rowgraph + rowvis + str(vtemp) + rowp + rowpathd + rowgraph + rowvis4
        fo.write('{}\n'.format(totrowvis))
        vtemp = vtemp + 1
        totrowhumd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowhumd + str(vtemp) + rowp + rowpathd + rowgraph + rowhumd2
        fo.write('{}\n'.format(totrowhumd))        
        vtemp = vtemp + 1
        totrowraind = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowpoprainwill + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowraind))
        vtemp = vtemp + 1
        totrowraind2 = rowpoprain + str(vtemp) + rowp + rowpathd + rowgraph + rowclo2
        fo.write('{}\n'.format(totrowraind2))
        vtemp = vtemp + 1
        totrowsnowd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowpopsnowwill + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowsnowd))
        vtemp = vtemp + 1
        gotoplus = gotoplus + gotodelta
        totrowsnowd2 =  rowpopsnow + str(vtemp) + rowp + rowpathd + rowgraph + rowclo2
        fo.write('{}\n'.format(totrowsnowd2))
        vtemp = vtemp + 1
        gotoplus = gotoplus - gotodelta
        totrowinfo = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowinfo + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowinfo))        
        vtemp = vtemp + 1
        #           the following row 21 is used to create the weather icons path
        # use next row if you want Weatherapi icons
        totico = pi + pi2 + pi3 + str(dicon[i]) + est + str(y) + virg + str(zd) + pfd
        y = y + 210
        # use next row if you want OpenWeather icons
        #totico = pi + pi2 + pi4 + str(dicon[i]) + (dicon[i][3:4]) + est + str(y) + virg + str(zd) + pfd
        #y = y + 133
        fo.write('{}\n'.format(totico))
        vtemp = vtemp + 2
        # row n. 22 (code) and multiples not present
        vtemp1 = 1 + (i * 2)
        vtemp2 = 2 + (i * 2)
        totrowuvid = rowuvi + str(vtemp2) + rowp + rowuvipathcolor1f + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1f + rowcolor
        fo.write('{}\n'.format(totrowuvid))
        vtemp = vtemp + 1
        totrowsunrised = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowsunrised + str(vtemp) + rowp + rowpathd +  rowgraph
        fo.write('{}\n'.format(totrowsunrised))
        vtemp = vtemp + 1
        totrowssd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowsunsetd + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowssd))
        vtemp = vtemp + 1
        totrowmrd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowmoonrised + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowmrd))
        vtemp = vtemp + 1
        totrowmoonsetd = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowmoonsetd + str(vtemp) + rowp + rowpathd +  rowgraph
        fo.write('{}\n'.format(totrowmoonsetd))
        vtemp = vtemp + 1
        totrowmoonphphaseud = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowmoonphphaseud + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowmoonphphaseud))
        vtemp = vtemp + 1
        totrowmoonphillud = rowgoto + str(gotonumd + gotoplus) + rowgraph + rowmoonphillud + str(vtemp) + rowp + rowpathd + rowgraph
        fo.write('{}\n'.format(totrowmoonphillud))
        vtemp = vtemp + 1
        gotonumd = 260
        gotoplus = 0
        zh = 210
        # if i == 2:
        #     fo.write('{}\n'.format(dashedline))
    fo.close()
    #                                  main HOURLY
    #                   set the paths for the FORECAST section
    pforecastcH = home + homename + ptemp + 'forecastconkyH.txt'
    y = 0
    counter = 0
    zh = 0
    zd = 300
    gotoplus = 100
    gotodelta = 30
    size = 83
    groupH = 35
    fo = open(pforecastcH, 'w')
    for i in range(firsth, grouph):
        if (hisday[i]) == 0:
            i2 = 1 + (groupH * i)
            # row n. 1 and multiples not present
            vtemp = i2 + 1
            #row n. 1 and multiples not present
            totrowdate = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowforecast + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowdate))
            vtemp = vtemp + 1
            totrowtempch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowtempd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempch))
            vtemp = vtemp + 1
            totrowtempfh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowtempd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowtempfh))
            vtemp = vtemp + 1
            totrowisdayh = hisday[i]
            fo.write('{}\n'.format(totrowisdayh))
            vtemp = vtemp + 1
            totrowinfoh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowcolor4 + rowinfo + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor
            fo.write('{}\n'.format(totrowinfoh))        
            vtemp = vtemp + 1
            #           the following row (7) is used to create the weather icons path
            # use next row if you want Weatherapi icons
            totico = pi + pi2 + pi3a + str(hicon[i]) + est + str(y) + virg + str(zh) + pfh
            # use next row if you want OpenWeather icons
            #totico = pi + pi2 + pi4 + str(dicon[i]) + (dicon[i][3:4]) + est + str(y) + virg + str(zh) + pfd
            #y = y + 133
            fo.write('{}\n'.format(totico))
            vtemp = vtemp + 2
            # row n. 8 (code) and multiples not present
            totrowwindsmh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd7
            fo.write('{}\n'.format(totrowwindsmh))        
            vtemp = vtemp + 1
            totrowwindskh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwindskh))        
            vtemp = vtemp + 1
            totrowwindsh4b = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd4b + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwindsh4b))        
            vtemp = vtemp + 1
            totrowwindsh4 = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd4 + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwindsh4))        
            vtemp = vtemp + 1
            totrowpresmh = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathh + rowgraph + rowpresd3
            fo.write('{}\n'.format(totrowpresmh))
            vtemp = vtemp + 1
            totrowpresih = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathh + rowgraph + rowpresd4
            fo.write('{}\n'.format(totrowpresih))
            vtemp = vtemp + 1
            totrowrain1a = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathh + rowgraph + rowrain2
            fo.write('{}\n'.format(totrowrain1a))        
            vtemp = vtemp + 1
            totrowrain1a = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathh + rowgraph + rowrain2a
            fo.write('{}\n'.format(totrowrain1a))        
            vtemp = vtemp + 1
            totrowhumh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowhumd + str(vtemp) + rowp + rowpathh + rowgraph + rowhumd2
            fo.write('{}\n'.format(totrowhumh))        
            vtemp = vtemp + 1
            totrowcloh = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowclo + str(vtemp) + rowp + rowpathh + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowcloh))
            vtemp = vtemp + 1
            totrowtempfch = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempfd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempfch))
            vtemp = vtemp + 1
            totrowtempffh = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempfd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowtempffh))
            vtemp = vtemp + 1
            totrowwcch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowwindsd3 + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowwcch))
            vtemp = vtemp + 1
            totrowwcch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowwindsd3 + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowwcch))
            vtemp = vtemp + 1
            totrowhich = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempheat + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowhich))
            vtemp = vtemp + 1
            totrowhifh = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempheat + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowhifh))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowdewch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1h + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1h + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowdewch))
            vtemp = vtemp + 1
            totrowdewfh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1h + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1h + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowdewfh))
            vtemp = vtemp + 1
            totrowwillrain = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowpoprainwill + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwillrain))        
            vtemp = vtemp + 1
            totrowpoph = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowpoprain + str(vtemp) + rowp + rowpathh + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowpoph))        
            vtemp = vtemp + 1
            totrowwillsnow = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowpopsnowwill + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwillsnow))        
            vtemp = vtemp + 1
            totrowpoph = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowpopsnow + str(vtemp) + rowp + rowpathh + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowpoph))        
            vtemp = vtemp + 1
            totrowvis = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowvis + str(vtemp) + rowp + rowpathh + rowgraph + rowvis3
            fo.write('{}\n'.format(totrowvis))
            vtemp = vtemp + 1
            totrowvis = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowvis + str(vtemp) + rowp + rowpathh + rowgraph + rowvis4
            fo.write('{}\n'.format(totrowvis))
            vtemp = vtemp + 1
            totrowwindgmh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd2 + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd7
            fo.write('{}\n'.format(totrowwindgmh))
            vtemp = vtemp + 1
            totrowwindgkh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd2 + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwindgkh))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowuvid = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1h + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1h + rowcolor
            fo.write('{}\n'.format(totrowuvid))
            if i == 5 or i == 11 or i == 17:
                zh = 0
            else:
                zh = zh + zhincrement
        elif (hisday[i]) != 0:
            i2 = 1 + (groupH * i)
            # row n. 1 and multiples not present
            vtemp = i2 + 1
            #row n. 1 and multiples not present
            totrowdate = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowforecast + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowdate))
            vtemp = vtemp + 1
            totrowtempch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowtempd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempch))
            vtemp = vtemp + 1
            totrowtempfh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowtempd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowtempfh))
            vtemp = vtemp + 1
            totrowisdayh = hisday[i]
            fo.write('{}\n'.format(totrowisdayh))
            vtemp = vtemp + 1
            totrowinfoh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowcolor4 + rowinfo + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor
            fo.write('{}\n'.format(totrowinfoh))        
            vtemp = vtemp + 1
            #           the following row (7) is used to create the weather icons path
            # use next row if you want Weatherapi icons
            totico = pi + pi2 + pi3a + str(hicon[i]) + est + str(y) + virg + str(zh) + pfh
            # use next row if you want OpenWeather icons
            #totico = pi + pi2 + pi4 + str(dicon[i]) + (dicon[i][3:4]) + est + str(y) + virg + str(zh) + pfd
            #y = y + 133
            fo.write('{}\n'.format(totico))
            vtemp = vtemp + 2
            # row n. 8 (code) and multiples not present
            totrowwindsmh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd7
            fo.write('{}\n'.format(totrowwindsmh))        
            vtemp = vtemp + 1
            totrowwindskh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwindskh))        
            vtemp = vtemp + 1
            totrowwindsh4b = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd4b + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwindsh4b))        
            vtemp = vtemp + 1
            totrowwindsh4 = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd4 + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwindsh4))        
            vtemp = vtemp + 1
            totrowpresmh = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathh + rowgraph + rowpresd3
            fo.write('{}\n'.format(totrowpresmh))
            vtemp = vtemp + 1
            totrowpresih = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowpresd + str(vtemp) + rowp + rowpathh + rowgraph + rowpresd4
            fo.write('{}\n'.format(totrowpresih))
            vtemp = vtemp + 1
            totrowrain1a = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathh + rowgraph + rowrain2
            fo.write('{}\n'.format(totrowrain1a))        
            vtemp = vtemp + 1
            totrowrain1a = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowrain1a + str(vtemp) + rowp + rowpathh + rowgraph + rowrain2a
            fo.write('{}\n'.format(totrowrain1a))        
            vtemp = vtemp + 1
            totrowhumh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowhumd + str(vtemp) + rowp + rowpathh + rowgraph + rowhumd2
            fo.write('{}\n'.format(totrowhumh))        
            vtemp = vtemp + 1
            totrowcloh = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowclo + str(vtemp) + rowp + rowpathh + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowcloh))
            vtemp = vtemp + 1
            totrowtempfch = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempfd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowtempfch))
            vtemp = vtemp + 1
            totrowtempffh = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempfd + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowtempffh))
            vtemp = vtemp + 1
            totrowwcch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowwindsd3 + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowwcch))
            vtemp = vtemp + 1
            totrowwcch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowwindsd3 + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowwcch))
            vtemp = vtemp + 1
            totrowhich = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempheat + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowhich))
            vtemp = vtemp + 1
            totrowhifh = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowtempheat + str(vtemp) + rowp + rowpathh + rowgraph + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowhifh))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowdewch = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1h + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1h + rowcolor + rowtempd2
            fo.write('{}\n'.format(totrowdewch))
            vtemp = vtemp + 1
            totrowdewfh = rowgoto + str(gotonumh + gotoplus * 0) + rowgraph + rowdew + str(vtemp2) + rowp + rowdewpathcolor1h + rowinfo + str(vtemp1) + rowp + rowdewpathvalue1h + rowcolor + rowtempd2a
            fo.write('{}\n'.format(totrowdewfh))
            vtemp = vtemp + 1
            totrowwillrain = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowpoprainwill + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwillrain))        
            vtemp = vtemp + 1
            totrowpoph = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowpoprain + str(vtemp) + rowp + rowpathh + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowpoph))        
            vtemp = vtemp + 1
            totrowwillsnow = rowgoto + str(gotonumh + gotoplus * 3) + rowgraph + rowpopsnowwill + str(vtemp) + rowp + rowpathh + rowgraph
            fo.write('{}\n'.format(totrowwillsnow))        
            vtemp = vtemp + 1
            totrowpoph = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowpopsnow + str(vtemp) + rowp + rowpathh + rowgraph + rowclo2
            fo.write('{}\n'.format(totrowpoph))        
            vtemp = vtemp + 1
            totrowvis = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowvis + str(vtemp) + rowp + rowpathh + rowgraph + rowvis3
            fo.write('{}\n'.format(totrowvis))
            vtemp = vtemp + 1
            totrowvis = rowgoto + str(gotonumh + gotoplus * 4) + rowgraph + rowvis + str(vtemp) + rowp + rowpathh + rowgraph + rowvis4
            fo.write('{}\n'.format(totrowvis))
            vtemp = vtemp + 1
            totrowwindgmh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd2 + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd7
            fo.write('{}\n'.format(totrowwindgmh))
            vtemp = vtemp + 1
            totrowwindgkh = rowgoto + str(gotonumh + gotoplus * 2) + rowgraph + rowwindsd2 + str(vtemp) + rowp + rowpathh + rowgraph + rowwindsd6
            fo.write('{}\n'.format(totrowwindgkh))
            vtemp = vtemp + 1
            vtemp1 = 1 + (i * 2)
            vtemp2 = 2 + (i * 2)
            totrowuvid = rowgoto + str(gotonumh + gotoplus * 1) + rowgraph + rowuvi + str(vtemp2) + rowp + rowuvipathcolor1h + rowinfo + str(vtemp1) + rowp + rowuvipathvalue1h + rowcolor
            fo.write('{}\n'.format(totrowuvid))
            if i == 5 or i == 11 or i == 17:
                zh = 0
            else:
                zh = zh + zhincrement
    fo.close()
    ################################ create CONKY statements for FORECAST HOURLY to copy into the conkyrc file
    vnblock = 33
    vconst = 0
    pconkycopy = home + homename + ptemp + 'conkycopyH.txt'
    fo = open(pconkycopy, 'w')
    for i in range(0, 24):
        v0 = "########################################### show " + str((i + 1)) + "° hour"
        fo.write('{}\n'.format(v0))
        v1 = "${execpi 900 sed -n '" + str(5 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}"
        fo.write('{}\n'.format(v1))
        v2 = "${execpi 900 sed -n '" + str(2 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(17 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(8 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(16 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(29 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}"
        fo.write('{}\n'.format(v2))
        v3 = "${execpi 900 sed -n '" + str(19 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(21 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(32 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(25 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(26 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}"
        fo.write('{}\n'.format(v3))
        v4 = "${execpi 900 sed -n '" + str(15 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(11 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(10 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(27 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(28 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}"
        fo.write('{}\n'.format(v4))
        v5 = "${execpi 900 sed -n '" + str(23 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(33 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(9 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(13 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(1 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}${execpi 900 sed -n '" + str(6 + vconst) + "p' $HOME/.conkyGITHUB/weather/Weatherapi/forecast/forecastconkyH.txt}"
        fo.write('{}\n'.format(v5))
        v8 = "${alignc}--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
        fo.write('{}\n'.format(v8))
        vconst = vconst + vnblock
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