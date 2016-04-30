from flask import Flask, render_template, request, jsonify
import urllib2
# If you are using Python 3+, import urllib instead of urllib2
import json
import csv
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/tab2")
#def showTab():
#    return render_template("index.html#tabs-2")

#@app.route("/index2")
#def showIndex2():
#    return render_template("index-2.html")

#@app.route("/index3")
#def showIndex3():
#    return render_template("index-3.html")

#@app.route("/index4")
#def showIndex4():
#    return render_template("index-4.html")

#@app.route("/index5")
#def showIndex5():
#    return render_template("index-5.html")


@app.route("/ml1", methods=['POST'])
def ml():
    paramVal = request.form["param"]
    Reader = csv.reader(paramVal)
    Data = list(Reader)
   

    data =  {

        "Inputs": {
                "input1":
                {
                    "ColumnNames": ["date_time", "site_name", "posa_continent", "user_location_country", "user_location_region", "user_location_city", "orig_destination_distance", "user_id", "is_mobile", "is_package", "channel", "srch_ci", "srch_co", "srch_adults_cnt", "srch_children_cnt", "srch_rm_cnt", "srch_destination_id", "srch_destination_type_id", "is_booking", "cnt", "hotel_continent", "hotel_country", "hotel_market", "hotel_cluster"],
                    "Values":[ [
                    for row in Data:
                        str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), "0", "0", str(row[19]), str(row[20]), str(row[21]), "0" ], ]
                },        },
            "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))
    
    print(body)

    url = 'https://ussouthcentral.services.azureml.net/workspaces/dcd42eb6e203459181e33854f8a7a4f7/services/3e8f52e17e524c20973e732b1b2139c5/execute?api-version=2.0&details=true'
    api_key = 'QkRUT7WOn1qyxUaycXQ1YunxQnZ6YqAmiTwFIU5JykpY8MDCPgIMF/c7/SC8lHl7R3wJJhHMm1aODHiha/XvsA==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib2.Request(url, body, headers) 

    try:
        response = urllib2.urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result) 
        return result
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))  
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)