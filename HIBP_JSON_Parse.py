import json
import datetime

timestamp = datetime.datetime.now()
timestamp =datetime.datetime.strftime(timestamp, "%Y-%m-%d")

# loads JSON file
j = open("./hibp.json", 'r')
j = j.read()
json_file = json.loads(j)
json_data = json_file['BreachSearchResults']

outputfile = f"{timestamp}_Parsed_HIBP_Output.csv"
print("Parsing JSON file...")
with open(outputfile,'w') as output_file:
    # writes headers
    output_file.write("email,breached_site,breach_date,report_date,pw_check,breached_data,description\n")
    # reads JSON file
    for row in json_data:
        alias = row['Alias']
        dname = row ['DomainName']
        total_breaches = []
        breaches = row['Breaches']
        for data in breaches:
            name = data['Name']
            bdate = data['BreachDate']
            bdata = data['DataClasses']
            rdata = data['AddedDate']
            # first converts str into a Datetime object then converts to just m/d/y. omiits the hour timestamp
                                                    #    2019-01-16T21:46:07Z
            rdata = datetime.datetime.strptime(rdata, "%Y-%m-%dT%H:%M:%SZ")
            rdata = datetime.datetime.strftime(rdata,"%m/%d/%Y")
            # removes commas in value to not mess up CSV
            desc = data['Description']
            desc = desc.replace(",", " ")
            desc = f"\'{desc}\'"
            # Checks if passwords were in the breach
            pw_check = "Passwords" in bdata or "passwords" in bdata
            if pw_check == True:
                pw_check_data = "y"
            else:
                pw_check_data = "n"
            # wrap in quotes to not mess with csv
            bdata = ",".join(bdata)
            bdata = f"\"{bdata}\""
            # makes a rough email name
            gu_name = f'{alias}@{dname}'
            output_file.write(f"{gu_name},{name},{bdate},{rdata},{pw_check_data},{bdata},{desc}\n")

print("Done!")