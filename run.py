# Copyright 2016 Ashish Shekar (codekidX)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

##########################################################################
#                                                                        #
#             Codekid's Noobs Script for Linux Newbies                   #
#                                                                        #
##########################################################################

import os
import pickle
import shutil
import sys

#constants
INTEGRATE_HOME = 'cp run.py ~/'
COMMANDS_CL_FILE = 'puppet.cl'
COMMAND_GET_CL 'wget'

# commands
COMMAND_E_TWEAKS_LOKI = "sudo apt install software-properties-common && sudo add-apt-repository ppa:philip.scott/elementary-tweaks && sudo apt update && sudo apt install elementary-tweaks -y"
COMMAND_E_TWEAKS_FREYA = "sudo add-apt-repository ppa:mpstark/elementary-tweaks-daily && sudo apt-get update && sudo apt-get install elementary-tweaks -y"
COMMAND_E_TWEAKS_LOKI = "sudo apt-add-repository ppa:versable/elementary-update && sudo apt-get update && sudo apt-get install elementary-tweaks -y"
COMMAND_VLC = "sudo apt-get update && sudo apt-get install vlc browser-plugin-vlc -y"
COMMAND_GIT = "sudo apt-get install git -y"
COMMAND_FILEZILLA = "sudo add-apt-repository ppa:n-muench/programs-ppa && sudo apt-get update && sudo apt-get install filezilla -y"


def main():
	# before os subroutine is called cl [commands-list] extraction subroutine is called to dump the command list
	# ask users if they want to copy run.py to home directory
	home_system_integration()


	# os_subroutine --> Calls the os asking routine to the users
	os_subroutine()
	# print if cl present


def show_main_menu():
	command('clear')
	print ' '
	print ' -------------------------------------------------------- '
	print ' '
	print ' Choose Linux Distribution:'
	print ' '
	print ' 1. Ubuntu, Elementary OS, Kubuntu, Lubuntu [apt]'
	print ' 2. Arch Linux, Antergos [pacman]'
	print ' -------------------------------------------------------- '
	print ' x. Exit'

def register_menu_choice():
	os_choice = raw_input('Enter Number [1-3] or [x]: ')

	if os_choice == '1':
		show_apt_menu()
	elif os_choice == '2':
		show_eos_menu()
	elif os_choice == 'x':
		sys.exit()
	else:
		os_subroutine()

def home_system_integration():
	choice = raw_input('Add this script to home directory so that whenever you open the terminal you can run this script out-of-the-box [y/n] : ')

	if choice == 'y' or choice == 'Y':
		command(INTEGRATE_HOME)
		print 'From next time you can run puppet-script from home directory itself :)'
	elif choice == 'n' or choice == 'n':
		print 'OK, moving on ...'

def command(the_command):
	os.system(the_command)

def get_cl():
	pass

####################################################################
#                                                                  #
#                           SUBROUTINES                            #
#                                                                  #
####################################################################

def os_subroutine():
	show_main_menu()
	register_menu_choice()

def ubuntu_subroutine():
	show_ubuntu_menu()

def eos_subroutine():
	show_eos_menu()

def arch_subroutine():
	show_arch_menu()

####################################################################
#                                                                  #
#                         APT STUFFS                               #
#                                                                  #
####################################################################

def show_apt_menu():
	command('clear')
	print ' '
	print ' -------------------------------------------------------- '
	print ' '
	print ' Options:'
	print ' '
	print ' ===== SYSTEM ====='
	print ' 1. Install elementary tweaks [Loki]'
	print ' 2. Install elementary tweaks [Freya]'
	print ' 3. Install elementary tweaks [Luna]'
	print ' 4. Install git'
	print ' 5. Install Gnome Disk Utility'
	print ' ===== WEB ====='
	print ' 6. Install Filezilla'
	print ' 7. Install Google Chrome'
	print ' ===== EDITOR ====='
	print ' 8. Install Sublime Text 3'
	print ' 9. Install Atom'
	print ' ===== MEDIA ====='
	print ' 10. Install vlc'
	print ' -------------------------------------------------------- '
	print ' x. Exit'

####################################################################
#                                                                  #
#                         ARCH STUFFS                              #
#                                                                  #
####################################################################

def show_arch_menu():
	command('clear')
	print ' '
	print ' -------------------------------------------------------- '
	print ' '
	print ' Options:'
	print ' '
	print ' 1. Install ubuntu tweaks'
	print ' 2. Install vlc'
	print ' 1. Install git'
	print ' 3. Install filezilla'
	print ' -------------------------------------------------------- '
	print ' x. Exit'



####################################################################
#                                                                  #
#                             MENU                                 #
#                                                                  #
# - Everything runs through this function regarfing the choice     #
# - of installing any stuff                                        #
####################################################################

def register_command(the_choice):
	# Prefixes
	# u - ubuntu choices
	# e - eos choices
	# a - arch choices
	pass

def is_cl_present():
	# get the current directory of the
	curr_dir = os.path.dirname(os.path.abspath(__file__))
	return os.path.exists(curr_dir + "/" + COMMANDS_CL_FILE)

def is_os_64bit():
    return platform.machine().endswith('64')

if __name__ == '__main__':
	main()