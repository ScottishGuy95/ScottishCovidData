# ScottishCovidData
Makes use of the Scottish Goverment data and ckan API to get recent COVID-19 cases and death data

Data and API details can be found here - [Data](https://www.opendata.nhs.scot/dataset/covid-19-in-scotland/resource/e8454cf0-1152-4bcb-b9da-4343f625dfef?inner_span=True)
 and [API](https://docs.ckan.org/en/latest/maintaining/datastore.html)

An alternative and more detailed version of this program - [Repo Link](https://github.com/ScottishGuy95/ScottishCovidCases)

The API lists data on the following local authorities:
* Aberdeen City
* Aberdeenshire
* Angus
* Argyll & Bute
* City of Edinburgh
* Clackmannanshire
* Dumfries & Galloway
* Dundee City
* East Ayrshire
* East Dunbartonshire
* East Lothian
* East Renfrewshire
* Falkirk
* Fife
* Glasgow City
* Highland
* Inverclyde
* Midlothian
* Moray
* Na h-Eileanan Siar
* North Ayrshire
* North Lanarkshire
* Orkney Islands
* Perth & Kinross
* Renfrewshire
* Scottish Borders
* Shetland Islands
* South Ayrshire
* South Lanarkshire
* Stirling
* West Dunbartonshire
* West Lothian

## Usage
Requires Python3 installed

To download and use this script in Windows:
* Clone the repository
  * At the top of this page, select Green code button
  * If you have `git` installed, select the https option
  * Otherwise, download the Zip and extract

* For cloning options, open CMD, go to your required directory and enter the following:
    * `git clone https://github.com/ScottishGuy95/ScottishCovidData.git`

## Arguments
`python ScottishCovidData.py [argument]`

```
* -h        Returns the help message and exits
* -o        Returns an overview of all local authorities COVID-19 data
* -a AREA   Returns the COVID-19 data for the given local authority
```

## Examples
Get the help messages: `python ScottishCovidData -h`

Get the details of all local authorities: `python ScottishCovidData -o`

Get the details of a specific local authority: `python ScottishCovidData -a Moray`

If the local authority contains spaces or symbols (e.g. Dumfries & Galloway), use speech marks:
`python ScottishCovidData -a "Dumfries & Galloway"`