from evdev import InputDevice, list_devices, categorize, KeyEvent, UInput, AbsInfo, ecodes as e
import time
import subprocess

JOYSTICK_AXIS = AbsInfo(
        value = 0,
# frsky taranis
#        min = 0,
#        max = 2000,
# flysky
        min = -32767,
        max = 32767,
        fuzz = 0,
        flat = 15,
        resolution = 0
        )

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
        #e.BTN_C,
        e.BTN_X,
        e.BTN_Y,
        #e.BTN_Z,
        #e.BTN_TL,
        #e.BTN_TR,
        #e.BTN_TL2,
        #e.BTN_TR2,
        e.BTN_SELECT,
        e.BTN_MODE,
        e.BTN_START,
        e.BTN_THUMBL,
        e.BTN_THUMBR,
        e.BTN_TRIGGER_HAPPY2,
        e.BTN_TRIGGER_HAPPY3,
        e.BTN_TRIGGER_HAPPY4,
        e.BTN_TRIGGER_HAPPY5,
        e.BTN_TRIGGER_HAPPY6,
        e.BTN_TRIGGER_HAPPY7,
        e.BTN_TRIGGER_HAPPY8,
        e.BTN_TRIGGER_HAPPY9,
        e.BTN_TRIGGER_HAPPY10,
        e.BTN_TRIGGER_HAPPY11,
        e.BTN_TRIGGER_HAPPY12,
        e.BTN_TRIGGER_HAPPY13,
        e.BTN_TRIGGER_HAPPY14,
        e.BTN_TRIGGER_HAPPY15,
        e.BTN_TRIGGER_HAPPY16,
        e.BTN_TRIGGER_HAPPY17,
        e.BTN_TRIGGER_HAPPY18,
        e.BTN_TRIGGER_HAPPY19,
        e.BTN_TRIGGER_HAPPY20,
        e.BTN_TRIGGER_HAPPY21,
        e.BTN_TRIGGER_HAPPY22,
        e.BTN_TRIGGER_HAPPY23,
        e.BTN_TRIGGER_HAPPY24,
        e.BTN_TRIGGER_HAPPY25,
        e.BTN_TRIGGER_HAPPY26,
        e.BTN_TRIGGER_HAPPY27,
        e.BTN_TRIGGER_HAPPY28,
        e.BTN_TRIGGER_HAPPY29,
        e.BTN_TRIGGER_HAPPY30,
        e.BTN_TRIGGER_HAPPY31,
        e.BTN_TRIGGER_HAPPY32,
        e.BTN_TRIGGER_HAPPY33,
        e.BTN_TRIGGER_HAPPY34,
        e.BTN_TRIGGER_HAPPY35,
        e.BTN_TRIGGER_HAPPY36,
        e.BTN_TRIGGER_HAPPY37,
        e.BTN_TRIGGER_HAPPY38,
        e.BTN_TRIGGER_HAPPY39,
        e.BTN_TRIGGER_HAPPY40,
	    e.KEY_SPACE,
        e.KEY_ENTER,
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
	('↵', e.KEY_ENTER),
	('a', e.KEY_A),
	('b', e.KEY_B),
	('c', e.KEY_C),
	('d', e.KEY_D),
	('e', e.KEY_E),
	('f', e.KEY_F),
	('g', e.KEY_G),
	('h', e.KEY_H),
	('i', e.KEY_I),
	('j', e.KEY_J),
	('k', e.KEY_K),
	('l', e.KEY_L),
	('m', e.KEY_M),
	('n', e.KEY_N),
	('o', e.KEY_O),
	('p', e.KEY_P),
	('q', e.KEY_Q),
	('r', e.KEY_R),
	('s', e.KEY_S),
	('t', e.KEY_T),
	('u', e.KEY_U),
	('v', e.KEY_V),
	('w', e.KEY_W),
	('x', e.KEY_X),
	('y', e.KEY_Y),
	('z', e.KEY_Z),
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

def _active_window_mavproxy_console():
    return subprocess.check_output(['xdotool', 'windowactivate $(xdotool search -name \"mavproxy.py --master=tcp:127.0.0.1:5760 --out=udp:0.0.0.0:14550\")']).decode().strip()

# write virtual js
capabilities = {
        e.EV_ABS: [(e.ABS_X, JOYSTICK_AXIS), (e.ABS_Y, JOYSTICK_AXIS), 
            (e.ABS_Z, JOYSTICK_AXIS) , (e.ABS_RX, JOYSTICK_AXIS),
            (e.ABS_RY, JOYSTICK_AXIS) , (e.ABS_RZ, JOYSTICK_AXIS),
            (e.ABS_THROTTLE, JOYSTICK_AXIS)
            ], 
        e.EV_KEY: ALL_JOYSTICK_BUTTONS }

ui = UInput(events=capabilities, name='js-donghee')
print(ui)

# Search joystick
devices = [InputDevice(path) for path in list_devices()]
frsky_device_path = ''
specktrum_device_path = ''
flysky_device_path = ''
for device in devices:
    print(device.path, device.name, device.phys)
    if 'FrSky' in device.name:
        frsky_device_path = device.path
    if 'SPEKTRUM' in device.name:
        specktrum_device_path = device.path
    if 'Arduino' in device.name:
        flysky_device_path = device.path

# Open FrSky Simulator USB
#gamepad = InputDevice(frsky_device_path) # taranis /dev/input/event6
#gamepad = InputDevice(specktrum_device_path) 
print(flysky_device_path)
gamepad = InputDevice(flysky_device_path) 

last = {
    "ABS_X": 1000, # yaw
    "ABS_Y": 1000, # throttle
    "ABS_Z": 1000, # roll
    "ABS_RX": 1000, # 
    "ABS_RY": 1000, # 
    "ABS_RZ": 1000, # 
    "ABS_THROTTLE": 1000, # 
}

# read streamdeck 
from streamdeck import streamdeck_init, streamdeck_exit, update_key_image, get_key_style

def send_key_string(key_string):
    for key in key_string:
        key_code = [x[1] for x in KEY_LIST if x[0] == key][0]
        ui.write(e.EV_KEY, key_code, 1)
        ui.syn()
        time.sleep(0.0025)
        ui.write(e.EV_KEY, key_code, 0)
        ui.syn()
        time.sleep(0.0025)

gimbal_previous_command = 0

def key_change_callback(deck, key, state):
    global gimbal_previous_command
    #print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)

    update_key_image(deck, key, state)

    if state:
        key_style = get_key_style(deck, key, state)
        key_name = key_style["name"]

        key = ALL_JOYSTICK_BUTTONS[key_name+13]
        #print("pressed streamdeck key {}", key)

        ui.write(e.EV_KEY, key, 1)
        ui.syn()
        if key_name == 5:
            send_key_string("guided 100")

        # pitch up
        if key_name == 6: 
            if gimbal_previous_command == key_name:
                send_key_string("servo set 10 1500 ↵") # stop
                gimbal_previous_command = 0 # init gimbal command
            else:
                send_key_string("servo set 10 1600 ↵") # pitch up
                gimbal_previous_command = key_name

        # pitch down
        if key_name == 7:
            if gimbal_previous_command == key_name:
                send_key_string("servo set 10 1500 ↵") # stop
                gimbal_previous_command = 0 # init gimbal command
            else:
                send_key_string("servo set 10 1400 ↵") # pitch down
                gimbal_previous_command = key_name

        # zoom in
        if key_name == 8: 
            if gimbal_previous_command == key_name:
                send_key_string("servo set 11 1500 ↵") # stop
                gimbal_previous_command = 0 # init gimbal command
            else:
                send_key_string("servo set 11 1000 ↵") # zoom in
                gimbal_previous_command = key_name

        # zoom out
        if key_name == 9:
            if gimbal_previous_command == key_name:
                send_key_string("servo set 11 1500 ↵") # stop
                gimbal_previous_command = 0 # init gimbal command
            else:
                send_key_string("servo set 11 2000 ↵") # zoom out
                gimbal_previous_command = key_name

        # cam1 servo
        if key_name == 10:
            if gimbal_previous_command == key_name:
                send_key_string("servo set 9 1200 ↵") # cam1 front
                gimbal_previous_command = 0 
            else:
                send_key_string("servo set 9 1800 ↵") # cam1 bottom
                gimbal_previous_command = key_name

        # Gimbal Yaw Left
        if key_name == 11:
            if gimbal_previous_command == key_name:
                send_key_string("servo set 12 1500 ↵") # stop
                gimbal_previous_command = 0 
            else:
                send_key_string("servo set 12 1400 ↵") # gimbal yaw left
                gimbal_previous_command = key_name

        # Gimbal Yaw Right
        if key_name == 12:
            if gimbal_previous_command == key_name:
                send_key_string("servo set 12 1500 ↵") # stop
                gimbal_previous_command = 0 
            else:
                send_key_string("servo set 12 1600 ↵") # gimbal yaw right
                gimbal_previous_command = key_name

        # Gimbal Center
        if key_name == 13:
            send_key_string("servo set 13 2000 ↵") # gimbal center
            send_key_string("servo set 13 1500 ↵") 

        #_active_window_mavproxy_console()
        #send_key_string("ARM THROTTLE")
        #_active_window_mavproxy_console()
        #send_key_string("GUIDED 100")
        #send_key_string("command_int GLOBAL_RELATIVE_ALT DO_SET_HOME 0 0 0 0 0 0 346101600 1272080410 0")
 
        #if key_style["name"] == "exit":
            #streamdeck_exit(deck)

    else:
        key_style = get_key_style(deck, key, state)
        key_name = key_style["name"]

        key = ALL_JOYSTICK_BUTTONS[key_name+13]
        #print("released streamdeck key {}", key)

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
ui.write(e.EV_ABS, e.ABS_X, last["ABS_RY"])
ui.syn()
ui.write(e.EV_ABS, e.ABS_Y, last["ABS_RZ"])
ui.syn()

for event in gamepad.read_loop():
    if event.type == e.EV_ABS:
        absevent = categorize(event)
        #print(e.bytype[absevent.event.type][absevent.event.code])

        # joystic frsky taranis
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_X':
#            last["ABS_X"] = absevent.event.value
#            #ui.write(e.EV_ABS, e.ABS_X, absevent.event.value)
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_Y':
#            last["ABS_Y"] = absevent.event.value
#            #ui.write(e.EV_ABS, e.ABS_Y, absevent.event.value)
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
#            last["ABS_RX"] = absevent.event.value
#            #ui.write(e.EV_ABS, e.ABS_Z, absevent.event.value)
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RX':
#            last["ABS_RY"] = absevent.event.value
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RY':
#            last["ABS_Z"] = absevent.event.value
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
#            last["ABS_RZ"] = absevent.event.value
#        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_THROTTLE':
#            last["ABS_THROTTLE"] = absevent.event.value

        # joystic flysky mode-2
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_X': # roll *
            last["ABS_RX"] = absevent.event.value
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_Y': # pitch *
            last["ABS_RY"] = absevent.event.value
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z': # throttle *
            last["ABS_Y"] = -absevent.event.value
        if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RX': # yaw *
            last["ABS_X"] = absevent.event.value

        #if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RY': # SWC+SWD
            #pass
        #if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ': # VRA
            #pass
        #if e.bytype[absevent.event.type][absevent.event.code] == 'ABS_THROTTLE': # VRB
            #pass

        #print(last)
        ui.write(e.EV_ABS, e.ABS_X, last["ABS_X"])
        ui.syn()
        ui.write(e.EV_ABS, e.ABS_Y, last["ABS_Y"])
        ui.syn()
        #ui.write(e.EV_ABS, e.ABS_Z, last["ABS_Z"])
        #ui.syn()
        ui.write(e.EV_ABS, e.ABS_RX, last["ABS_RX"])
        ui.syn()
        ui.write(e.EV_ABS, e.ABS_RY, last["ABS_RY"])
        ui.syn()
        #ui.write(e.EV_ABS, e.ABS_RZ, last["ABS_RZ"])
        #ui.syn()
        #ui.write(e.EV_ABS, e.ABS_THROTTLE, last["ABS_THROTTLE"])
        #ui.syn()
 
ui.close()

deck.reset()     
deck.close()
