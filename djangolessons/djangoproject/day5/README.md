Set up django project with Anaconda

1. Install dependencies

```bash
$ sudo apt update
$ sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

2. Download install script

```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```

3. Install conda

```bash
$ sudo chmod u+x Anaconda3-2022.10-Linux-x86_64.sh
$ ./Anaconda3-2022.10-Linux-x86_64.sh
```

4. Complete the installation

a. Press Enter to review the license agreement. Then press and hold Enter to scroll.

b. Enter “yes” to agree to the license agreement.

c. Use Enter to accept the default install location, use CTRL+C to cancel the installation, or enter another file path to specify an alternate installation directory. If you accept the default install location, the installer displays PREFIX=/home/<USER>/anaconda<2/3> and continues the installation. It may take a few minutes to complete.

Note: Anaconda recommends you accept the default install location. Do not choose the path as `/usr` for the Anaconda/Miniconda installation.

d. The installer prompts you to choose whether to initialize Anaconda Distribution by running `conda init`. Anaconda recommends entering “yes”.

e. If you enter “no”, then conda will not modify your shell scripts at all. In order to initialize after the installation process is done, first run source `[PATH TO CONDA]/bin/activate` and then run `conda init`.

f. The installer finishes and displays, “Thank you for installing Anaconda3!”

g. Close and re-open your terminal window for the installation to take effect, or enter the command `source ~/.bashrc` to refresh the terminal.

Note: You can also control whether or not your shell has the base environment activated each time it opens.

```bash
# The base environment is activated by default
conda config --set auto_activate_base True

# The base environment is not activated by default
conda config --set auto_activate_base False
```
5. Install Anaconda Navigator (i.e. the GUI interface)

```bash
$ conda install anaconda-navigator
```

And reload the shell.

```bash
$ source ~/.bashrc
```
6. Conda now can be opened from the terminal

```bash
$ anaconda-navigator
```

7. Create a conda environment and activate:

```bash
# creates and activates a conda environment 
$ conda create --name env
$ conda activate env
# creates and activates a conda environment in the designated path
$ conda create --prefix ./env
$ conda activate ./env
```

8. Install dependencies

```bash
$ conda install -c anaconda django
$ django-admin startproject djangoproject
$ conda install -c conda-forge djangorestframework
```
