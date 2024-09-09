from flask import Flask,render_template,request
import pyodbc
app=Flask(__name__)
#Home Page
@approute('/')
def home():
    print('Loading Home page')
    return return_template('index.html')

#Food ordering home page
@app.route('/order',methods=['GET','POST'])  
def order():
    conn=pyodbc.connect('food_order.db')
    cursor=conn.cursor()
#Create a new table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                     (Name TEXT,Email TEXT,FoodItem TEXT,Quantity INTEGER,Address TEXT,Pincode TEXT)''')
    conn.commit()
if request.method=='POST':
        Name=request.form['username']
        Email=request.form['email']
        FoodItem=request.form['fooditem']
        Quantity=request.form['quantity']
        Address=request.form['address']
        Pincode=request.form['pincode']

#Insert order data
cursor.execute("Insert into orders(Name,Email,Fooditem,Quantity,Address,Pincode) VALUES (?,?,?,?,?,?)",
                    (Name,Email,FoodItem,Quantity,Address,Pincode))
conn.commit()
conn.close()
        print("Order has been successfully placed!")
        return render_template('order_success.html',username=Name,email=Email,fooditem=FoodItem,quantity=Quantity,address=Address,pincode=Pincode)
    
else:
    return render_template('oder_form.html')

if__name__=='__main__':
    app.run(debug=True)
    print("Service started")