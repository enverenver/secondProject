import xml.etree.ElementTree as ET
data = '''<persons>
    <users>
        <user x="1">
            <name>Chuck</name>
            <phone type="intl">
                +1 734 303 4456
            </phone>
            <email hide="yes"/>
        </user>
            <user x="2">
            <name>Jack</name>
            <phone type="intl">
                +1 777 333 5566
            </phone>
            <email hide="yes"/>
        </user>
    </users>
</persons>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print(lst)
print('User count: ', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Phone: ', item.find('phone').text)
    print('Attribute', item.get("x"))
