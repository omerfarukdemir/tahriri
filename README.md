# Tahriri
### Configuration
- Hash your password via tor: `tor --hash-password "{{password}}"`
- Set password to environment as `TOR_PASSWORD`
- Edit ```/etc/tor/torrc``` with values:
```
ControlPort 9051
CookieAuthentication 1
HashedControlPassword {{password_hash}}
```
- Restart tor service: `service tor restart`
### Run
```
poetry install
python tahriri.py
```
