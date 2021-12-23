from django.http import HttpResponse
from django.shortcuts import render
import pandas_gbq
from google.oauth2 import service_account
from datetime import datetime
from .forms import PostForm

# Make sure you have installed pandas-gbq at first;
# You can use the other way to query BigQuery.
# please have a look at
# https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-nodejs
# To get your credential

credentials = service_account.Credentials.from_service_account_file("C:/Users/Yuzhao Pan/Desktop/Columbia/EECSE6893/bigdata_hw3/hw3_yp2578/hw3_yp2578/parabolic-grid-326800-aa68f163eb2c.json")



def hello(request):
    context = {}
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
    context['content1'] = 'hello world!'
    context['form'] = form
    return render(request, 'helloworld.html', context)


def dashboard(request):


    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "parabolic-grid-326800"

    SQL = "select time, ai, data, good, movie, spark from parabolic-grid-326800.wordcount.words limit 8"
    df = pandas_gbq.read_gbq(SQL)

    data = {}


    df_dict = df.to_dict('records')
    data_list = []
    for key in df_dict:
        data_dict = dict()
        data_dict["Time"] = key["time"].strftime(format="%H:%M")
        key = dict(key)
        key.pop("time")
        data_dict["count"] = key
        data_list.append(data_dict)
    data["data"] = data_list
    return render(request, 'dashboard.html', data)


def connection(request):
    pandas_gbq.context.credentials = credentials
    pandas_gbq.context.project = "parabolic-grid-326800"
    SQL1 = "SELECT node "\
           "FROM parabolic-grid-326800.data_103079215141.nodes"
    df1 = pandas_gbq.read_gbq(SQL1)

    SQL2 = "SELECT source, target "\
           "FROM parabolic-grid-326800.data_103079215141.edges"
    df2 = pandas_gbq.read_gbq(SQL2)

    data = {
        'n': list(df1.T.to_dict().values()),
        'e': list(df2.T.to_dict().values())
    }

    '''
        TODO: Finish the SQL to query the data, it should be limited to 8 rows. 
        Then process them to format below:
        Format of data:
        {'n': [xxx, xxx, xxx, xxx],
         'e': [{'source': xxx, 'target': xxx},
                {'source': xxx, 'target': xxx},
                ...
                ]
        }
    '''
    return render(request, 'connection.html', data)
