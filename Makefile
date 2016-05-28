ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
WINEPREFIX="${ROOT_DIR}/../.wine_h2"
WINEARCH="win32"
WINEPATH="C:\\python27\;C:\\python27\\Scripts"

init_linux:
	pip install -r requirements_linux.txt

init_wine:
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" wine wineboot

	# Install mercurial (required to download PyGame)
	# wget https://bitbucket.org/tortoisehg/files/downloads/mercurial-3.8.1-x86.msi -cO /tmp/mercurial-3.8.1-x86.msi
	# WINEPREFIX="${WINEPREFIX}" msiexec /q /i /tmp/mercurial-3.8.1-x86.msi

	# Install Python & requirements
	wget https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi -cO /tmp/python-2.7.11.msi
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" msiexec /i /tmp/python-2.7.11.msi TARGETDIR=C:\\python27; true
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" wine python -c 'import sys; print sys.platform'

	# wget http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi -cO /tmp/pygame-1.9.1.win32-py2.7.msi
	# WINEPREFIX="${WINEPREFIX}" msiexec /i /tmp/pygame-1.9.1.win32-py2.7.msi; true
	wget http://pygame.org/ftp/pygame-1.9.2a0.win32-py2.7.msi -cO /tmp/pygame-1.9.2a0.win32-py2.7.msi
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" msiexec /i /tmp/pygame-1.9.2a0.win32-py2.7.msi; true

	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" wine pip install -r requirements_win.txt

	-mkdir ${WINEPREFIX}/drive_c/libs

	# wget https://www.libsdl.org/release/SDL2-2.0.4-win32-x86.zip -cO ${WINEPREFIX}/drive_c/libs/SDL2-2.0.4-win32-x86.zip
	# cd ${WINEPREFIX}/drive_c/libs && unzip SDL2-2.0.4-win32-x86.zip

	# wget https://www.libsdl.org/projects/SDL_image/release/SDL2_image-2.0.1-win32-x86.zip -cO ${WINEPREFIX}/drive_c/libs/SDL2_image-2.0.1-win32-x86.zip
	# cd ${WINEPREFIX}/drive_c/libs && unzip SDL2_image-2.0.1-win32-x86.zip

	# wget https://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.1-win32-x86.zip -O ${WINEPREFIX}/drive_c/libs/SDL2_mixer-2.0.1-win32-x86.zip
	# cd ${WINEPREFIX}/drive_c/libs && unzip SDL2_mixer-2.0.1-win32-x86.zip


build_linux:
	echo ${ROOT_DIR}
	python2.7 ./setup.py build

build_wine:
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" wine python ./setup.py build
	# cp ${WINEPREFIX}/drive_c/python27/python27.dll build/exe.win-amd64-2.7
	# cp ${WINEPREFIX}/drive_c/SDL2.dll build/exe.win-amd64-2.7
	# cp ../.wine_h2/drive_c/windows/syswow64/python27.dll build/exe.win32-2.7
	cp ../.wine_h2/drive_c/windows/system32/python27.dll build/exe.win32-2.7
	# cp ${WINEPREFIX}/drive_c/libs/*.dll build/exe.win32-2.7
	cp ${WINEPREFIX}/drive_c/Lib/site-packages/pygame/*.dll build/exe.win32-2.7
	cp ${WINEPREFIX}/drive_c/python27/Lib/site-packages/numpy/core/numpy-atlas.dll build/exe.win32-2.7

run_linux:
	./app.py

run_wine:
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" python app.py

python_wine:
	WINEPREFIX="${WINEPREFIX}" WINEARCH="${WINEARCH}" WINEPATH="${WINEPATH}" wine python
