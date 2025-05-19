import folium
import json
from folium.plugins import LocateControl, MarkerCluster

marker_img = './stone.png'

boulder_list = [
    {'sector_name': 'Ponte del Baffo',
     'boulders': [
         {
             'name': 'Blocco 1 - Bad Ass',
             'coords': (46.1937559, 9.6252532),
             'lines': [
                 {'name': 'Studio Line 7B', 'link': 'https://www.instagram.com/p/DJHwetSt06b/'}
             ]
         },
     ]
     },
    {'sector_name': 'Tetto Di Filorera',
     'boulders': [
         {
             'name': 'Blocco 2 - Il Profeta',
             'coords': (46.21934406490515, 9.640707829572289),
             'lines': [
                 {'name': 'Linea A 6B', 'link': 'https://www.instagram.com/p/C6O5jtlN4EM/'},
                 {'name': 'Baywatch 6C', 'link': 'https://www.instagram.com/p/DA1VbYvNso2/'},
                 {'name': 'Linea F 4C', 'link': 'https://www.instagram.com/p/DGv4_AAN8mY/'}
             ]
         },
         {
             'name': 'Blocco 3 - Tetto Di Filorera',
             'coords': (46.21926348746294, 9.64095565444605),
             'lines': [
                 {'name': 'Linea A 7B', 'link': 'https://www.instagram.com/p/C6n43WTN76J/'},
                 {'name': 'L\'Arco Del Tetto 6C+', 'link': 'https://www.instagram.com/p/C69Z5IIti_V/'}
             ]
         },
         {
             'name': 'Blocco 30 - Ultimi Raggi',
             'coords': (46.21980722349366, 9.640989137048944),
             'lines': [
                 {'name': 'Beppe Tallona 6C', 'link': 'https://www.instagram.com/p/C56TrqytK2m/'}
             ]
         },
     ]
     },
    {'sector_name': 'La Collinetta',
     'boulders': [
         {
             'name': 'Blocco 2 - Lo Strapiombo',
             'coords': (46.22027038994832, 9.640804814541543),
             'lines': [
                 {'name': 'Lo Strapiombo 7A+', 'link': 'https://www.instagram.com/p/C5vhSI9tJpN/'}
             ]
         },
         {
             'name': 'Blocco 4 - Alta Pressione',
             'coords': (46.220613, 9.641112),
             'lines': [
                 {'name': 'Alta Pressione 6C+', 'link': 'https://www.instagram.com/p/DGK8HLHtlh8/'}
             ]
         },
         {
             'name': 'Blocco 6',
             'coords': (46.220745, 9.641010),
             'lines': [
                 {'name': 'Totem 6B+', 'link': 'https://www.instagram.com/p/DHrH8NLNVD8/'}
             ]
         },
         {
             'name': 'Blocco 14',
             'coords': (46.220834, 9.641114),
             'lines': [
                 {'name': 'Linea E 6A+', 'link': 'https://www.instagram.com/p/DGXcvTYNcWU/'}
             ]
         },
         {
             'name': 'Blocco 15 - Quarzo Liquido',
             'coords': (46.2211150, 9.6410640),
             'lines': [
                 {'name': 'Il Mangiacaccole 7B', 'link': 'https://www.instagram.com/p/DF3QA8PNyYP/'}
             ]
         },
         {
             'name': 'Blocco 23',
             'coords': (46.220417, 9.641098),
             'lines': [
                 {'name': 'Magica Miky 7A', 'link': 'https://www.instagram.com/p/DH8_4ZIt3AN/'}
             ]
         },
         {
             'name': 'Blocco 36',
             'coords': (46.2208881, 9.6414142),
             'lines': [
                 {'name': 'Il Bisteccone 7A+', 'link': 'https://www.instagram.com/p/DGQ6YBotPbz/'}
             ]
         },
     ]
     },
    {'sector_name': 'Il Tendine Dello Yeti',
     'boulders': [
         {
             'name': 'Blocco 1',
             'coords': (46.221196283305204, 9.64024033384728),
             'lines': [
                 {'name': 'Shiba 7B', 'link': 'https://www.instagram.com/p/C6adgNsthHB/'},
                 {'name': 'Linea B 6B', 'link': 'https://www.instagram.com/p/DCHDuy-vYh4/'}
             ]
         },
         {
             'name': 'Blocco 3 - Tendine Dello Yeti',
             'coords': (46.22132227721143, 9.640056979892453),
             'lines': [
                 {'name': 'Andrea Si È Perso Diretto 7B', 'link': 'https://www.instagram.com/p/C_TZAGWNc2d/'},
                 {'name': 'Tendine Sinistro 6C+', 'link': 'https://www.instagram.com/p/DFBAAm6tbj7/'},
                 {'name': 'Linea N 7A', 'link': 'https://www.instagram.com/p/C_OUNY7t0Ec/'},
                 {'name': 'Linea T 7A', 'link': 'https://www.instagram.com/p/C7PWHPCNk4p/'},
             ]
         },
         {
             'name': 'Blocco 4',
             'coords': (46.22143536663251, 9.64005812258591),
             'lines': [
                 {'name': 'Titanic 6C+', 'link': 'https://www.instagram.com/p/DFGIjTntlmR/'},
                 {'name': 'Linea F 6A+', 'link': 'https://www.instagram.com/p/C79H96VNPa4/'}
             ]
         },
     ]
     },
    {'sector_name': 'Vermuth Strisciut',
     'boulders': [
         {
             'name': 'Blocco 2 - Il Quadricipite',
             'coords': (46.2223497, 9.6388547),
             'lines': [
                 {'name': 'Linea D 6C', 'link': 'https://www.instagram.com/p/DCmx-fdN6io/'},
             ]
         },
         {
             'name': 'Blocco 8 - L\'Elicottero',
             'coords': (46.2229712, 9.6386877),
             'lines': [
                 {'name': 'Billy Idol 7A+', 'link': 'https://www.instagram.com/p/DHZBIWyNdcO/'},
             ]
         },
     ]
     },
    {'sector_name': 'Visido Alta',
     'boulders': [
         {
             'name': 'Blocco 30',
             'coords': (46.221783, 9.643058),
             'lines': [
                 {'name': 'La Sottile Linea Gialla 7C', 'link': 'https://www.instagram.com/p/DChgBclN6Xl/'},
             ]
         },
         {
             'name': 'Blocco non in guida',
             'coords': (46.222299, 9.643131),
             'lines': [
                 {'name': 'Linea A 7A+', 'link': 'https://www.instagram.com/p/DDAXKtIN3FM/'},
             ]
         }
     ]
     },
    {'sector_name': 'Tarzan',
     'boulders': [
         {
             'name': 'Blocco 1 - Il Sogno Di Tarzan',
             'coords': (46.21918101169434, 9.639728665460543),
             'lines': [
                 {'name': 'Il Sogno Di Tarzan 7B', 'link': 'https://www.instagram.com/p/C6EmbpetWpu/'},
                 {'name': 'Tarzan e Cita stand 7B+', 'link': 'https://www.instagram.com/p/DFqS26gtfvF/'},
                 {'name': 'Linea G 6B', 'link': 'https://www.instagram.com/p/C6J1zUcN3Em/'},
                 {'name': 'Spalla 6C+', 'link': 'https://www.instagram.com/p/DJUbA3VNJ5O/'},
                 {'name': 'Linea N 7A', 'link': 'https://www.instagram.com/p/C6ZO2faNmha/'},
             ]
         },
         {
             'name': 'Blocco 3 - Masso Dell\'Entalpia',
             'coords': (46.21928103898559, 9.639222674606636),
             'lines': [
                 {'name': 'Linea H 6C+', 'link': 'https://www.instagram.com/p/DCZjcrUNefL/'},
             ]
         }
     ]
     },
    {'sector_name': 'Zocca',
     'boulders': [
         {
             'name': 'Blocco 1 - Mezon Creek',
             'coords': (46.2196095, 9.6377637),
             'lines': [
                 {'name': 'Tacchine Assassine 6C', 'link': 'https://www.instagram.com/p/DE2KWj9NzlX/'}
             ]
         },
         {
             'name': 'Blocco 8 - Black Bloc',
             'coords': (46.219296, 9.638271),
             'lines': [
                 {'name': 'Ayrton Senna 7A', 'link': 'https://www.instagram.com/p/C5lBru_t6wz/'}
             ]
         },
         {
             'name': 'Blocco 18 - Filorera Hit',
             'coords': (46.21734365932265, 9.637278930367646),
             'lines': [
                 {'name': 'Filorera Hit 6B', 'link': 'https://www.instagram.com/p/C51YKgMtJV5/'}
             ]
         },
         {
             'name': 'Blocco 20 - La Discarica Privata',
             'coords': (46.21778359475178, 9.637242513463274),
             'lines': [
                 {'name': 'La Discarica 7B', 'link': 'https://www.instagram.com/p/C5qHbRRNQgd/'}
             ]
         }
     ]
     },
    {'sector_name': 'Zocca Superiore',
     'boulders': [
         {
             'name': 'Blocco 1 - Castello',
             'coords': (46.221698735924704, 9.634388310969028),
             'lines': [
                 {'name': 'La Lama Nella Roccia 5C', 'link': 'https://www.instagram.com/p/DGlZNmsNlef/'},
                 {'name': 'Katana San 6B', 'link': 'https://www.instagram.com/p/C7KKIOStyhE/'}
             ]
         },
         {
             'name': 'Blocco 2',
             'coords': (46.22146858783223, 9.634227367487158),
             'lines': [
                 {'name': 'L\'Opinione dell\'Opilione 7B', 'link': 'https://www.instagram.com/p/C7o8qQxNaTt/'}
             ]
         },
         {
             'name': 'Blocco 3 - Sass Do Boff',
             'coords': (46.22113455233579, 9.634393664441712),
             'lines': [
                 {'name': 'Linea B 6C', 'link': 'https://www.instagram.com/p/C7Uryt9tiV9/'}
             ]
         },
         {
             'name': 'Blocco 5',
             'coords': (46.221020, 9.634374),
             'lines': [
                 {'name': 'Linea B 6B+', 'link': 'https://www.instagram.com/p/C-Iz9MXtVpx/'}
             ]
         },
         {
             'name': 'Blocco 7',
             'coords': (46.22088442559476, 9.634511782977246),
             'lines': [
                 {'name': 'Linea F 6B', 'link': 'https://www.instagram.com/p/C8FNkXot3R5/'}
             ]
         },
         {
             'name': 'Blocco 9',
             'coords': (46.219281, 9.635498),
             'lines': [
                 {'name': 'Spigolo Kima 6C', 'link': 'https://www.instagram.com/p/DGaUiYXNSIM/'}
             ]
         },
     ]
     },
    {'sector_name': 'Scivolo',
     'boulders': [
         {
             'name': 'Blocco 1 - Camarillo Brillo',
             'coords': (46.22322825558623, 9.635099172546335),
             'lines': [
                 {'name': 'Camarillo Per Tutti 7A+', 'link': 'https://www.instagram.com/p/C7heVq4NEtq/'}
             ]
         },
         {
             'name': 'Blocco 2 - Masso delle Crepe',
             'coords': (46.2241479, 9.6347016),
             'lines': [
                 {'name': 'Cadi e Muori 7A+', 'link': 'https://www.instagram.com/p/DIGYLCWt3RN/'}
             ]
         },
         {
             'name': 'Blocco 12',
             'coords': (46.2244246251822, 9.635044787851378),
             'lines': [
                 {'name': 'Heart of Stone 7B', 'link': 'https://www.instagram.com/p/DHHHzSQNTVD/'},
                 {'name': 'El Corazon 6C', 'link': 'https://www.instagram.com/p/DGgOCwPNLgk/'}
             ]
         },
         {
             'name': 'Blocco 16 . Masso del Sassista',
             'coords': (46.22431240609788, 9.634684884576668),
             'lines': [
                 {'name': 'Linea D', 'link': 'https://www.instagram.com/p/DHBEJZgN5og/'}
             ]
         },
     ]
     },
    {'sector_name': 'Remenno',
     'boulders': [
         {
             'name': 'Blocco 6 - Masso di Goldrake',
             'coords': (46.2259697, 9.6354205),
             'lines': [
                 {'name': 'Goldrake 6C', 'link': 'https://www.instagram.com/p/DBCGPAQtF96/'}
             ]
         },
         {
             'name': 'Blocco 8 - Masso Erculeo',
             'coords': (46.2257025, 9.6357095),
             'lines': [
                 {'name': 'Linea C 6B', 'link': 'https://www.instagram.com/p/DA88ggZNusE/'}
             ]
         },
         {
             'name': 'Blocco 21 - Sasso Piatto',
             'coords': (46.224967, 9.635729),
             'lines': [
                 {'name': 'Bidone 6C+', 'link': 'https://www.instagram.com/p/DG01FHWtQqs/'}
             ]
         },
     ]
     },
    {'sector_name': 'La Mota',
     'boulders': [
         {
             'name': 'Blocco 7 - Masso del Diavolo',
             'coords': (46.235770, 9.629098),
             'lines': [
                 {'name': 'Diavolo 7A', 'link': 'https://www.instagram.com/p/DAanG21tPMs/'}
             ]
         },
         {
             'name': 'Blocco 14 - Sasso Gioele',
             'coords': (46.235944, 9.629286),
             'lines': [
                 {'name': 'Melloblocco Version 7A', 'link': 'https://www.instagram.com/p/C__OwsiNXOL/'}
             ]
         },
         {
             'name': 'Blocco 15 - Sasso Ketty',
             'coords': (46.235920, 9.628916),
             'lines': [
                 {'name': 'Linea A 6B', 'link': 'https://www.instagram.com/p/DBInTqatu0N/'}
             ]
         },
         {
             'name': 'Blocco 22 - Sasso Alice',
             'coords': (46.236193, 9.629382),
             'lines': [
                 {'name': 'Linea A 6A', 'link': 'https://www.instagram.com/p/C-uon0Dttd3/'},
                 {'name': 'Linea C 6B', 'link': 'https://www.instagram.com/p/C_nNk5FNnyr/'}
             ]
         },
         {
             'name': 'Blocco 33',
             'coords': (46.236768, 9.628728),
             'lines': [
                 {'name': 'La Zappa E Il Martello 6B', 'link': 'https://www.instagram.com/p/C--lW4rtTPr/'}
             ]
         },
         {
             'name': 'Blocco 35',
             'coords': (46.237113, 9.628980),
             'lines': [
                 {'name': 'Tanti Auguri 7B', 'link': 'https://www.instagram.com/p/C-VUsVbNR-Y/'}
             ]
         },
         {
             'name': 'Blocco 36',
             'coords': (46.237384, 9.628953),
             'lines': [
                 {'name': 'Linea C 6B+', 'link': 'https://www.instagram.com/p/C-p6aurNUnk/'}
             ]
         },
     ]
     },
    {'sector_name': 'Campeggio',
     'boulders': [
         {
             'name': 'Blocco 5 - Masso del Campeggio',
             'coords': (46.231176, 9.635417),
             'lines': [
                 {'name': 'Linea M 6C', 'link': 'https://www.instagram.com/p/C7b3m0jNUFK/'}
             ]
         },
         {
             'name': 'Blocco 12 - Bidon Jack',
             'coords': (46.231109, 9.636936),
             'lines': [
                 {'name': 'Linea B 6B', 'link': 'https://www.instagram.com/p/C9crU7XNYVv/'}
             ]
         },
     ]
     },
    {'sector_name': 'Campo Sportivo',
     'boulders': [
         {
             'name': 'Blocco 24',
             'coords': (46.237176, 9.634913),
             'lines': [
                 {'name': 'Linea E 6B', 'link': 'https://www.instagram.com/p/C_tPncstCmX/'}
             ]
         },
         {
             'name': 'Blocco 36 - Pietra delle Meditazioni',
             'coords': (46.2367992, 9.6340458),
             'lines': [
                 {'name': 'Dj Set 7A', 'link': 'https://www.instagram.com/p/DHgFUPqtvP0/'},
                 {'name': 'Onice Nera 6C+', 'link': 'https://www.instagram.com/p/DHlvq2tNzb8/'}
             ]
         }
     ]
     },
    {'sector_name': 'Belvedere',
     'boulders': [
         {
             'name': 'Blocco 1 - Little Karma',
             'coords': (46.24074676167137, 9.600611281316468),
             'lines': [
                 {'name': 'Little Karma 8A', 'link': 'https://www.instagram.com/p/DJPmt9Dtbug/'},
             ]
         },
         {
             'name': 'Blocco 3 - Oscurità',
             'coords': (46.240353, 9.600340),
             'lines': [
                 {'name': 'Oscurità 7A', 'link': 'https://www.instagram.com/p/C8kJ2bLNVBz/'},
                 {'name': 'Oscurità sit 7B+', 'link': 'https://www.instagram.com/p/DCPbflLNcWZ/'}
             ]
         },
     ]
     },
    {'sector_name': 'Ersaf',
     'boulders': [
         {
             'name': 'Blocco 1 - Lo Scrigno Del Bosco',
             'coords': (46.2439287, 9.5954898),
             'lines': [
                 {'name': 'Spigolo Rudi 6B', 'link': 'https://www.instagram.com/p/C8grc8CNnUH/'}
             ]
         },
         {
             'name': 'Blocco 10',
             'coords': (46.243162, 9.595707),
             'lines': [
                 {'name': 'La Balance 7a', 'link': 'https://www.instagram.com/p/DAVsldrtOZN/'}
             ]
         },
         {
             'name': 'Blocco 12 - Lady Red',
             'coords': (46.242931, 9.595807),
             'lines': [
                 {'name': 'Lady Red 7B', 'link': 'https://www.instagram.com/p/DJmjWiFtr7v/'}
             ]
         },
         {
             'name': 'Blocco 13 - Sono Fuori dal Tunnel',
             'coords': (46.242730, 9.595731),
             'lines': [
                 {'name': 'La Danza della Morte 7B', 'link': 'https://www.instagram.com/p/DJZfn1UtESv/'}
             ]
         },
         {
             'name': 'Blocco 15',
             'coords': (46.242778, 9.595152),
             'lines': [
                 {'name': 'Pancia Rudi 7A', 'link': 'https://www.instagram.com/p/C9KvH8htq9K/'}
             ]
         },
         {
             'name': 'Blocco 24 - Profiterol Di Ghughi',
             'coords': (46.244804, 9.593878),
             'lines': [
                 {'name': 'Linea B 5C', 'link': 'https://www.instagram.com/p/C-lGRUyNUIK/'}
             ]
         },
         {
             'name': 'Blocco 27 - Mellolista',
             'coords': (46.244856, 9.594275),
             'lines': [
                 {'name': 'The Yellow Bird 7A+', 'link': 'https://www.instagram.com/p/C9iHPt-tr_o/'}
             ]
         },
         {
             'name': 'Blocco 28 - Lucilla',
             'coords': (46.245149, 9.594242),
             'lines': [
                 {'name': 'Linea B 7A', 'link': 'https://www.instagram.com/p/C8PqzysNa2c/'}
             ]
         },
         {
             'name': 'Blocco 29 - La Sfinge',
             'coords': (46.245434, 9.592856),
             'lines': [
                 {'name': 'Linea A 7A', 'link': 'https://www.instagram.com/p/C-5tnx7tuWv/'}
             ]
         },
     ]
     },
    {'sector_name': 'Proprietà privata',
     'boulders': [
         {
             'name': 'Blocco 3 - Proprietà Privata',
             'coords': (46.249504, 9.641525),
             'lines': [
                 {'name': 'Il Lancio 7A', 'link': 'https://www.instagram.com/p/DAjHEW8NUQN/'}
             ]
         },
         {
             'name': 'Blocco 8 - Masso del Torrente',
             'coords': (46.2501274, 9.6418541),
             'lines': [
                 {'name': 'Linea D 6A+', 'link': 'https://www.instagram.com/p/DAoVFfvNquP/'}
             ]
         },
         {
             'name': 'Blocco 9 - Muro Dei Granchi',
             'coords': (46.250127, 9.642155),
             'lines': [
                 {'name': 'Linea D 6B', 'link': 'https://www.instagram.com/p/C9wI1qOtWzb/'},
                 {'name': 'Idrojet 6A+', 'link': 'https://www.instagram.com/p/C8mokmXN3Mb/'}
             ]
         }
     ]
     },
    {'sector_name': 'Cascina Piana',
     'boulders': [
         {
             'name': 'Blocco 4 - La Carrozza di Rame',
             'coords': (46.2551449, 9.6546663),
             'lines': [
                 {'name': 'Spigolo della Carrozza di Rame 7A', 'link': 'https://www.instagram.com/p/DIB94d4NF_z/'}
             ]
         },
     ]
     },
]

cluster = MarkerCluster(options={'showCoverageOnHover': False,
                                 'zoomToBoundsOnClick': True,
                                 'spiderfyOnMaxZoom': False,
                                 'disableClusteringAtZoom': 14})

MyMap = folium.Map(location=[46.2276363923169, 9.635030700689214], tiles='OpenStreetMap', zoom_start=13,
                   min_zoom=11, max_zoom=19, control_scale=True)

search_entries = []

# Create markers for each pub in the pub dictionary
for sector in boulder_list:
    for boulder in sector["boulders"]:
        sector_name = sector["sector_name"]
        coordinates = boulder["coords"]

        lines_html = ""
        for line in boulder["lines"]:
            lines_html = lines_html + f""" <div> <a href="{line["link"]}"> {line["name"]} </a> </div>"""
            search_entries.append({
                'line': line['name'],
                'link': line['link'],
                'boulder': boulder['name'],
                'sector': sector['sector_name'],
            })
        pub_html = folium.Html(
            f""" <p style="text-align: center;"><span style="font-family: Didot, serif; font-size: 21px;">{boulder["name"]}</span></p>{lines_html}""",
            script=True)

        custom_icon = folium.CustomIcon(marker_img, icon_size=(35, 35), popup_anchor=(0, -22))

        popup = folium.Popup(pub_html, max_width=700)
        custom_marker = folium.Marker(location=coordinates, tooltip=boulder["name"], icon=custom_icon, popup=popup)

        custom_marker.add_to(cluster)

cluster.add_to(MyMap)

LocateControl(auto_start=False).add_to(MyMap)

# Define webpage title html and add to script.
tab_title = """<title>MiraMonkeys boulders</title>"""
MyMap.get_root().html.add_child(folium.Element(tab_title))

map_html = MyMap.get_root().render()

search_json = json.dumps(search_entries).replace("</", "<\\/")  # prevent </script> break

search_script = f"""
<script>
const searchData = {search_json};

const input = document.createElement('input');
input.type = 'text';
input.placeholder = 'Cerca un blocco, una linea, o un settore';
input.style = 'position:absolute;top:10px;left:50px;z-index:1000;width:300px;padding:6px;';
document.body.appendChild(input);

const results = document.createElement('div');
results.style = 'position:absolute;top:40px;left:50px;z-index:1000;width:300px;background:white;border:1px solid #ccc;max-height:300px;overflow-y:auto;font-family:sans-serif;font-size:14px;';
results.hidden = true;
document.body.appendChild(results);

input.addEventListener('input', () => {{
    const query = input.value.toLowerCase();
    results.innerHTML = '';
    if (!query) {{
        results.hidden = true;
        return;
    }}

    const matches = searchData.filter(item =>
        item.line.toLowerCase().includes(query) ||
        item.boulder.toLowerCase().includes(query) ||
        item.sector.toLowerCase().includes(query)
    );

    matches.forEach(item => {{
        const div = document.createElement('div');
        div.innerHTML = `<strong>${{item.boulder}} - ${{item.line}}</strong> (${{item.sector}})`;
        div.style = 'padding:6px;cursor:pointer;border-bottom:1px solid #eee;';
        div.addEventListener('click', () => {{
            window.open(item.link, '_blank');
        }});
        results.appendChild(div);
    }});

    results.hidden = matches.length === 0;
}});

input.addEventListener('blur', () => {{
    setTimeout(() => {{
        results.hidden = true;
    }}, 150);
}});

input.addEventListener('focus', () => {{
   if (input.value) {{
        results.hidden = false;
   }}
}});
</script>
"""

final_html = map_html.replace("</body>", f"{search_script}</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)