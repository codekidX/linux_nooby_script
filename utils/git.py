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
import os
import sys

#constants
GIT_STATUS = 'git status'
GIT_ADD = 'git add .'
GIT_COMMIT = 'git commit -m "'
GIT_PUSH_MASTER = 'git push -u origin master'

def main():
	# view status
	command(GIT_STATUS)
	show_changes_pattern()
	# ask if you want to proceed with adding the changes
	proceed = raw_input('Do you want to add these changes ? [y/n] ')

	if proceed == 'y' or proceed == 'Y':
		command(GIT_ADD)
		commit_message = raw_input('Enter commit message: ')
		command(GIT_COMMIT + commit_message + '"')
		command(GIT_PUSH_MASTER)
	else:
		print 'Exiting script now ...'
		sys.exit()


def command(the_command):
	os.system(the_command)

def show_changes_pattern():
	print ' '
	print ' -----------------------------------------------------'
	print ' '
	print 'THESE ARE THE CHANGES ^'


if __name__ == '__main__':
	main()