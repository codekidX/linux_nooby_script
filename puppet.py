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
import shutil
import sys
import ast

#constants
INTEGRATE_HOME = 'cp run.py ~/'
COMMAND_EXECUTE_APT_MENU = 'chmod +x puppet-apt-list.sh && ./puppet-apt-list.sh'
COMMANDS_CL_FILE = 'puppet.cl'
COMMANDS_PAL_FILE = 'puppet-apt-list.sh'
COMMAND_GET_CL = 'wget https://raw.githubusercontent.com/codekidX/linux_nooby_script/master/puppet.cl'
COMMAND_GET_PAL = 'wget https://raw.githubusercontent.com/codekidX/linux_nooby_script/master/puppet-apt-list.sh'
CL_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + COMMANDS_CL_FILE
PAL_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + COMMANDS_PAL_FILE

# commands
# COMMAND_E_TWEAKS_LOKI = "sudo apt install software-properties-common && sudo add-apt-repository ppa:philip.scott/elementary-tweaks && sudo apt update && sudo apt install elementary-tweaks -y"
# COMMAND_E_TWEAKS_FREYA = "sudo add-apt-repository ppa:mpstark/elementary-tweaks-daily && sudo apt-get update && sudo apt-get install elementary-tweaks -y"
# COMMAND_E_TWEAKS_LOKI = "sudo apt-add-repository ppa:versable/elementary-update && sudo apt-get update && sudo apt-get install elementary-tweaks -y"
# COMMAND_VLC = "sudo apt-get update && sudo apt-get install vlc browser-plugin-vlc -y"
# COMMAND_GIT = "sudo apt-get install git -y"
# COMMAND_FILEZILLA = "sudo add-apt-repository ppa:n-muench/programs-ppa && sudo apt-get update && sudo apt-get install filezilla -y"


def main():
	# before script subroutine is called cl [commands-list] extraction subroutine is called to dump the command list
	get_cl()
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
		apt_subroutine()
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
	print 'Please wait ... '
	print '%s' % (is_cl_present())
	print 'Getting updated commands list'
	if is_cl_present() is True:
		print 'Deleting old command list ..'
		os.remove(CL_PATH)
		os.remove(PAL_PATH)
		command(COMMAND_GET_CL)
		command(COMMAND_GET_PAL)
	else:
		command(COMMAND_GET_CL)
		command(COMMAND_GET_PAL)

	command('clear')
	print 'Commands list fetched !'


####################################################################
#                                                                  #
#                           SUBROUTINES                            #
#                                                                  #
####################################################################

def os_subroutine():
	show_main_menu()
	register_menu_choice()

def apt_subroutine():
	show_apt_menu()
	register_apt_choice()

def arch_subroutine():
	show_arch_menu()
	register_arch_choice()

####################################################################
#                                                                  #
#                         APT STUFFS                               #
#                                                                  #
####################################################################

def show_apt_menu():
	command('clear')
	command(COMMAND_EXECUTE_APT_MENU)


def register_apt_choice():
	choices = {}
	apt_choice = raw_input('Enter Number or [x] \{Multiple installs by inserting commas\}: ')

	# if choice_type == True then the user has entered multiple input
	choice_type = single_or_multiple(apt_choice)

	if choice_type is True:
		choices = apt_choice.split(',')
		for i in range(0, len(choices)):
			execute_command('a', choices[i])
	else:
		execute_command('a', apt_choice)

	# show menu agian after all execution complete
	show_apt_menu()

def register_arch_choice():
	choices = {}
	apt_choice = raw_input('Enter Number or [x] \{Multiple installs by inserting commas\}: ')

	# if choice_type == True then the user has entered multiple input
	choice_type = single_or_multiple(apt_choice)

	if choice_type is True:
		choices = apt_choice.split(',')
		for i in range(0, len(choices)):
			execute_command('p', choices[i])
	else:
		execute_command('p', apt_choice)

	# show menu agian after all execution complete
	show_arch_menu()

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

def execute_command(the_pm, the_choice):
	# Prefixes
	# a - ubuntu choices
	# p - arch choices

	# first load the file to get commands in the form of dictionary
	cl_file = open(CL_PATH, 'r')
	# read cl file
	cl_str = cl_file.read()
	# file contents are in the form of <'str'> --> convert it to <'dict'>
	cl_dict = ast.literal_eval(cl_str)
	# evaluate choice as dictionary key :D
	cl_choice = the_pm + the_choice
	# print(cl_dict[cl_choice])
	#                 Choice Restrictor
	#   -- if there is a os specific choice [append suffix]
	# ------------------------------------------------------
	#
	if cl_choice is 'a7':
		if is_os_64bit() == True:
			cl_choice.append('_2')
		else:
			cl_choice.append('_1')


	if cl_choice is 'ax' or 'px':
		command('clear')
		sys.exit()
	else:
		# all hail the mighty script execute_command starts NOW !!!
		command(cl_dict[cl_choice])
		# clear screen after each command
		command('clear')

def is_cl_present():
	# get the current directory of the
	return os.path.exists(CL_PATH) or os.path.exists(PAL_PATH)

def is_os_64bit():
    return platform.machine().endswith('64')

def single_or_multiple(choice):
	return ',' in choice
	

if __name__ == '__main__':
	main()