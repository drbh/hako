# Hako

[![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Welcome to Hako

![login](https://cdn-images-1.medium.com/max/1600/1*GFZ2iFworTLm4ta3Wehw7g.png)

Hako (or "box" in Japanese) is a super secure decentralized file sharing application powered by Web 3.0

Unlike other file sharing services such as Dropbox and Google Drive, Hako does not place your keys in the hands of a large companies. The user is always in control of your keys and your data.

![img](https://cdn-images-1.medium.com/max/1600/1*Qhs0abEvWk7v84AS8V7E-g.gif)

**Hako** leverages Web 3.0 peer to peer protocols so users can directly share data, as well as access to a distributed network layer or a trusted federated re encryption network.
Hako has no single point of failure and allow non-trusted 3rd parties to delegate access to data - while never being able to decipher the original message.

### Resources

https://medium.com/@david.richard.holtz/hako-3825c3a033d7

https://www.youtube.com/watch?v=_0Jl836ETLo

https://github.com/drbh/ncipfs 

## Concepts 

#### NUCID

We introduce a new concept of a `NUCID` all a NUCID is, is a combination of a NuCypher policy and a IPFS CID. A NUCID specifices alot of information in not tooooo many characters. It have the access policy, the signing key, the humanreadble label and the CID (location and sig of encrypted data)

This all lets you create NUCID's or download data via NUCID's. You can alwayws request a NUCID you don't have access too - you just won't be able to decrypt it. If the policy allows you access, your Bob keys will allow yout to decrypt.

![](https://cdn-images-1.medium.com/max/1600/1*s-92vOhsK_msW_UBTC_j5Q.png)\\

#### Futari 

We introduce a new concept of a `Futari` (or "two people" in Japanese) 


### Install


```bash
git clone https://github.com/drbh/hako.git
cd hako
```

now we grab all the deps
```bash
pipenv install --skip-lock --pre
```

### Run App

```bash
pipenv shell
```

```bash
python app.py 
```

**Note** 

you may have to edit the local IP address in `app/src/App.vue` and in `app.py` to your computers local IP (if running in offline mode) otherwise change the IPs accordingly to the networks you want to connect to.


you should see

```bash
(hako) bash-3.2$ python app.py 
Automatic Mode A Public Gateway will be used as a fallback
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

### Endpoints
```
/data POST 
/create_user POST
/allow_access POST
/decrypt_message POST
/my_public_keys POST
```
