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

#constants
INTEGRATE_HOME = 'cp run.py ~/'

# commands
COMMAND_E_TWEAKS_LOKI = "sudo apt install software-properties-common && sudo add-apt-repository ppa:philip.scott/elementary-tweaks && sudo apt update && sudo apt install elementary-tweaks -y"
COMMAND_E_TWEAKS_FREYA = "sudo add-apt-repository ppa:mpstark/elementary-tweaks-daily && sudo apt-get update && sudo apt-get install elementary-tweaks -y"
COMMAND_E_TWEAKS_LOKI = "sudo apt-add-repository ppa:versable/elementary-update && sudo apt-get update && sudo apt-get install elementary-tweaks -y"
COMMAND_VLC = "sudo apt-get update && sudo apt-get install vlc browser-plugin-vlc -y"
COMMAND_GIT = "sudo apt-get install git -y"
COMMAND_FILEZILLA = "sudo add-apt-repository ppa:n-muench/programs-ppa && sudo apt-get update && sudo apt-get install filezilla -y"


def main():
	# ask users if they want to copy run.py to home directory
	home_system_integration():
	# os_subroutine --> Calls the os asking routine to the users
	os_subroutine()


def show_main_menu():
	print ' '
	print ' -------------------------------------------------------- '
	print ' '
	print ' Choose Linux Distribution:'
	print ' '
	print ' 1. Ubuntu [Debian] [apt]'
	print ' 2. Elementary OS [Debian] [apt]'
	print ' 3. Arch Linux [Arch] [pacman]'
	print ' -------------------------------------------------------- '
	print ' x. Exit'

def register_menu_choice():
	os_choice = raw_input('Enter Number [1-3] or [x]: ')

	if os_choice == '1':
		show_ubuntu_menu()
	elif os_choice == '2':
		show_eos_menu()
	elif os_choice == '3':
		show_arch_menu()
	else:
		os_subroutine()

def home_system_integration():
	choice = raw_input('Add this script to home directory so that whenever you open the terminal you can run this script out-of-the-box [y/n] : ')

	if choice == 'y' or choice == 'Y':
		command(INTEGRATE_HOME)
	elif choice == 'n' or choice == 'n':
		print 'OK, moving on ...'

def command(the_command):
	os.system(the_command)

####################################################################
#                                                                  #
#                           SUBROUTINES                            #
#                                                                  #
####################################################################

def os_subroutine():
	show_main_menu()

def ubuntu_subroutine():
	show_ubuntu_menu()

def eos_subroutine():
	show_eos_menu()

def arch_subroutine():
	show_arch_menu()

####################################################################
#                                                                  #
#                         UBUNTU STUFFS                            #
#                                                                  #
####################################################################

def show_ubuntu_menu():
	print ' '
	print ' -------------------------------------------------------- '
	print ' '
	print ' Options:'
	print ' '
	print ' 1. Install ubuntu tweaks'
	print ' 2. Install vlc'
	print ' 3. Install git'
	print ' 4. Install filezilla'
	print ' -------------------------------------------------------- '
	print ' x. Exit'

def register_ubuntu_choice():
	pass

####################################################################
#                                                                  #
#                         EOS STUFFS                               #
#                                                                  #
####################################################################

def show_eos_menu():
	print ' '
	print ' -------------------------------------------------------- '
	print ' '
	print ' Options:'
	print ' '
	print ' 1. Install elementary tweaks [Loki]'
	print ' 2. Install elementary tweaks [Freya]'
	print ' 3. Install elementary tweaks [Luna]'
	print ' 4. Install vlc'
	print ' 5. Install git'
	print ' 6. Install filezilla'
	print ' -------------------------------------------------------- '
	print ' x. Exit'

####################################################################
#                                                                  #
#                         ARCH STUFFS                              #
#                                                                  #
####################################################################

def show_arch_menu():
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

if __name__ == '__main__':
	main()