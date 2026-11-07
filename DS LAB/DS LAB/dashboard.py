import dash
from dash import dcc,html
app=dash.Dash(__name__)
app.layout=html.Div([
    html.H1("Dash Tutotrial"),
    dcc.Graph(
        id="example",
        figure={
            "data":[
                {
                    "x":[1,2,3,4,5],
                    "y":[5,4,7,4,8],
                    "type": "line",
                    "name":"Trucks"
                },
                {
                    "x":[1,2,3,4,5],
                    "y":[6,3,5,3,7],
                    "type": "bar",
                    "name":"ships"
                    
                }
            ],
            "layout":{
                "title":"Basic Dashboard"
            }
        }
    )
])
app.run(debug=True,port=8052)

