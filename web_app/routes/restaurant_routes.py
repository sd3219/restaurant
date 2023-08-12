
# this is the "web_app/routes/restaurant_routes.py" file ...

from flask import Blueprint, request, render_template, redirect, flash

from app.restaurant import fetch_restaurant_data

restaurant_routes = Blueprint("restaurant_routes", __name__)

@restaurant_routes.route("/restaurant/form")
def restaurant_form():
    print("RESTAURANT FORM...")
    return render_template("restaurant_form.html")

@restaurant_routes.route("/restaurant/dashboard", methods=["GET", "POST"])
def restaurant_dashboard():
    print("RESTAURANT DASHBOARD...")

    # for data sent via POST request, form inputs are in request.form:
    request_data = dict(request.form)
    print("FORM DATA:", request_data)

    c_zipcode = request_data.get("c_zipcode")

    restaurants = fetch_restaurant_data(c_zipcode=c_zipcode)

    zipcode_list = [ r["location"]["zip_code"] for r in restaurants ]

    if c_zipcode in zipcode_list:
        
        flash("Fetched Real-time Market Data!", "success")
        return render_template("restaurant_dashboard.html",
            restaurants=restaurants
        )
    
    else:
        print('OOPS')

        flash("Data Error. Please check your zipcode and try again!", "danger")
        return redirect("/restaurant/form")