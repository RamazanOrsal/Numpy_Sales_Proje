import pandas as pd
import numpy as np

document = 'market_satis_veri.xlsx'  

try:
    sales_df = pd.read_csv('sales.csv')
    prices_df = pd.read_csv('prices.csv')

except FileNotFoundError:
    print("CSV file not found. Retrieving data from Excel...")
    sales_df =pd.read_excel(document, sheet_name='Satislar')
    prices_df = pd.read_excel(document, sheet_name='Fiyatlar')
    # CSV olarak kaydedelim:#
    sales_df.to_csv('sales.csv', index=False)
    prices_df.to_csv('prices.csv', index=False)

class SalesData:
    def __init__(self):
        self.productname = prices_df.columns[1:].tolist()   
        degerler = prices_df.iloc[0,1:].tolist()
        productprice = degerler = [int(x) for x in degerler]  
        self.pricesDict = dict(zip(self.productname, productprice))

        np_sales=np.array(sales_df)
        self.salesData=np_sales[:,1:]
        self.cirodayList=[]
        self.ciroDays()

    def ciro(self):
        ciro=0
        for i in range(0,len(self.productname)):
            product=self.productname[i]
            urun=sum(self.salesData[:,i])
            kazanc_urun=urun*self.pricesDict[product]
            print(f'This month you earned {kazanc_urun} from selling {product}.')
            ciro+=urun*self.pricesDict[product]
        print(f'Total:{ciro} ')

    def ciroDays(self):
        kazanclist=[]
        for i in range(0,len(self.salesData)):
            kazanc=0
            for j in range(0,len(self.productname)):
                product=self.productname[j]
                kazanc+=self.salesData[i,j]*self.pricesDict[product]
            kazanclist.append(kazanc)
        self.cirodayList=np.array(kazanclist)

    def displayciroDays(self):

        for i in range(0,len(self.salesData)):
            print(f'You earned {self.cirodayList[i]} liras {i+1}. day.')


    def displayminciroDay(self):
        minciro=self.cirodayList.min()
        minindex=self.cirodayList.argmin()
        print(f"You earned money at least on the {minindex+1}th day. That's {minciro} liras.")

    def displaymaxciroDay(self):
        maxciro=self.cirodayList.max()
        maxindex=self.cirodayList.argmax()
        print(f"You earned money at most on the {maxindex+1}th day. That's {maxciro} liras.")

    def displayaverageCiro(self):
        averageEarning=self.cirodayList.mean()
        print(f'Your average montly income is {averageEarning:.2f} liras.')

data=SalesData()



while True:
    select=input('1-Display ciro\n2-Display daily earnings\n3-Display the highest daily earnings\n4-Display the lowest daily earnings\n5-Display average daily earnings\n6-Exit\nSelect')

    if select=='6':
        break
    else:
        if select=='1':
            data.ciro()
        elif select=='2':
            data.displayciroDays()
        elif select=='3':
            data.displaymaxciroDay()
        elif select=='4':
            data.displayminciroDay()
        elif select=='5':
            data.displayaverageCiro()
        else:
            print('You have made a false click.')
        



