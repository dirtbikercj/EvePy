import urllib.request, json


def return_item_data(item, region):
    global returned_ItemID
    global returned_RegionID
    typeid_lines = {}
    regionid_lines = {}
    with open('typeids.txt', 'r', encoding='utf-8') as f:  # Opens files with encoding
        for line in f:  # goes line to line
            s = line.strip().split("\t")  # removes white leading/trailing white space, splits at tab(\t)
            typeid_lines[s[0]] = int(s[1])  # assigns key pairs to data
            returned_ItemID = typeid_lines.get(item)  # Item to enter to find ID
        print('Item: ', item + '\n', 'ID: ', returned_ItemID)
    with open('regionID.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            ss = line.strip().split("\t")
            regionid_lines[ss[1]] = int(ss[0])
            returned_RegionID = regionid_lines.get(region)
        print("Region: " + str(region) + '\n' + "ID: " + str(returned_RegionID) + '\n')
    url1 = "https://market.fuzzwork.co.uk/aggregates/?region="
    url2 = str(returned_RegionID)
    url3 = "&types="
    url4 = str(returned_ItemID)
    response = urllib.request.urlopen(url1 + str(url2) + url3 + str(url4))
    data = json.loads(response.read())
    print(json.dumps(data, indent=4, sort_keys=True))
    return json.dumps(data, indent=4, sort_keys=True)


