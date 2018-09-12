import csv
from tkinter.filedialog import askdirectory
import ad_manager

def load_mapping(filename):
	flag = False
	mapping = {}
	with open(filename, "r") as csvfile:
		reader = csv.reader(csvfile, delimiter = ',', quotechar='"')	
		for row in reader:
			elem_0 = row[0]
			elem_1 = row[1]
			#validate data
			if '@' in elem_0:
				mapping[elem_1] = elem_0
			elif '@' in elem_1:
				mapping[elem_0] = elem_1
			else:
				#not a valid row, missing email address, log
				flag = True
		if flag:
			#alert user there was a problem row
			print("err")
	return mapping

def main():
	#get input for where the files should be
	path = askdirectory()
	csv_map = path+'/mappings.csv'
	#load mapping
	map = load_mapping(csv_map)
	print(map)
	#connect to facebook api
	access_token = "acc_tok"
	app_secret = "app_sec"
	app_id = "app_id"
	id = "id"
	admanager = ad_manager.AdManager(access_token, app_secret, app_id, id)
	#push new campaign info
	fields = [
		'name',
	]
	for name in map.keys():
		#found filtering method at 
		# https://stackoverflow.com/questions/42955081/how-to-get-specific-campaigns-by-name-from-facebook-marketing-api-using-python#comment75421532_44024943
		#unsure if this works, but only other obvious option I see is to cycle through all campaigns and match name fields
		#would be cumbersome for times when a fraction of campaigns require updating...
		params = {
			'filtering': [{'field':'campaign.name','operator':'CONTAIN','va‌​lue':name}]
		}
		campaign = admanager.get_campaign(fields, params)
		image_hash = admanager.add_image('/images/'+map[name])
		#TO-DO: get ad set
		#TO-DO: change targeting.publisher_platforms to include facebook (currently only has instagram)
		#		Note: no need to specify facebook_positions, default assumes all are valid
		#TO-DO: get info from current ad creative
		#TO-DO: create new ad creative with old info but new image
		#TO-DO: push new ad creative to be under the same ad set


if __name__ == "__main__":
	main()
