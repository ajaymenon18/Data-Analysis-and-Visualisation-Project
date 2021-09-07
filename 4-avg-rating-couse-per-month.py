import justpy as jp
import pandas
 
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates = ['Timestamp']) #telling the dataframe to treat the date as date(int) format and not string

#Grouping by Month Coursename and Ratings 
data['Month'] = data['Timestamp'].dt.strftime('%Y-%U')
mon_average_crs = data.groupby(['Month','Course Name'])['Rating'].count().unstack()

chart_def = """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average ratings of the courses'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}

"""

def app():
    wep = jp.QuasarPage()
    h1 = jp.QDiv(a = wep, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md ")
    p1 = jp.QDiv(a = wep, text = "These graphs represent course review analysis for 2 years ")

    hc = jp.HighCharts(a = wep, options = chart_def)
    hc.options.xAxis.categories = list(mon_average_crs.index)

    hc_data = [{"name":v1 , "data":[v2 for v2 in mon_average_crs[v1]]} for v1 in mon_average_crs.columns]
    hc.options.series = hc_data

    return wep
jp.justpy(app)