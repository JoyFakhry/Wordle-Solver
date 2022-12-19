data = '''-a----          8/2/2022   4:28 PM         120449 PCARD0253 202208002, Servo City, $123.29.PDF
-a----         8/19/2022   5:15 PM          25017 PCARD0253 202208019, McMaster-Carr, $127.01.PDF
-a----         8/23/2022   4:44 PM          92142 PCARD0253 202208023, MISUMI, $68.29.PDF.pdf
-a----         8/30/2022   7:22 PM        1067453 PCARD0253 202208029, Metals Depot, $420.67.PDF
-a----          9/6/2022   9:31 AM          27175 PCARD0253 202209002, McMaster-Carr, $228.48.PDF
-a----          9/8/2022   9:51 AM          27702 PCARD0253 202209007, McMaster-Carr, $716.71.PDF
-a----         9/15/2022   9:10 AM          25650 PCARD0253 202209014, McMaster-Carr, $133.66.PDF
-a----         9/19/2022  12:51 PM          61732 PCARD0253 202209019, PACK EXPO International, $30.00.pdf
-a----         10/3/2022   1:44 PM          94530 PCARD0253 202209023, CitizenM, $1063.50.pdf
-a----         10/8/2022   7:04 PM          25409 PCARD0253 202210007, McMaster-Carr, $199.27.PDF
-a----        10/17/2022   9:45 AM          25576 PCARD0253 202210014, McMaster-Carr, $248.05.PDF
-a----        10/20/2022   9:16 AM          25473 PCARD0253 202210019, McMaster-Carr, $243.69.PDF
-a----        10/25/2022  10:10 AM          25118 PCARD0253 202210021, McMaster-Carr, $175.45.PDF
-a----         11/8/2022   1:35 PM          51887 PCARD0253 202211004, Global Industrial, $205.20.PDF
-a----         11/9/2022   9:04 AM          25518 PCARD0253 202211008, McMaster-Carr, $304.96.PDF
-a----        11/15/2022  11:14 AM          51663 PCARD0253 202211010, Global Industrial, $141.78.PDF
-a----        11/18/2022   9:32 AM          25504 PCARD0253 202211017, McMaster-Carr, $2328.37.PDF
-a----        11/25/2022   9:07 AM          25106 PCARD0253 202211022, McMaster-Carr, $161.46.PDF
-a----        11/25/2022   9:06 AM          27651 PCARD0253 202211022, McMaster-Carr, $275.00.PDF
-a----        11/28/2022   8:57 AM          25433 PCARD0253 202211023, McMaster-Carr, $236.00.PDF
-a----        11/29/2022  12:48 PM          27231 PCARD0253 202211028, McMaster-Carr, $338.66.PDF'''

lines = data.split('\n')

prices = []
for line in lines:
    price_str = line.split(' ')[-1]
    price = price_str.replace('$', '')
    price = price.replace('.PDF', '')
    price = price.replace('.pdf', '')
    prices.append(float(price))
print(sum(prices))