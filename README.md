# Tahriri
### Dependencies
tor, stem, flask
### Configuration
- Hash your password via tor:
```
tor --hash-password "{{password}}"
```
- Export it to your root profile:
```
export TOR_PASSWORD={{password}}
```
- Edit ```/etc/tor/torrc``` with:
```
ControlPort 9051
CookieAuthentication 1
HashedControlPassword {{password_hash}}
```
- Restart tor service:
```
sudo service tor restart
```
### Run
```
sudo python tahriri.py
```
