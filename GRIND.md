Date - 2026-09-29
Subject - Network
Topic - IP addressing, binary, CIDR/subnetting fundamentals

Commands - sudo apt install -y ipcalc, ipcalc 

Keywords - IPv4, binary, CIDR, subnet mask, network address, broadcast address, host bits, usable hosts

Brief -
Learned IPv4 structure (32 bits, 4 octets) and how binary maps to decimal, plus how network and host portions split based on the mask.

Learned the core formulas: total = 2^(32-n), usable = total - 2 (AWS: total - 5), and block size = 256 - last mask octet.

Solved 6 practice questions by hand: finding last usable address across single and multi-octet block sizes, and checking whether an IP falls inside a given subnet, all correct.

Installed ipcalc and verified my manual math against its output for 172.31.16.0/20 - exact match on network, broadcast, and host range.

Covered the difference between reading/calculating a given subnet (done, solid) versus VLSM/splitting a network into multiple subnets (not yet covered).

Next: VLSM (splitting one network into multiple subnets, equal and unequal sizes) and applying this to AWS VPC subnet design.

-----------------

Date - 2026-09-30
Subject - Network
Topic - OSI/TCP-IP model, LAN/WAN/WLAN, protocols, VLSM, Layer 2 intro

Commands - ipcalc <ip/cidr> (verification only, no new commands run this session)

Keywords - OSI, TCP/IP, encapsulation, VLSM, LAN, WAN, WLAN, frame, MAC, ARP, broadcast, switch

Brief -
Learned the OSI 7-layer model and the TCP/IP 4-layer model, how they map to each other, and that OSI is theoretical/teaching while TCP/IP is what's actually implemented.

Learned encapsulation: data is wrapped going down the layers on send, and unwrapped going up on receive, one direction per message, not a back-and-forth object.

Solved a full VLSM split by hand for 192.168.0.0/24 with requirements 60, 25, 10, 5 — correct sizing, no overlap, sequential allocation, with leftover space flagged as intentional growth room.

Corrected several assumptions: subnet size limits deployable devices, not website visitors; HTTP specifically is request/response by protocol design, but not all protocols guarantee a response (UDP sends without confirmation, TCP/HTTP do).

Covered LAN/WAN/WLAN as scope terms, not new protocols, and mapped them to AWS (VPC = private LAN, Direct Connect/VPN = WAN link).

Started Layer 2 basics: frame is the L2 data unit, switches forward by MAC, ARP requests are broadcasts (FF:FF:FF:FF:FF:FF) since the target MAC is unknown.

Next: finish L2 (switch MAC learning, broadcast/unicast/multicast, why ARP can't cross a router), then Layer 3 in depth.

----------------------------

Date - 2026-10-01
Subject - Network
Topic - ARP/DHCP distinction, local-segment logic, AWS Networking Basics course, scope decisions

Commands - (none run today — conceptual + course-based session)

Keywords - ARP, DHCP, local segment, broadcast, subnet vs visitor capacity, asymmetric encryption, AWS Skill Builder

Brief -
Corrected a mix-up: ARP resolves a known IP to a MAC, only on the local segment — it does not assign IPs, and it never crosses a router. DHCP assigns IPs.

Worked through the Mohammed Residence example (shared public IP, separate private IP/MAC per device) and confirmed only the device with the matching IP replies to an ARP broadcast, others stay silent.

Reconfirmed that subnet size limits how many devices can be deployed in a network, not how many visitors a server can handle — two separate, unrelated mechanisms.

Decided to stop going CCNA-depth on Layer 2 (frame structure, collision domains) and skip GNS3 entirely, since neither transfers to the AWS/DevOps path; sticking with Multipass for Linux and real AWS for cloud networking.

Clarified asymmetric encryption (public/private key pairs), tying it back to SSH key auth from earlier.

Completed AWS Skill Builder's "AWS Networking Basics" course, certificate earned (Oct 1, 2026); also completed TryHackMe Pre Security — Computer Fundamentals, "Inside a Computer System" room.

Next: GitHub repo setup (pushed to tomorrow), then TCP/UDP to continue the networking fundamentals track.

--------------------------

Date - 2026-10-02
Subject - Network
Topic - Switch vs Router, Gateway/Route Tables, TCP/UDP + Ports, GitHub repo discovery

Commands - ip route, ifconfig en0 / ipconfig getifaddr en0, ss -tulpn, curl -v http://example.com, git remote -v

Keywords - switch, router, route table, default gateway, MAC-hop rule, TCP, UDP, ports, 3-way handshake, git

Brief -
Learned switch (L2, MAC-based, same network) vs router (L3, IP-based, between networks), and locked in the MAC-hop rule: only adjacent devices learn each other's MAC, never further down a chain — verified with the Ali-Mohammed-Taha-Omer example.

Learned ARP and switch are sequential, not duplicate: ARP finds the MAC first, the switch then delivers using it.

Proved the gateway/route table concept live — ran ip route on dev-ubuntu (gateway 192.168.64.1, matching my earlier prediction) and checked real IPs on my phone and Mac's WiFi (192.168.29.x), confirming my Mac runs two separate networks at once: home WiFi and Multipass's private VM network.

Corrected a mix-up: route tables are each router's own local rulebook, not a full map of the journey — no single device knows the whole path.

Learned TCP (reliable, ordered, handshake-based) vs UDP (fast, no confirmation) and ports (app-level addressing on top of IP); verified live with ss -tulpn (SSH on port 22, DNS on 53, DHCP client on 68) and curl -v (watched DNS resolution, TCP connect, HTTP request/response in sequence).

Corrected a repeated mix-up: TCP provides reliability, not security — SSH's actual security (encryption) is a separate layer on top of TCP, not a TCP feature itself.

Found my actual local repo at ~/desktop/devops/careerpath (GRIND.md inside), confirmed via git remote -v that it isn't a git repo yet. Next: git init, .gitignore, connect to a new GitHub repo, first push — picking up tomorrow from git init.

-------------------------------------

Date - 2026-10-04
Subject - GitHub
Topic - Repo setup and authentication for career_path

Commands - git init, git remote add origin, git add, git commit, git config pull.rebase false, git pull --allow-unrelated-histories, git push -u origin main, git branch -M main

Keywords - git init, remote, personal access token, merge, divergent histories, gitignore

Brief -
Spent today entirely on GitHub setup, not networking content, walking through it step by step with Claude so the whole process is recorded as proof of doing it myself. Initialized git locally in the existing careerpath folder, connected it to the GitHub repo via git remote add origin, and verified the connection with git remote -v before trusting it.

Created .gitignore (pem, env, tfstate, terraform folder, plus DS_Store after catching it in git status) and committed GRIND.md and .gitignore as the first local commit.

Hit a real auth wall: GitHub no longer accepts password auth over HTTPS, resolved by generating a Personal Access Token (classic, repo scope) and using it as the push password.

Hit a real push rejection (divergent histories, since GitHub had old README commits my local repo didn't know about), resolved by setting pull.rebase false and running git pull --allow-unrelated-histories, then completing the merge commit in Vim.

Successfully pushed — GRIND.md and .gitignore now live on GitHub at invicx/career_path, confirmed by the commit hash change (dd36915 to 7b8e494).

No networking or Linux content learned today — purely infrastructure/tooling setup. Going forward, daily logging is just: edit GRIND.md, git add ., git commit, git push.

Next: resume networking (or Linux) content next session; watching a GitHub overview video for consolidation before then.

---------------------------