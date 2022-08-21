from evdev import InputDevice, list_devices, categorize, KeyEvent, UInput, AbsInfo, ecodes as e
import time

JOYSTICK_AXIS = AbsInfo(
        value = 0,
        min = 0,
        max = 2000,
        fuzz = 0,
        flat = 15,
        resolution = 0
        )

ALL_JOYSTICK_AXIS = [ (e.ABS_X, JOYSTICK_AXIS), (e.ABS_Y, JOYSTICK_AXIS) , (e.ABS_Z, JOYSTICK_AXIS) , (e.ABS_RX, JOYSTICK_AXIS) ]

ALL_JOYSTICK_BUTTONS = [
        e.BTN_JOYSTICK,
        e.BTN_THUMB, 
        e.BTN_THUMB2, 
        e.BTN_TOP,
        e.BTN_TOP2,
        e.BTN_PINKIE,
        e.BTN_BASE,
        e.BTN_BASE2,
        e.BTN_BASE3,
        e.BTN_BASE4,
        e.BTN_BASE5,
        e.BTN_BASE6,
        e.BTN_DEAD,
        e.BTN_A,
        e.BTN_B,
        e.BTN_C,
#        e.BTN_X,
#        e.BTN_Y,
#        e.BTN_Z,
#        e.BTN_TL,
#        e.BTN_TR,
#        e.BTN_TL2,
#        e.BTN_TR2,
#        e.BTN_SELECT,
#        e.BTN_START,
#        e.BTN_MODE,
#        e.BTN_THUMBL,
#        e.BTN_THUMBR,
#        e.BTN_TRIGGER_HAPPY2,
#        e.BTN_TRIGGER_HAPPY3,
#        e.BTN_TRIGGER_HAPPY4,
#        e.BTN_TRIGGER_HAPPY5,
#        e.BTN_TRIGGER_HAPPY6,
#        e.BTN_TRIGGER_HAPPY7,
#        e.BTN_TRIGGER_HAPPY8,
#        e.BTN_TRIGGER_HAPPY9,
#        e.BTN_TRIGGER_HAPPY10,
#        e.BTN_TRIGGER_HAPPY11,
#        e.BTN_TRIGGER_HAPPY12,
#        e.BTN_TRIGGER_HAPPY13,
#        e.BTN_TRIGGER_HAPPY14,
#        e.BTN_TRIGGER_HAPPY15,
#        e.BTN_TRIGGER_HAPPY16,
#        e.BTN_TRIGGER_HAPPY17,
#        e.BTN_TRIGGER_HAPPY18,
#        e.BTN_TRIGGER_HAPPY19,
#        e.BTN_TRIGGER_HAPPY20,
#        e.BTN_TRIGGER_HAPPY21,
#        e.BTN_TRIGGER_HAPPY22,
#        e.BTN_TRIGGER_HAPPY23,
#        e.BTN_TRIGGER_HAPPY24,
#        e.BTN_TRIGGER_HAPPY25,
#        e.BTN_TRIGGER_HAPPY26,
#        e.BTN_TRIGGER_HAPPY27,
#        e.BTN_TRIGGER_HAPPY28,
#        e.BTN_TRIGGER_HAPPY29,
#        e.BTN_TRIGGER_HAPPY30,
#        e.BTN_TRIGGER_HAPPY31,
#        e.BTN_TRIGGER_HAPPY32,
#        e.BTN_TRIGGER_HAPPY33,
#        e.BTN_TRIGGER_HAPPY34,
#        e.BTN_TRIGGER_HAPPY35,
#        e.BTN_TRIGGER_HAPPY36,
#        e.BTN_TRIGGER_HAPPY37,
#        e.BTN_TRIGGER_HAPPY38,
#        e.BTN_TRIGGER_HAPPY39,
#        e.BTN_TRIGGER_HAPPY40,
	e.KEY_SPACE,
	e.KEY_A,
	e.KEY_B,
	e.KEY_C,
	e.KEY_D,
	e.KEY_E,
	e.KEY_F,
	e.KEY_G,
	e.KEY_H,
	e.KEY_I,
	e.KEY_J,
	e.KEY_K,
	e.KEY_L,
	e.KEY_M,
	e.KEY_N,
	e.KEY_O,
	e.KEY_P,
	e.KEY_Q,
	e.KEY_R,
	e.KEY_S,
	e.KEY_T,
	e.KEY_U,
	e.KEY_V,
	e.KEY_W,
	e.KEY_X,
	e.KEY_Y,
	e.KEY_Z,
	e.KEY_0,
	e.KEY_1,
	e.KEY_2,
	e.KEY_3,
	e.KEY_4,
	e.KEY_5,
	e.KEY_6,
	e.KEY_7,
	e.KEY_8,
	e.KEY_9
        ]


KEY_LIST = [
	(' ', e.KEY_SPACE),
	('A', e.KEY_A),
	('B', e.KEY_B),
	('C', e.KEY_C),
	('D', e.KEY_D),
	('E', e.KEY_E),
	('F', e.KEY_F),
	('G', e.KEY_G),
	('H', e.KEY_H),
	('I', e.KEY_I),
	('J', e.KEY_J),
	('K', e.KEY_K),
	('L', e.KEY_L),
	('M', e.KEY_M),
	('N', e.KEY_N),
	('O', e.KEY_O),
	('P', e.KEY_P),
	('Q', e.KEY_Q),
	('R', e.KEY_R),
	('S', e.KEY_S),
	('T', e.KEY_T),
	('U', e.KEY_U),
	('V', e.KEY_V),
	('W', e.KEY_W),
	('X', e.KEY_X),
	('Y', e.KEY_Y),
	('Z', e.KEY_Z),
	('0', e.KEY_0),
	('1', e.KEY_1),
	('2', e.KEY_2),
	('3', e.KEY_3),
	('4', e.KEY_4),
	('5', e.KEY_5),
	('6', e.KEY_6),
	('7', e.KEY_7),
	('8', e.KEY_8),
	('9', e.KEY_9)
]

# write virtual js
capabilities = {
        e.EV_ABS: [(e.ABS_X, JOYSTICK_AXIS), (e.ABS_Y, JOYSTICK_AXIS) , (e.ABS_Z, JOYSTICK_AXIS) , (e.ABS_RX, JOYSTICK_AXIS)] , 
        e.EV_KEY: ALL_JOYSTICK_BUTTONS }

ui = UInput(events=capabilities, name='js-donghee')
print(ui)

# read real js
devices = [InputDevice(path) for path in list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

gamepad = InputDevice('/dev/input/event2')

last = {
    "ABS_X": 1000, # yaw
    "ABS_Y": 1000, # throttle
    "ABS_Z": 1000, # roll
    "ABS_RX": 1000, # pitch
}

# read streamdeck 

from streamdeck import streamdeck_init, streamdeck_exit, update_key_image, get_key_style

def send_key_string(key_string):
    for key in key_string:
        key_code = [x[1] for x in KEY_LIST if x[0] == key][0]
        ui.write(e.EV_KEY, key_code, 1)
        ui.syn()
        ui.write(e.EV_KEY, key_code, 0)
        ui.syn()

def key_change_callback(deck, key, state):
    #print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)

    update_key_image(deck, key, state)

    if state:
        key_style = get_key_style(deck, key, state)

        if key_style["name"] == "loiter":
            key = e.BTN_JOYSTICK
            ui.write(e.EV_KEY, key, 1)
            ui.syn()

        if key_style["name"] == "guided":
            key = e.BTN_THUMB
            ui.write(e.EV_KEY, key, 1)
            ui.syn()

        if key_style["name"] == "auto":
            key = e.BTN_THUMB2
            ui.write(e.EV_KEY, key, 1)
            ui.syn()

        if key_style["name"] == "arm":
            send_key_string("ARM THROTTLE")

        if key_style["name"] == "goto":
            send_key_string("GUIDED 100")

        if key_style["name"] == "home":
            send_key_string("command_int GLOBAL_RELATIVE_ALT DO_SET_HOME 0 0 0 0 0 0 346101600 1272080410 0")
 
        if key_style["name"] == "exit":
            streamdeck_exit(deck)

    else:
        key_style = get_key_style(deck, key, state)

        if key_style["name"] == "loiter":
            key = e.BTN_JOYSTICK
            ui.write(e.EV_KEY, key, 0)
            ui.syn()

        if key_style["name"] == "guided":
            key = e.BTN_THUMB
            ui.write(e.EV_KEY, key, 0)
            ui.syn()

        if key_style["name"] == "auto":
            key = e.BTN_THUMB2
            ui.write(e.EV_KEY, key, 0)
            ui.syn()

deck = streamdeck_init()

for key in range(deck.key_count()):
    update_key_image(deck, key, False)

deck.set_key_callback(key_change_callback)

# https://manpages.ubuntu.com/manpages/focal/man7/python-evdev.7.html
# https://readthedocs.org/projects/python-evdev/downloads/pdf/latest/

ui.write(e.EV_ABS, e.ABS_X, last["ABS_X"])
ui.syn()
ui.write(e.EV_ABS, e.ABS_Y, last["ABS_Y"])
ui.syn()
ui.write(e.EV_ABS, e.ABS_Z, last["ABS_Z"])
ui.syn()
ui.write(e.EV_ABS, e.ABS_RX, last["ABS_RX"])
ui.syn()

for event in gamepad.read_loop():
    if event.type == e.EV_ABS:
        absevent = categorize(event)
        #print(e.bytype[absevent.event.type][absevent.event.code])

        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_X':
            last["ABS_X"] = absevent.event.value
            #ui.write(e.EV_ABS, e.ABS_X, absevent.event.value)
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_Y':
            last["ABS_Y"] = absevent.event.value
            #ui.write(e.EV_ABS, e.ABS_Y, absevent.event.value)
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
            last["ABS_Z"] = absevent.event.value
            #ui.write(e.EV_ABS, e.ABS_Z, absevent.event.value)
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RX':
            last["ABS_RX"] = absevent.event.value
            #ui.write(e.EV_ABS, e.ABS_RX, absevent.event.value)
        #print(last)
        ui.write(e.EV_ABS, e.ABS_X, last["ABS_X"])
        ui.syn()
        ui.write(e.EV_ABS, e.ABS_Y, last["ABS_Y"])
        ui.syn()
        ui.write(e.EV_ABS, e.ABS_Z, last["ABS_Z"])
        ui.syn()
        ui.write(e.EV_ABS, e.ABS_RX, last["ABS_RX"])
        ui.syn()

 
ui.close()

deck.reset()     
deck.close()


