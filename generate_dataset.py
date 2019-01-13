import csv
from ota_infra import *


SETTINGS = {
	"NR_PROPERTIES":50,
	"NR_BOOKINGS": 500,
}

OTAS = ["B","A"]
PROPERTIES = ["property_" +str(i) for i in range(0,SETTINGS["NR_PROPERTIES"])]



OCCUPANCY = initiateOCCUPANCY(OTAS,PROPERTIES)
BOOKINGS = generateBookings(OCCUPANCY, OTAS, SETTINGS["NR_BOOKINGS"])

with open('bookings_'+str(SETTINGS["NR_BOOKINGS"])+'_per_'+str(SETTINGS["NR_PROPERTIES"])+'.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, BOOKINGS[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(BOOKINGS)
