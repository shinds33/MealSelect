import random
import webbrowser
import PySimpleGUI as sg

mexican = ['https://rb.gy/pcvbh5', 'https://www.chuys.com/menu']
tacos = ['https://rb.gy/npkjxo', 'https://rb.gy/z09fln']
pizza = ['https://rb.gy/173nm9', 'http://www.piesmtx.com/#menu', 'https://rb.gy/jdal1n',
         'https://littlecaesars.com/en-us/']
asian = ['http://www.rollinbowl.com/Menu', 'https://www.kobesmtx.com/menu', 'https://umamiumami.com/#intro',
         'https://rb.gy/pw6jqf']
burger = ['https://rb.gy/01vkdd', 'https://pterrys.com/menu', 'https://www.fiveguys.com/menu',
          'https://hatcreekburgers.com/menu/']
sandwich = ['https://www.schlotzskys.com/menu', 'https://thundercloud.com/main-menu/',
            'http://alvinordssanmarcos.com/#menu']
chicken = ['https://rb.gy/fv7mto', 'https://rb.gy/69bt5b', 'https://rb.gy/dlooiu',
           'https://rb.gy/8wgp2b', 'https://chickene.com/menu/', 'https://www.popeyes.com/explore-menu',
           'http://www.bushschicken.com/menu/', 'https://rb.gy/wepzco']
seafood = ['https://rb.gy/qvyde1', 'https://rb.gy/ispfgk']
names = ['Mexican', 'Tacos', 'Pizza', 'Asian', 'Burger', 'Sandwich', 'Chicken', 'Seafood']


sg.theme('DarkBlue')

layout = [
    [sg.Text('Enter a choice from the list: ')],
    [sg.Text('In the mood for.. ', size=(15, 1)), sg.InputText()],
    [sg.Listbox(names,
    default_values=None,
    select_mode=None,
    change_submits=False,
    enable_events=False,
    bind_return_key=False,
    size=(15, 15),
    disabled=False,
    auto_size_text=None,
    font=None,
    no_scrollbar=False,
    background_color=None,
    text_color=None,
    key=None,
    k=None,
    pad=None,
    tooltip=None,
    right_click_menu=None,
    visible=True,
    metadata=None)],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Where we boutta eat at?', layout)
event, values = window.read()
window.close()

user_in = values[0]
print('\nYou have picked ' + user_in)

if user_in == 'Mexican' or user_in == 'mexican':
    cur_choice = random.choice(mexican)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'tacos' or user_in == 'Tacos':
    cur_choice = random.choice(tacos)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'pizza' or user_in == 'Pizza':
    cur_choice = random.choice(pizza)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'asian' or user_in == 'Asian':
    cur_choice = random.choice(asian)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'Burger' or user_in == 'burger':
    cur_choice = random.choice(burger)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'sandwich' or user_in == 'Sandwich':
    cur_choice = random.choice(sandwich)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'chicken' or user_in == 'Chicken':
    cur_choice = random.choice(chicken)
    webbrowser.open(cur_choice, new=1)
elif user_in == 'seafood' or user_in == 'Seafood':
    cur_choice = random.choice(seafood)
    webbrowser.open(cur_choice, new=1)
else:
    print('You need to choose from the list!')

















