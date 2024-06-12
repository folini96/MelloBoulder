import folium
import json
from folium.plugins import LocateControl, MarkerCluster

marker_img = './stone.png'

boulder_list = {'1': [(46.21945980379365, 9.637749612424523), 'https://www.instagram.com/p/C5lBru_t6wz/', 'Zocca - Blocco 8 - Ayrton Senna 7A'],
                '2': [(46.21778359475178, 9.637242513463274), 'https://www.instagram.com/p/C5qHbRRNQgd/', 'Zocca - Blocco 20 - La Discarica 7B'],
                '3': [(46.22027038994832, 9.640804814541543), 'https://www.instagram.com/p/C5vhSI9tJpN/', 'La Collinetta - Blocco 2 - Lo Strapiombo 7A+'],
                '4': [(46.21734365932265, 9.637278930367646), 'https://www.instagram.com/p/C51YKgMtJV5/', 'Zocca - Blocco 18 - Filorera Hit 6B'],
                '5': [(46.21980722349366, 9.640989137048944), 'https://www.instagram.com/p/C56TrqytK2m/', 'Tetto di Filorera - Blocco 30 - Beppe Tallona 6C'],
                '6': [(46.21928103898559, 9.639222674606636), 'https://www.instagram.com/p/C5-5UX4NPlP/', 'Tarzan - Blocco 3 - Linea H 6C+'],
                '7': [(46.21918101169434, 9.639728665460543), 'https://www.instagram.com/p/C6EmbpetWpu/', 'Tarzan - Blocco 1 - Il sogno di Tarzan 7B'],
                '8': [(46.219168508270116, 9.63964734550188), 'https://www.instagram.com/p/C6J1zUcN3Em/', 'Tarzan - Blocco 1 - Linea G 6B'],
                '9': [(46.21934406490515, 9.640707829572289), 'https://www.instagram.com/p/C6O5jtlN4EM/', 'Tetto di Filorera - Blocco 2 - Linea A 6B'],
                '10': [(46.21914330183873, 9.639625930799902), 'https://www.instagram.com/p/C6ZO2faNmha/', 'Tarzan - Blocco 1 - Linea N 7A'],
                '11': [(46.221196283305204, 9.64024033384728), 'https://www.instagram.com/p/C6adgNsthHB/', 'Il Tendine dello Yeti - Blocco 1 - Shiba 7B'],
                '12': [(46.21925049670988, 9.640947607819216), 'https://www.instagram.com/p/C6n43WTN76J/', 'Tetto di Filorera - Blocco 3 - Linea A 7B'],
                '13': [(46.21926348746294, 9.64095565444605), 'https://www.instagram.com/p/C69Z5IIti_V/', 'Tetto di Filorera - Blocco 3 - L\'Arco del Tetto 6C+'],
                '14': [(46.221698735924704, 9.634388310969028), 'https://www.instagram.com/p/C7KKIOStyhE/', 'Zocca Superiore - Blocco 1 - Katana San 6B'],
                '15': [(46.22132227721143, 9.640056979892453), 'https://www.instagram.com/p/C7PWHPCNk4p/', 'Tendine dello Yeti - Blocco 3 - Linea T 7A'],
                '16': [(46.22113455233579, 9.634393664441712), 'https://www.instagram.com/p/C7Uryt9tiV9/', 'Zocca Superiore - Blocco 3 - Linea B 6C'],
                '17': [(46.2319818109148, 9.635366109621582), 'https://www.instagram.com/p/C7b3m0jNUFK/', 'Campeggio - Blocco 5 - Linea M 6C'],
                '18': [(46.22322825558623, 9.635099172546335), 'https://www.instagram.com/p/C7heVq4NEtq/', 'Scivolo - Blocco 1 - Camarillo per Tutti 7A+'],
                '19': [(46.22146858783223, 9.634227367487158), 'https://www.instagram.com/p/C8FNkXot3R5/', 'Zocca Superiore - Blocco 2 - L\'Opinione dell\'Opilione /B'],
                '20': [(46.22143536663251, 9.64005812258591), 'https://www.instagram.com/p/C79H96VNPa4/', 'Tendine dello Yeti - Blocco 4 - Linea F 6A+'],
                '21': [(46.22088442559476, 9.634511782977246), 'https://www.instagram.com/p/C7o8qQxNaTt/', 'Zocca Superiore - Blocco 7 - Linea F 6B']}

cluster = MarkerCluster(options={'showCoverageOnHover': False,
                                        'zoomToBoundsOnClick': True,
                                        'spiderfyOnMaxZoom': False,
                                        'disableClusteringAtZoom': 14})

MyMap = folium.Map(location=[46.2276363923169, 9.635030700689214], tiles='OpenStreetMap', zoom_start=13,
                   min_zoom=11, max_zoom=19, control_scale=True)

# Create markers for each pub in the pub dictionary
for boulder, details in boulder_list.items():
    id = boulder
    coordinates = details[0]
    insta_post = details[1]
    title = details[2]

    custom_icon = folium.CustomIcon(marker_img, icon_size=(35, 35), popup_anchor=(0, -22))


    pub_html = folium.Html(
        f"""
        <p style="text-align: center;"><span style="font-family: Didot, serif; font-size: 21px;">{title}</span></p>
        <iframe src={insta_post}embed width="400" height="400" frameborder="0" scrolling="auto" allowtransparency="true"></iframe>
    """, script=True)

    popup = folium.Popup(pub_html, max_width=700)
    custom_marker = folium.Marker(location=coordinates, tooltip=title, icon=custom_icon, popup=popup)

    custom_marker.add_to(cluster)

cluster.add_to(MyMap)

LocateControl(auto_start=False).add_to(MyMap)

# Define webpage title html and add to script.
tab_title = """<title>MiraMonkeys boulders</title>"""
MyMap.get_root().html.add_child(folium.Element(tab_title))

# Save the map
MyMap.save('index.html')