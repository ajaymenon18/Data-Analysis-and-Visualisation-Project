ABOUT THE PROJECT:

The given project uses Justpy and Highcharts to visualize data that is obtained from the Dataset about the certain set of courses in udemy and use several functionality available in the highcharts 

INSTALLING THE REQUIRED LIBRARIES:

To build this app we need to install a few Python libraries. 
justpy (library for building web apps and data visualization):
pandas (library for data analysis)
pytz (library for datetime calculations between timezones)
matplotlib (library for quick data visualization)
jupyter (library that enables a reach interactive Python shell)

METHODOLOGIES:

The dataset containing the reviews of the courses are obtained and is displayed using pandas in jupyter notebook 

![image](https://user-images.githubusercontent.com/10756648/132438960-9abe1d85-2bc8-46bb-9349-db430e05bd26.png)

TASKS

First task of the project is to display the average rating per day, we will be using the spline chart from the high-charts the source code is mentioned below 
#https://www.highcharts.com/docs/chart-and-series-types/spline-chart

![image](https://user-images.githubusercontent.com/10756648/132439533-4f8185b5-3fd2-4e17-8f82-5157cb3f141f.png)

Data is then grouped in terms of the day and ratings are calculated 

![image](https://user-images.githubusercontent.com/10756648/132440101-909a24a3-4855-4d64-98f0-665d3c9e7a59.png)

On running the code by using justpy and Highcharts we arrive at the following visualisation ( 1-avg-rating-per-day.py)

![average-rating-by-day (1)](https://user-images.githubusercontent.com/10756648/132440236-cdddc7e7-633a-44dd-986a-8db534a51738.png)

Next task is to display the average rating per week, similar code is used wherein instead of groupby using days, groupby by weeks
are used to the display the data. Spline charts are used 

![chart](https://user-images.githubusercontent.com/10756648/132441036-42abb7ac-c079-4f84-8b8b-18e34a2b60b3.png)

Average ratings per month 

![reviews-of-the-course-pe](https://user-images.githubusercontent.com/10756648/132443237-c7bc896e-63d5-4617-90f5-e646f29bd1bb.png)

Next we try to find the ratings of multiple courses with respect to months. Here we are using the areasline chart of the highcharts 
Grouping of the data 

![image](https://user-images.githubusercontent.com/10756648/132443872-2aa1a08a-b972-4474-a8f5-e26da73019f9.png)


Areaspline chart for ratings of multiple courses per month 
![image](https://user-images.githubusercontent.com/10756648/132443990-a42d5013-7587-419e-91de-60f3c8bf1655.png)

By changing the Areaspline to streamgraph we obtain the following visualisation 
![course-wise-ratings-with](https://user-images.githubusercontent.com/10756648/132444449-17023927-77be-4a05-b573-49e33b876114.png)

The final task is to represent the course and their number of ratings in terms of pie-chart. pie-chart functionality of the high charts are used 
![browser-market-shares-in](https://user-images.githubusercontent.com/10756648/132444782-3b69de87-c68f-4485-99fb-09c4ccd093b8.png)

Learnings from the application development 
Greater understanding about justpy, pandas, highchart codes and data visualization 



