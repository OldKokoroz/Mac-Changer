import subprocess
import optparse

def step_1():

    command_inputs = optparse.OptionParser()
    command_inputs.add_option("-i", "--interface", dest="attack_interface", help="attack interface to change")
    command_inputs.add_option("-m", "--mac", dest="new_mac", help="new mac")

    return command_inputs.parse_args()


def step_2(attack_interface, new_mac):
    subprocess.call(["ifconfig", attack_interface, "down"])
    subprocess.call(["ifconfig", attack_interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", attack_interface, "up"])


print("""---------------------------------------------------

Mac Changer Started

Linux and Mac only

---------------------------------------------------
""")

(fast_input, arguments) = step_1()
step_2(fast_input.attack_interface, fast_input.new_mac)


print(" JOB IS DONE ")
