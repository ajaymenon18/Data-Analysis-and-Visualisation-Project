import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates = ['Timestamp']) #telling the dataframe to treat the date as date(int) format and not string 

data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()


#code of highcharts javascripts code are pasted in the main code 
#https://www.highcharts.com/docs/chart-and-series-types/spline-chart : The copied code from the spline chart 


chart_def = """    
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the data sets collected'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Individual-dates'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Ratings'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average-Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}

"""
def app():
    wep = jp.QuasarPage()
    h1 = jp.QDiv(a = wep, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md ")
    p1 = jp.QDiv(a = wep, text = "These graphs represent course review analysis for 2 years ")
    hc = jp.HighCharts(a = wep, options = chart_def) # we are doing the highcharts 
    hc.options.title.text = "Average rating by day"
    
    hc.options.xAxis.categories = list(day_average.index) # creation of a new catgory part in the xAxis 

    # to make x = [3,4], y = [4,5 ] it into [[3,4],[6,7]]  we use the zip command 
    hc.options.series[0].data = list(day_average['Rating'])


    return wep

jp.justpy(app)