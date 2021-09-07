import justpy as jp
import pandas 
from datetime import datetime
from pytz import utc 

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

### Average ratings by week 

data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()




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
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
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
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wep = jp.QuasarPage()
    h1 = jp.QDiv(a = wep, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md ")
    p1 = jp.QDiv(a = wep, text = "These graphs represent course review analysis for 2 years ")

    hc = jp.HighCharts(a = wep, options = chart_def)
    hc.options.xAxis.categories = list(week_average.index)   # Here we are fixing the X axis of the plot 
    hc.options.series[0].data = list(week_average['Rating'])
    return wep
jp.justpy(app)