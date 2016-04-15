Sample for the summit plugin lab
================================

Don't use this yet unless you are fond of broken code!

starting with ubuntu 14.04 image
::

    sudo apt-get install -y git
    git clone http://github.com/openstack-dev/devstack
    cd devstack
    git checkout stable/mitaka
    wget https://raw.githubusercontent.com/doug-fish/sample-horizon-angular-plugin/master/local.conf
    ./stack.sh
