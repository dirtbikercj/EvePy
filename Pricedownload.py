import urllib.request, json


def return_item_data(item):
    global returned_ItemID
    typeid_lines = {}
    with open('typeids.txt', 'r', encoding='utf-8') as f:  # Opens files with encoding
        for line in f:  # goes line to line
            s = line.strip().split("\t")  # removes white leading/trailing white space, splits at tab(\t)
            typeid_lines[s[0]] = int(s[1])  # assigns key pairs to data
            returned_ItemID = typeid_lines.get(item)  # Item to enter to find ID
        print('Item: ', item + '\n', 'ID: ', returned_ItemID)
    url1 = "https://market.fuzzwork.co.uk/aggregates/?region=10000002&types="
    url2 = str(returned_ItemID)
    response = urllib.request.urlopen(url1 + str(url2))
    data = json.loads(response.read())
    print(data)


if __name__ == "__main__":
    item_to_find = input("Enter an item to find the ID: ")
    return_item_data(item_to_find)
