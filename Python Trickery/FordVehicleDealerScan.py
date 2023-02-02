from bs4 import BeautifulSoup 
import requests
import re
import csv

Ford = input("What vehicle do you want to search for? ")

# Create a CSV file to store the data
with open('DealerDataFord.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Dealer Name', 'Dealer Location']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    
    page_num = 1
    while True:
        url = f"https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=ford&maximum_distance=all&mileage_max=&page_size=20&seller_type[]=dealership&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip=48640&page={page_num}"

        page = requests.get(url).text 
        doc = BeautifulSoup(page, "html.parser")

        # Find the dealer name and location
        dealers = doc.find_all(class_="vehicle-dealer")
        for dealer in dealers:
            dealer_name = dealer.find(class_="dealer-name").text
            
            
            # Write the data to the CSV file
            writer.writerow({'Dealer Name': dealer_name})

        # Check if there is a next page
        next_page = doc.find(class_="sds-button sds-button--secondary sds-pagination__control")
        if next_page:
            page_num += 1
        else:
            break
