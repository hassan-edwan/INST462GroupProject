import pandas as pd

carCountryMap = {'Mazda':'Japan', 'Kia':'South Korea', 'Chevrolet':'USA', 'Ford':'USA', 'Acura':'Japan',
                 'Volkswagen':'Germany', 'Toyota':'Japan', 'Nissan':'Japan', 'Hyundai':'South Korea',
                 'Jeep':'USA', 'Honda':'Japan', 'Subaru':'Japan', 'BMW':'Germany', 'Mercedes-Benz':'Germany',
                 'Volvo':'Sweden', 'Audi':'Germany', 'Lexus':'Japan', 'Buick':'USA', 'GMC':'USA', 'Cadillac':'USA',
                 'Infiniti':'Japan', 'Porsche':'Germany', 'Land Rover':'UK', 'Jaguar':'UK', 'Lincoln':'USA',
                 'RAM':'USA', 'Mitsubishi':'Japan', 'MINI':'UK', 'FIAT':'Italy', 'Tesla':'USA', 'Bentley':'UK',
                 'Maserati':'Italy', 'Ferrari':'Italy', 'Alfa Romeo':'Italy', 'McLaren':'UK', 'Aston Martin':'UK',
                 'Dodge':'USA', 'Smart':'Germany', 'Genesis':'South Korea', 'Karma':'USA', 'Bugatti':'France',
                 'Chrysler':'USA', 'Eagle':'USA', 'Geo':'USA', 'Hummer':'USA', 'Isuzu':'Japan', 'Maybach':'Germany',
                 'International Scout':'USA', 'Oldsmobile':'USA', 'Plymouth':'USA', 'Pontiac':'USA', 'Saab':'Sweden',
                 'Lamborghini':'Italy', 'Lotus':'UK', 'Scion':'Japan', 'Saturn':'USA', 'Suzuki':'Japan',
                 'Lucid':'USA','Mercury':'USA', 'Polestar':'Sweden', 'Rivian':'USA','Rolls-Royce':'UK'}

def load_data(link):
    data = pd.read_csv(link, encoding='UTF-16', sep=',')
    return data

def add_region_data(data):
    data['Country'] = data['Brand'].map(carCountryMap)
    ##return data

def add_msrp_data(data):
    return data


def get_vehicle_msrp(make, model, year):
    return

def manipulation_for_heatmap():
    source = pd.read_csv('output.csv', encoding='UTF-8', sep=',')

    # Compute average prices for each status type
    average_prices_status = source.groupby('Status')['Price'].mean()
    # Compute average prices for each country and status type
    average_prices_country_status = source.groupby(['Country', 'Status'])['Price'].mean()

    # Compute percentage deviation for each country and status
    percentage_deviation = average_prices_country_status.to_frame()

    percentage_deviation['Percentage Deviation'] = percentage_deviation.apply(lambda x: ((x['Price'] - average_prices_status[x.name[1]])/(average_prices_status[x.name[1]])) * 100, axis=1)

    percentage_deviation.to_csv('pricebycountry.csv', index=True)

## depreciation by mileage
## get msrp from KBB http://developer.kbb.com/#!/idws/99-Swagger

data = load_data('car_sale_data.csv')
add_region_data(data)
data.to_csv('output.csv', index=False)