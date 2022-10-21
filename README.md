Anonymous web application example on tor network

#### Requirements
- ```anaconda```/```miniconda```, ```tor```
#### Create environment
- ```conda env create -f conda.yaml```
#### Use environment
- ```conda activate tahriri```
#### Update environment
- ```conda env update -f conda.yaml --prune```
#### Exit environment
- ```conda deactivate```
#### Remove environment
- ```conda env remove -n tahriri```
#### Configuration
- Hash your password via tor: `tor --hash-password "{{password}}"`
- Set password to environment as `TOR_PASSWORD`
- Edit ```/etc/tor/torrc``` with values:
```
ControlPort 9051
CookieAuthentication 1
HashedControlPassword {{password_hash}}
```
- Restart tor service: `service tor restart`
#### Run
```python tahriri.py```
