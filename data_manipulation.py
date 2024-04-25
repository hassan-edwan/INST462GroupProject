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
                 'Lamborghini':'Italy', 'Lotus':'UK', 'Scion':'Japan', 'Saturn':'USA', 'Suzuki':'Japan', 'Daewoo':'South Korea',
                 'Lucid':'USA', 'Spyker':'Netherlands', 'Fisker':'USA', 'DeLorean':'USA', 'Panoz':'USA', 'Saleen':'USA',
                 'Mercury':'USA', 'Polestar':'Sweden', 'Rivian':'USA', 'Hennessey':'USA', 'Koenigsegg':'Sweden',
                 'Rolls-Royce':'UK'}

def load_data(link):
    data = pd.read_csv(link)
    return data

def add_region_data(data):
    return data

def add_msrp_data(data):
    return data

def connect_to_api():
    return

def get_vehicle_msrp(make, model, year):
    return

## depreciation by mileage
## get msrp from KBB http://developer.kbb.com/#!/idws/99-Swagger