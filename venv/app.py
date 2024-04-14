from flask import Flask,render_template,request,Response
import requests as rq
import qrcode 
from PIL import Image
import uuid as uu
import io
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("login.html")

@app.route("/getTicket",methods = ["POST"])
def getTicket():
    username = request.form["name"]
    email = request.form["email"]
    Uni = request.form["Uni"]
    print(username,email,Uni)
    url = "https://api.sheety.co/9a4b27f9e0cadde1d7ef325454108d37/signupForm/emails"
    data = {
        "email":{
        "name":username,
        "email":email,
        "un":str(uu.uuid3(uu.NAMESPACE_DNS,email)).split("-")[4],
        "university":Uni,
        }

    }
    r = rq.post(url=url,json=data)
    print(r.json())
    if r.status_code==200:
        img_buffer = io.BytesIO()
        qr = qrcode.QRCode(version=1, box_size=10, border=4)  # Adjust parameters as needed
        qr.add_data(data["email"]["un"])
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(img_buffer, format="PNG")

        # Return QR code image data directly
        return Response(img_buffer.getvalue(), mimetype="image/png")
    else:
        return 

if __name__ == "__main__":
    app.run(debug=True)