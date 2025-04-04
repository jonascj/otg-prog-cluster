# OTG Prog Cluster
Sejt cluster af ~20 identiske Dell computere, med en i7-6700; Nvidia GeForce GTX 1070; 1x 256GB NVMe M.2 SSD; 2TB Segate HDD.

## Indholdsfortegnelse
* [Install (how-to)](#install)
* [Naming convention](#name-scheme)
* [Login](#login-info-defaults)
* [Nodes (Master/Slaves)](#nodes-etchosts)
* [Logbog](#logbog-ish)

---

### Install
Alle maskinerne er blevet installeret uden GUI og med SSH server, 

---

### Name-scheme
debian[id-fra-case] (står på siden.)

Eksempel:
**SDE-2017-10101** -> debian10101

---

### Login-Info (defaults)
* root:root
* debian:debian

**OBS:** Root SSH er tilladt på alle maskiner!

---

### Nodes (/etc/hosts)
**Master:** debian10102 (10.130.58.40)

```
10.130.58.40 debian10102
10.130.58.38 debian10107
10.130.58.43 debian10092
10.130.58.44 debian10101
```

**Info:** d. 01.04.2025 blev deres subnet skiftet til 10.42.0.1/24

---

### Opsætning
Vi følger for det meste den her [guide](https://github.com/asankaSovis/Beowulf-Cluster-Setup-Tutorial). Men her er en kort gennemgang af hvad der skal være på computerne
#### Manager node
 - mpiuser vigtigt at holde styr på at alle mpiuser på alle maskiner skal have samme uid.
 - NFS server der dele /home/mpiuser/shared
 - mpich installeret.
### Worker nodes
 - mpiuser
 - Mount til /home/mpiuser/shared
 - ssh key fra Manager node i brugeren mpiuser
 - mpich installeret



### Logbog (ish)

| Dag | Hvad er der sket/lavet? | Til næste gang. |
| ------------- | ------------- | ------------- |
| Mandag - 31.03.2025 | I dag er der blevet installeret Debian 12 (bookworm) på 4 maskiner, der er også forsøgt installation af at [Beowulf - MPI Cluster](https://github.com/asankaSovis/Beowulf-Cluster-Setup-Tutorial). | Der er 16 maskiner der mangler at blive satop, noget netboot iPXE alla: [netboot.xyz](https://hub.docker.com/r/netbootxyz/netbootxyz) |
| Tirsdag - 01.04.2025 | @migsej har fået mpirun til at virke ved at give public keys til mpiuser og ikke root brugeren :\| N/A | 
| Onsdag - 02.04.2025 | Vi har forsøgt at få netboot.xyz til at virke sammen med [dnsmasq](https://netboot.xyz/docs/docker/dhcp/), vi kan få dell computerne til at ramme vores DHCP server men den står og hænger, dnsmasq smider også nogle fejl i journalctl. | Finde ud af hvorfor dnsmasq ikkr virker :( |
