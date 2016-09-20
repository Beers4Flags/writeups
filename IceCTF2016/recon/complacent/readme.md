# Complacent (Reconnaissance · 40 pt)

I used nikto to scan the chall website:
```bash
nikto -h https://complacent.vuln.icec.tf

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          104.154.248.13
+ Target Hostname:    complacent.vuln.icec.tf
+ Target Port:        443
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /C=IS/ST=Kingdom of IceCTF/L=IceCTF city/O=Secret IceCTF Buisness Corp/OU=Flag: IceCTF{this_1nformation_wasnt_h1dd3n_at_a11}/CN=complacent.icec.tf
                   Ciphers:  ECDHE-RSA-AES256-GCM-SHA384
                   Issuer:   /C=IS/ST=Kingdom of IceCTF/L=IceCTF city/O=Secret IceCTF Buisness Corp/OU=Flag: IceCTF{this_1nformation_wasnt_h1dd3n_at_a11}/CN=complacent.icec.tf
```
                   
Flag was in SSL Certificate
The flag is : IceCTF{this_1nformation_wasnt_h1dd3n_at_a11}
