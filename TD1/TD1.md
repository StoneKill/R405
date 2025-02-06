# TD1 R405

## Préparation "manuelle" des VMs :  

### Serveurs DNS Installation et config de DNS-1/DNS-2 :  

- Installation de l'OS  
    - Pas de commande particulière   
- MàJ des paquets    
    - `apt update -y && apt upgrade -y`  
- Installation de sudo  
    - `apt install sudo`  
- Ajout de l'user de base de sudo      
    - `adduser user sudo`   
- Configuration de la machine (hostname, host ssh, domaine)    
    - `sudo nano /etc/hostname`   
    ```bash
    Serveur_DNS_n
    ```  

    - `sudo nano /etc/hosts`  

    ```bash  
    # This host address
    127.0.1.1  Serveur_DNS_n
    ```
- Installer Bind9 et Dnsutils      
- Créer la conf Bind9 (zone + options + etc)      
- SERIAL !!!!!!    
- Reboot Bind9      
- Faire la commande `named checkzone`    

### Installation et config de web-1 à web-n :    

- MàJ des paquets   
- Installer Apache2   
- Configurer les VHosts    
- Installer le site web    
- Redémarrer le service    