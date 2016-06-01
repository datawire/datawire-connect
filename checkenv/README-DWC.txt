Datawire Connect relies on the datawire-cli package.

We strongly recommend that you use a virtualenv when working on Datawire Connect --
if you're doing that, you can go to the main Datawire Connect directory and run

make install-dwc

to install the datawire-cli package in your virtualenv.

If you don't want to use a virtualenv, you can install datawire-cli by hand:

curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s --

will install it to $HOME/.datawire/cli and offer to update your .bashrc.

