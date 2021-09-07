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
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    // Make sure connected countries have similar colors
    

    title: {
        floating: true,
        align: 'center',
        text: 'Course wise ratings with respect to the months '
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Comprehensive chart on the review of the course '
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Course Launched'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Python got popular'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [{
        name: "Finland",
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7, 7, 6, 12, 7, 9, 5, 5
        ]
    }, {
        name: "Slovenia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 3, 8
        ]
    }, {
        name: "Latvia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4
        ]
    }, {
        name: "Estonia",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 0
        ]
    }, {
        name: "Uzbekistan",
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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