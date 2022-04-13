from flask import  Flask,request,render_template
from config import app
from product_info import Product
productlist=[]

@app.route('/')
def ecomeLanding_page():
    return render_template('landing.html')
@app.route('/update')
def update_emp():
    a=productlist
    print(a)
    for b in a:
                print(b)
                # print('ssssssssssssssssss',type(b))
    #     for (i) in (b):
    #         if i and (b[i] == 101):  # If check key and value exact
                print(b['prodID'])
                # b['ProdPrice'] = '3333'
                # b['prodQty'] = '3'
    return render_template('update.html',mess='Update successfuly..........')

@app.route("/product/save",methods=['GET','POST'])
def save_update_product():
    # print(request.values)
    print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',productlist)

    message = ""
    if request.method=='POST':

        formadata=request.form
            # print('jjjjjjjjjjjjjj')
        Products=Product(pid=formadata.get('pid'),prnm=formadata.get('pnm'),
                pqty=formadata.get('pqty'),prc=formadata.get('pprc'),pven=formadata.get('pven'))

        productlist.append(Products)
        message='Product Added successfuly'
        # return render_template("")
    return render_template('add_update_product.html',message=message)
print('*'*10,productlist)
@app.route('/product/search')
def Show_all_product():
    print(productlist,'*'*30)
    return render_template('show.html',message=productlist)

d={}
d['dict1']={1:12,2:22,3:33}
d['dict1'][3]={}
d['dict1'][3][1]=23
d['dict1'][3][2]=23
d['dict1'][3][5]=21
print(d)

for i,v in d.items():
    print(v)
    for a,v in v.items():
        if type(v)==dict:
            for k,l in v.items():
                if k==5:
                    print(k,l,end=' ')
        # print(v)
    #     for  b in a:
    #         print('a')

