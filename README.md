# Hako

[![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Welcome to Hako

Hako (or "box" in Japanese) is a super secure decentralized file sharing application powered by Web 3.0

Unlike other file sharing services such as Dropbox and Google Drive, Hako does not place your keys in the hands of a large companies. The user is always in control of your keys and your data.

Hako leverages Web 3.0 peer to peer protocols so users can directly share data, as well as access to a distributed network layer or a trusted federated re encryption network.
Hako has no single point of failure and allow non-trusted 3rd parties to delegate access to data - while never being able to decipher the original message.




### Concepts 


#### NUCID

We introduce a new concept of a `NUCID` all a NUCID is, is a combination of a NuCypher policy and a IPFS CID. A NUCID specifices alot of information in not tooooo many characters. It have the access policy, the signing key, the humanreadble label and the CID (location and sig of encrypted data)

This all lets you create NUCID's or download data via NUCID's. You can alwayws request a NUCID you don't have access too - you just won't be able to decrypt it. If the policy allows you access, your Bob keys will allow yout to decrypt.

#### Futari 

We introduce a new concept of a `Futari` (or "two people" in Japanese) 


### Install


```
git clone
cd hako
```

now we grab all the deps
```
pipenv install --skip-lock --pre
```