apt install curl
# install rust
curl https://sh.rustup.rs -sSf | sh
# install git if not present
sudo apt install git

git clone https://github.com/nachoparker/dutree.git
git clone https://github.com/nachoparker/dutree.git
# after intalling the rust and clonning it
source $HOME/.cargo/env
cargo install dutree
dutree -h


# best ncdu on ubuntu
sudo apt install ncdu
