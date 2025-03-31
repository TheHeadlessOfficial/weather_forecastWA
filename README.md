# Conky Weather FORECAST (by Weatherapi)
 
A conky (with a script written in Python) that shows the FORECAST weather, using [Weatherapi API](https://www.weatherapi.com/) website.<br>

<br>
<br>

## **WIKI**<br>

Download the .zip file, extract the file, copy the file `.conkyrc_waforecast` and the folder `.conky` inside your Linux `home`.<br>
If your `home` is named *pippo*, copy inside *pippo* so you get: `/home/pippo/.conky` and `/home/pippo/.conkyrc_waforecast`.<br>
Go to `/home/YOURHOMENAME/.conky/weather/Weatherapi/forecast/` and open with a text editor the file `forecastwadata.py`, go to row 14 and 15 and type your latitude and your longitude, go to row 16 and type your city name, go to row 17 and write your APPID.<br>
If you don't know how to get your APPID, follow this video instructions: [APPID guide](https://youtu.be/FgRy3O12DKo?si=rF_3Zoh0NZox_qXP&t=103)<br>
<br>
In the `font` folder, you can find some fonts you need.<br>
The python script saves data in file so you can build your conky weather as you wish.<br>
Edit `.conkyrc_waforecast` to build your conky.<br>
The `.conkyrc_waforecast` file i attach, works.<br>
Run the file `.conkyrc_waforecast` from terminal (the first time you run this conky), so you can get possible errors. 




<br>
<br>

## Screenshot

![](https://github.com/TheHeadlessOfficial/weather_forecastWA/blob/main/.conky/docs/screenshot.png)<br>
This pic is related to the file `-daily.txt` (or `daily.txt`)  and it shows the next 2 forecast days.<br>
You can build the daily conky as you wish getting the data from one of the file mentioned above.<br>
One block of 32 rows (in the two file) is for 1 single forecast day, the first 32 rows block is for the current day.<br>
<br>
<br>
<br>
<br>

![](https://github.com/TheHeadlessOfficial/weather_forecastWA/blob/main/.conky/docs/screenshot2.png)<br>
This pic is related to the file `-hourly.txt` (or `hourly.txt`) and it shows the next 6 forecast hours.<br>
You can build the hourly conky as you wish getting the data from one of the two file mentioned above.<br>
One block of 36 rows (in the two file) is for 1 single forecast hour.<br>
<br>
<br>
<br>
<br>

---
[Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


