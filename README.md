# Novint Falcon Python Demos

Using the SWIG Python bindings from https://github.com/libnifalcon/libnifalcon

    git clone https://github.com/libnifalcon/libnifalcon
    cd libnifalcon/
    mkdir build
    cd build
    cmake -DBUILD_SWIG_BINDINGS=ON ..
    make -j8
    sudo make install
    # HACK: Install the build python library
    sudo cp lib/_pynifalcon.so lang/swig/pynifalcon.py /usr/lib/python3.7/

    git clone https://github.com/BarnabyShearer/falcon
    cd falcon/
    pip install pipenv
    pipenv run ./cube.py
