import pygame
import pygame_gui
import csv
import random
import gpiozero


#initalize pygame
pygame.init()
pygame.display.set_caption('Its_Alive')
clock = pygame.time.Clock()
is_running = True


#set up the main window surface and gui manager
screen = pygame.display.set_mode((1920, 1080))
manager = pygame_gui.UIManager((1920, 1080), 'theme.json')

#background
background = pygame.image.load("stars.jpg").convert()



#LABEL: a short text that describes how parameters are changing
#TEXT: longer desription that is more content-focused
#BOX: a rectangle that holds text

#title
title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((20,20), (1880, 130)),
    text="What does it take to be habitable in space? Use the sliders to imagine a world, then use the SEARCH button to find similar planets in our universe.",
    manager=manager,
    object_id='title_label')


#input sliders
sizeslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((20, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
distslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((480, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
denslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((960, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)
tempslide = pygame_gui.elements.ui_horizontal_slider.UIHorizontalSlider(
    ((1440, 200), (450, 30)), 0, (0,3), manager, None,None, 'slider', None, 1, 1)

#parameter text: stored here for more concise main function

size_param_label = '<p>The sheer size of a planet has a huge effect on the type of planet it will become. The term <i>planet</i> only applies when it has enough mass and gravity to form itself into a round shape.</p>'

small_param_label = 'Worlds that are less than .5x the radius of the Earth.'
small_param_text = 'The smaller something is, the more challenging it is to find, meaning there are few very small worlds we know of outside the Solar System. Small planets are typically rocky but may struggle to keep their cores molten, causing them to lose their magnetic field and protection from radiation.</p>'

medium_param_label = 'Worlds that are about .5x to 1.5x the size of Earth.'
medium_param_text = 'Earth is fairly large for a terrestrial planet and fairly small in the context of all planets. Earth&apos;s size may have played an important role in becoming habitable. Too small, and it cools off; too large, and it becomes gas-dominated.' 

big_param_label = 'Worlds between 1.5x and 2x times the radius of the Earth.'
big_param_text = 'Many terrestrial exoplanets have been found in the range slightly bighger than Earth. These planets have been termed &quot;super-Earths&quot; and are often good candidates for Earth-like conditions.'

giant_param_label = 'Worlds over 2x times the radius of the Earth.'
giant_param_text = 'Planets of this size typically made of more gas than they are rock. The term &quot;mini-Neptune&quot; has been used to describe these planets, but new research shows super-Earths may just be mini-Neptunes that lost their atmospheres.'

distance_param_label = 'Here, distance is a comparison between '

close_param_label= 'Worlds that are too close to their star'
close_param_text = '<p>Being too close to the host star means being constantly pummeled with energy in the form of light, heat, and radiation. Worlds may also have their rotation disrupted or even be squished by the gravity of their star.</p>' 

inner_param_label = 'Worlds within their star&apos;s Habitable Zone.'
inner_param_text = '<p> Venus, Earth, and Mars are all technically within the Habitable Zone of the sun, but even variations within the Zone can severely change a planet. Our neighbors are an example of how distance is one of the most notable factors in a planet&apos;s climate, other factors such as size can play just as large a role. Even a tiny change in distance will have big effects on the length of a year &mdash; Mars is not relatively far from us, but its year is almost twice as long.</p>'

outer_param_label = 'Worlds outside their star&apos;s Habitable Zone'
outer_param_text = 'Despite this range being too cold for life, some moons orbiting the Solar System&apos;s Gas Giants are theorized to have conditions for specialized life.'

distant_param_label = 'Worlds far from their star'
distant_param_text = '<p>Current methods for finding worlds beyond our Solar System require using the light or gravity of the host star, making it very difficult to find planets even as far away as Jupiter is to our Sun. Even in our own Solar System, studying distant worlds is challenging &mdash; the New Horizons probe to Pluto took 9 years to fly by. However, since many astronomers believe important ingredients for life could be found far from the sun, making the challenge worthwhile.</p>'

dens_param_label = '<p>Using a combination of observations and physics formulas, scientists are able to make estimates of mass and radius. Comparing the two can estimate density, which tells us about the potential composition of the world.</p>'

rocky_param_label = 'A world mostly made of solid materials.'
rocky_param_text = '<p>These worlds are solid all the way through, with very little liquid or gaseous elements. Though astronomers use the term <i>rocky</i>, most of these worlds contain metals in their core, especially iron. Rocky worlds are also more common nearer to their host stars. </p>'

earthy_param_label = 'A world containing liquids and gases in addition to solid metals and rocks.'
earthy_param_text = '<p> The Earth is about 33% Iron by mass. The rest is a combination of other metals, rocks, minerals, water, and gases. Most of this iron is found in the superheated core of the planet, which drives volcanic activity and keeps the planet &quot;alive&quot;. Astronomers believe a similar core and metal composition to Earth could be one indicator of potential habitability.</p>'

watery_param_label = 'A world that contains a solid core, but also a significant global ocean.'
watery_param_text = '<p>Though the surface of the Earth is 70% water, it accounts for less than 1% of Earth&apos;s total mass. Some worlds are estimated to be 20-40% water by total mass, with giant oceans stretching down for miles, heated by volcanic vents at the core</p>'

neptune_param_label = 'A world with a thick, puffy atmosphere'
neptune_param_text = '<p>Worlds tend to fit one of two categories: a small world that is mostly rock, or a very large world mostly made of gas. Gas Giants, like Neptune, do not have a solid surface, but a slushy core where gases begin to turn solid and liquid under high pressure. Mini-Neptunes are an emerging study of in-between worlds that seem to be rocky cores with giant, puffy atmospheres. </p>'

temp_param_label = 'The temperature of a world may seem straightforward, but depends on many interconnected factors. The atmosphere, presence of water, composition, distance, age, and more can all play a role. We often take the weather for granted on Earth, but the ability to form clouds and cycle water through the air is a key factor in maintaining a liveable temperature. The study of temperature in astrobiology is also linked to the study of <i>extremophiles</i> on Earth, or organisms that thrive in extreme environments.'

freeze_param_label = 'Worlds too cold for liquid water'
freeze_param_text = '<p> Outer Space nearly reaches what we believe to be the coldest possible temperature. Stars can provide energy, but only an atmosphere can trap it once the world is not in direct sunlight.Still, some organisms on Earth are able to survive extreme cold. Astronomers have also shown that important organic molecules can be found frozen in ice.</p>'

temperate_param_label = 'Worlds where liquid water could exist'
temperate_param_text = 'The general temperatures for Earth-like habitability are between -15 and 122 degrees Celsius. This encompasses the range where water is liquid. Currently, exoplanet temperatures are estimations, but several worlds show promise of Earth-like temperatures.'

hot_param_label = 'Worlds too hot for liquid water'
hot_param_text = 'Many worlds have features that raise their temperature dramatically, such as close orbits, volcanic activity, or heat-trapping atmospheres. Maintaining a temperate climate is difficult, and worlds that become too hot sometimes pass the point of no return.'

wild_param_label = 'A world where internal factors influence the temperature in unique ways'
wild_param_text = 'Many worlds can only be measured by one estimated temperature. In comparison, Earth is convered in temperature variations where extremophiles adapt and thrive. Some worlds, most notably Jupiter&apos;s moon Europa, are hypothesized to have features such as hydrothermal vents that would create a habitable zone inside a seemingly uninhabitable planet.'


#parameter graphics

check = pygame.image.load('graphics/check.png').convert()
uncheck = pygame.image.load('graphics/uncheck.png').convert()

small_graphic = pygame.image.load('graphics/small.png').convert()
medium_graphic = pygame.image.load('graphics/medium.png').convert()
big_graphic = pygame.image.load('graphics/large.png').convert()
giant_graphic = pygame.image.load('graphics/giant.png').convert()

close_graphic = pygame.image.load('graphics/close.png').convert()
inner_graphic = pygame.image.load('graphics/inner.png').convert()
outer_graphic = pygame.image.load('graphics/outer.png').convert()
distant_graphic = pygame.image.load('graphics/distant.png').convert()

rocky_graphic = pygame.image.load('graphics/rocky.png').convert()
earthy_graphic = pygame.image.load('graphics/earthy.png').convert()
watery_graphic = pygame.image.load('graphics/watery.png').convert()
neptune_graphic = pygame.image.load('graphics/neptune.png').convert()

freeze_graphic = pygame.image.load('graphics/freeze.png').convert()
temperate_graphic = pygame.image.load('graphics/temp.png').convert()
hot_graphic = pygame.image.load('graphics/hot.png').convert()
wild_graphic = pygame.image.load('graphics/wild.png').convert()

#parameter icons

size_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((20, 100), (100, 100)),
    image_surface = small_graphic,
    manager = manager,
    visible = 1)

dist_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((480, 100), (100,100)),
    image_surface = close_graphic,
    manager = manager,
    visible = 1)

dens_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((960, 100), (100,100)),
    image_surface = rocky_graphic,
    manager = manager,
    visible = 1)

temp_icon = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((1440, 100), (100,100)),
    image_surface = freeze_graphic,
    manager = manager,
    visible = 1)


#planet images box: images themselves stored within the csv data

blank_surface  = pygame.Surface((600,600))

planet_image_box = pygame_gui.elements.ui_image.UIImage(
    relative_rect = pygame.rect.Rect((120, 400), (600, 600)),
    image_surface = blank_surface,
    manager = manager,
    visible = 1)
                                
paramlabelbox = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = "param label",
    relative_rect = pygame.rect.Rect((220, 500), (400,400)),
    manager= manager,
    visible = 1,
    object_id = 'paramlabelbox')

imagecaption = pygame_gui.elements.ui_label.UILabel(
    relative_rect = pygame.rect.Rect((120, 500), (600, 50)),
    text = " ",
    manager = manager)

#planet info UI boxes

planet_name_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet name',
    relative_rect=pygame.Rect((960, 350), (940, 150)),
    manager=manager)

planet_fact_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet text',
    relative_rect = pygame.Rect((960, 540), (940,360)),
    manager=manager)

planet_size_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet size',
    relative_rect = pygame.Rect((200, 250), (240, 40)),
    manager = manager)

planet_dist_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet dist',
    relative_rect = pygame.Rect((680, 250), (240, 40)),
    manager = manager)

planet_dens_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text='planet dens',
    relative_rect = pygame.Rect((1150, 250), (240, 40)),
    manager = manager)

planet_temp_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = 'planet temp',
    relative_rect = pygame.Rect((1660, 250), (240, 40)),
    manager=manager)
    

    
    
#this is labeling text that doesnt change
Size_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((200, 100), (150, 50)),
    text="SIZE",
    manager=manager,
    object_id='main_label')

Distance_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((700, 100), (150, 50)),
    text="DISTANCE",
    manager=manager,
    object_id='main_label')

Density_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((1100, 100), (150, 50)),
    text="DENSITY",
    manager=manager,
    object_id='main_label')

Temp_UILabel = pygame_gui.elements.ui_label.UILabel(
    relative_rect=pygame.rect.Rect((1600, 100), (150, 50)),
    text="TEMPERATURE",
    manager=manager,
    object_id='main_label')

#these labels boxes change based on what the user has chosen
size_label_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text = 'Size',
    relative_rect = pygame.rect.Rect((200, 150), (240, 40)),
    manager = manager,
    object_id='param_label')

dist_label_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Distance',
    relative_rect = pygame.rect.Rect((680, 150), (240, 40)),
    manager= manager,
    object_id='param_label')

dens_label_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Density',
    relative_rect = pygame.rect.Rect((1150, 150), (240, 40)),
    manager=manager,
    object_id='param_label')

temp_label_box = pygame_gui.elements.ui_text_box.UITextBox(
    html_text= 'Temp',
    relative_rect = pygame.rect.Rect((1660, 150), (240, 40)),
    manager=manager,
    object_id='param_label')


#gpio functions

def sizefunc(device):
    if device.pin.number == 4:
        print('0')
        sizeslide.set_current_value(0)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('size_param_label')
        size_label_box.clear()
        size_label_box.set_text('Small')
        planet_name_box.clear()
        planet_name_box.set_text(small_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(small_param_text)
        size_icon.set_image(small_graphic)
    elif device.pin.number == 17:
        sizeslide.set_current_value(1)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('size_param_label')
        size_label_box.clear()
        size_label_box.set_text('Medium')
        planet_name_box.clear()
        planet_name_box.set_text(medium_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(medium_param_text)
        size_icon.set_image(medium_graphic)
    elif device.pin.number == 27:
        sizeslide.set_current_value(2)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('size_param_label')
        size_label_box.clear()
        size_label_box.set_text('Big')
        planet_name_box.clear()
        planet_name_box.set_text(giant_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(giant_param_text)
        size_icon.set_image(big_graphic)
    elif device.pin.number == 22:
        sizeslide.set_current_value(3)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('size_param_label')
        size_label_box.clear()
        size_label_box.set_text('Giant')
        planet_name_box.clear()
        planet_name_box.set_text(giant_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(giant_param_text)
        size_icon.set_image(giant_graphic)
        
def distfunc(device):
    if device.pin.number == 5:
        distslide.set_current_value(0)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dist_param_label')
        dist_label_box.clear()
        dist_label_box.set_text('Close')
        planet_name_box.clear()
        planet_name_box.set_text(close_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(close_param_text)
        dist_icon.set_image(close_graphic)
    elif device.pin.number == 6:
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dist_param_label')
        distslide.set_current_value(1)
        dist_label_box.clear()
        dist_label_box.set_text('Inner')
        planet_name_box.clear()
        planet_name_box.set_text(close_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(close_param_text)
        dist_icon.set_image(inner_graphic)
    elif device.pin.number == 13:
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dist_param_label')
        distslide.set_current_value(2)
        dist_label_box.clear()
        dist_label_box.set_text('Outer')
        planet_name_box.clear()
        planet_name_box.set_text(outer_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(outer_param_text)
        dist_icon.set_image(outer_graphic)
    elif device.pin.number == 19:
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dist_param_label')
        distslide.set_current_value(3)
        dist_label_box.clear()
        dist_label_box.set_text('Distant')
        planet_name_box.clear()
        planet_name_box.set_text(distant_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(distant_param_text)
        dist_icon.set_image(distant_graphic)
        
def densfunc(device):
    if device.pin.number == 18:
        denslide.set_current_value(0)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dens_param_label')
        dens_label_box.clear()
        dens_label_box.set_text('100% Rocky')
        planet_name_box.clear()
        planet_name_box.set_text(rocky_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(rocky_param_text)
        dens_icon.set_image(rocky_graphic)
    elif device.pin.number == 23:
        denslide.set_current_value(1)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dens_param_label')
        dens_label_box.clear()
        dens_label_box.set_text('Similar to Earth')
        planet_name_box.clear()
        planet_name_box.set_text(earthy_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(earthy_param_text)
        dens_icon.set_image(earthy_graphic)
    elif device.pin.number == 24:
        denslide.set_current_value(2)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dens_param_label')
        dens_label_box.clear()
        dens_label_box.set_text('Water World')
        planet_name_box.clear()
        planet_name_box.set_text(watery_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(watery_param_text)
        dens_icon.set_image(watery_graphic)
    elif device.pin.number == 25:
        denslide.set_current_value(3)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('dens_param_label')
        dens_label_box.clear()
        dens_label_box.set_text('Sub-Neptune')
        planet_name_box.clear()
        planet_name_box.set_text(neptune_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(neptune_param_text)
        dens_icon.set_image(neptune_graphic)
        
def tempfunc(device):
    if device.pin.number == 12:
        tempslide.set_current_value(0)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('temp_param_label')
        temp_label_box.clear()
        temp_label_box.set_text('Freezing')
        planet_name_box.clear()
        planet_name_box.set_text(freeze_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(freeze_param_text)
        temp_icon.set_image(freeze_graphic)
    elif device.pin.number == 16:
        tempslide.set_current_value(1)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('temp_param_label')
        temp_label_box.clear()
        temp_label_box.set_text('Temperate')
        planet_name_box.clear()
        planet_name_box.set_text(temperate_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(temperate_param_text)
        temp_icon.set_image(temperate_graphic)
    elif device.pin.number == 20:
        tempslide.set_current_value(2)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('temp_param_label')
        temp_label_box.clear()
        temp_label_box.set_text('Scalding')
        planet_name_box.clear()
        planet_name_box.set_text(hot_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(hot_param_text)
        temp_icon.set_image(hot_graphic)
    elif device.pin.number == 21:
        tempslide.set_current_value(3)
        paramlabelbox.show()
        paramlabelbox.clear()
        paramlabelbox.set_text('temp_param_label')
        temp_label_box.clear()
        temp_label_box.set_text('Wildcard')
        planet_name_box.clear()
        planet_name_box.set_text(wild_param_label)
        planet_fact_box.clear()
        planet_fact_box.set_text(wild_param_text)
        temp_icon.set_image(wild_graphic)
        
#defining the switches of the gpio
size_0 = gpiozero.DigitalInputDevice(4)
size_1 = gpiozero.DigitalInputDevice(17)
size_2 = gpiozero.DigitalInputDevice(27)
size_3 = gpiozero.DigitalInputDevice(22)

dist_0 = gpiozero.DigitalInputDevice(5)
dist_1 = gpiozero.DigitalInputDevice(6)
dist_2 = gpiozero.DigitalInputDevice(13)
dist_3 = gpiozero.DigitalInputDevice(19)

dens_0 = gpiozero.DigitalInputDevice(18)
dens_1 = gpiozero.DigitalInputDevice(23)
dens_2 = gpiozero.DigitalInputDevice(24)
dens_3 = gpiozero.DigitalInputDevice(25)

temp_0 = gpiozero.DigitalInputDevice(12)
temp_1 = gpiozero.DigitalInputDevice(16)
temp_2 = gpiozero.DigitalInputDevice(20)
temp_3 = gpiozero.DigitalInputDevice(21)

search_button = gpiozero.Button(26)

#comparison function that searches csv for a best match
def compare(filename, s, d, p, t):
    best_match_arrays = []
    max_matches = -1
    global planet_name
    global planet_size
    global planet_size
    global planet_distance
    global planet_density
    global planet_temperature
    global planet_text
    global planet_image_path
    
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            current_matches = 0
            # Compare s, d, p, t to columns 2, 3, 4, 5 (indices 1, 2, 3, 4)
            target = [s, d, p, t]
            for i in range(4):  # Compare the first four columns
                if float(target[i]) == float(row[i + 1]):  
                    current_matches += 1

            if current_matches > max_matches:
                max_matches = current_matches
                best_match_arrays = [row]  # Reset list with new best match
            elif current_matches == max_matches:
                best_match_arrays.append(row)  # Add to list of equally good matches

        # Choose random match from best matches
        if best_match_arrays:
            best_match_array = random.choice(best_match_arrays)
            planet_name = best_match_array[5]
            planet_size = best_match_array[1]
            planet_distance = best_match_array[2]
            planet_density = best_match_array[3]
            planet_temperature = best_match_array[4]
            planet_text = best_match_array[6]
            planet_image_path = best_match_array[7]
            image_caption = best_match_array[8]
            
            
def searchfunc(device):
    s = sizeslide.get_current_value()
    d = distslide.get_current_value()
    p = denslide.get_current_value()
    t = tempslide.get_current_value()
    compare('Worlds_Data_Sheet.csv', s,d,p,t)

    paramlabelbox.hide()
    
    planet_name_box.clear()
    planet_name_box.set_text(planet_name)

    planet_fact_box.clear()
    planet_fact_box.set_text(planet_text)
    
    imagecaption.set_text(image_caption)
                
    planet_image = pygame.image.load(planet_image_path).convert()
    planet_image_box.set_image(planet_image, True)
        
            
                                                              
            
#main loop of game window
while is_running:
    time_delta = clock.tick(60)/1000.0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        #SELECTION PHASE
            
        size_0.when_activated = sizefunc
        size_1.when_activated = sizefunc
        size_2.when_activated = sizefunc
        size_3.when_activated = sizefunc
        
        dist_0.when_activated = distfunc
        dist_1.when_activated = distfunc
        dist_2.when_activated = distfunc
        dist_3.when_activated = distfunc
        
        dens_0.when_activated = densfunc
        dens_1.when_activated = densfunc
        dens_2.when_activated = densfunc
        dens_3.when_activated = densfunc
        
        temp_0.when_activated = tempfunc
        temp_1.when_activated = tempfunc
        temp_2.when_activated = tempfunc
        temp_3.when_activated = tempfunc
        
            
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == sizeslide:
                size_slider_value = sizeslide.get_current_value()
                if size_slider_value == 0:
                    size_label_box.clear()
                    size_label_box.set_text('Small')
                    planet_name_box.clear()
                    planet_name_box.set_text(small_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(small_param_text)
                    size_icon.set_image(small_graphic)
                elif size_slider_value == 1:
                    size_label_box.clear()
                    size_label_box.set_text('Medium')
                    planet_name_box.clear()
                    planet_name_box.set_text(medium_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(medium_param_text)
                    size_icon.set_image(medium_graphic)
                elif size_slider_value == 2:
                    size_label_box.clear()
                    size_label_box.set_text('Big')
                    planet_name_box.clear()
                    planet_name_box.set_text(giant_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(giant_param_text)
                    size_icon.set_image(big_graphic)
                elif size_slider_value == 3:
                    size_label_box.clear()
                    size_label_box.set_text('Giant')
                    planet_name_box.clear()
                    planet_name_box.set_text(giant_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(giant_param_text)
                    size_icon.set_image(giant_graphic)
                    
            if event.ui_element == distslide:
                dist_slider_value = distslide.get_current_value()
                if dist_slider_value == 0:
                    dist_label_box.clear()
                    dist_label_box.set_text('Close')
                    planet_name_box.clear()
                    planet_name_box.set_text(close_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(close_param_text)
                    dist_icon.set_image(close_graphic)
                elif dist_slider_value == 1:
                    dist_label_box.clear()
                    dist_label_box.set_text('Inner')
                    planet_name_box.clear()
                    planet_name_box.set_text(close_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(close_param_text)
                    dist_icon.set_image(inner_graphic)
                elif dist_slider_value == 2:
                    dist_label_box.clear()
                    dist_label_box.set_text('Outer')
                    planet_name_box.clear()
                    planet_name_box.set_text(outer_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(outer_param_text)
                    dist_icon.set_image(outer_graphic)
                elif dist_slider_value == 3:
                    dist_label_box.clear()
                    dist_label_box.set_text('Distant')
                    planet_name_box.clear()
                    planet_name_box.set_text(distant_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(distant_param_text)
                    dist_icon.set_image(distant_graphic)

            if event.ui_element == denslide:
                dens_slider_value = denslide.get_current_value()
                if dens_slider_value == 0:
                    dens_label_box.clear()
                    dens_label_box.set_text('100% Rocky')
                    planet_name_box.clear()
                    planet_name_box.set_text(rocky_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(rocky_param_text)
                    dens_icon.set_image(rocky_graphic)
                elif dens_slider_value == 1:
                    dens_label_box.clear()
                    dens_label_box.set_text('Similar to Earth')
                    planet_name_box.clear()
                    planet_name_box.set_text(earthy_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(earthy_param_text)
                    dens_icon.set_image(earthy_graphic)
                elif dens_slider_value == 2:
                    dens_label_box.clear()
                    dens_label_box.set_text('Water World')
                    planet_name_box.clear()
                    planet_name_box.set_text(watery_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(watery_param_text)
                    dens_icon.set_image(watery_graphic)
                elif dens_slider_value == 3:
                    dens_label_box.clear()
                    dens_label_box.set_text('Sub-Neptune')
                    planet_name_box.clear()
                    planet_name_box.set_text(neptune_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(neptune_param_text)
                    dens_icon.set_image(neptune_graphic)

            elif event.ui_element == tempslide:
                temp_slider_value = tempslide.get_current_value()
                if temp_slider_value == 0:
                    temp_label_box.clear()
                    temp_label_box.set_text('Freezing')
                    planet_name_box.clear()
                    planet_name_box.set_text(freeze_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(freeze_param_text)
                    temp_icon.set_image(freeze_graphic)
                elif temp_slider_value == 1:
                    temp_label_box.clear()
                    temp_label_box.set_text('Temperate')
                    planet_name_box.clear()
                    planet_name_box.set_text(temperate_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(temperate_param_text)
                    temp_icon.set_image(temperate_graphic)
                elif temp_slider_value == 2:
                    temp_label_box.clear()
                    temp_label_box.set_text('Scalding')
                    planet_name_box.clear()
                    planet_name_box.set_text(hot_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(hot_param_text)
                    temp_icon.set_image(hot_graphic)
                elif temp_slider_value == 3:
                    temp_label_box.clear()
                    temp_label_box.set_text('Wildcard')
                    planet_name_box.clear()
                    planet_name_box.set_text(wild_param_label)
                    planet_fact_box.clear()
                    planet_fact_box.set_text(wild_param_text)
                    temp_icon.set_image(wild_graphic)

        
        #SEARCH PHASE
        search_button.when_activated = searchfunc            
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == search_button_ui:
                #csv is indexed from 0
                s = sizeslide.get_current_value()
                d = distslide.get_current_value()
                p = denslide.get_current_value()
                t = tempslide.get_current_value()
                compare('Worlds_Data_Sheet.csv', s,d,p,t)


                planet_name_box.clear()
                planet_name_box.set_text(planet_name)

                planet_fact_box.clear()
                planet_fact_box.set_text(planet_text)
                
                planet_image = pygame.image.load(planet_image_path).convert()
                planet_image_box.set_image(planet_image, True)
            
        

        manager.process_events(event)

    manager.update(time_delta)

    #drawing onto the screen
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    
    

#END: final display
    pygame.display.update()



pygame.quit()
