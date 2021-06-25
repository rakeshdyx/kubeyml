## Linux Networking

```
iptables -nvL -t nat - to check the iptables set by docker.
```
---
# CNI(Container Runtime Interface)
- Conatiner runtime must create a network namespace
- Identify network the conatiner must attach to
- Conatiner Runtime to invoke Network Plugin (bridge) when conatiner is ADDed
- Conatiner Runtime to invoke Network Plugin (bridge) when conatiner is DELeted
- JSON format of the Network Configuration
- Must support command line arguments Add/Del/Check
- Must support parameter conatiner id, network ns etc.
- Must manage IP address assignment to PODs
- Must Return results in a specific format
  - However docker doesn’t support CNI, docker has its own container network model(CNM) same as CNI with some differences.
  - When k8 cluster runs a conatiner in docker runtime, by default it set --network=none and later it assign a bridge to the container.

* Example *

```
docker run --network=none nginx
bridge add 2e34dcf34 /var/run/netns/2e34dcf34
```
---
# Pod Networking