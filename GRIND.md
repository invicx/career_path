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

Date - 2026-10-03
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

Date - 2026-10-05
Subject - Network
Topic - DNS (full), HTTP/HTTPS/TLS, live terminal proof across multiple real sites

Commands - dig google.com, dig google.com MX/NS/TXT, dig github.com A/NS, curl -v https://google.com , curl -v https://invicx.github.io/barca-quiz/, curl https://api.github.com/repos/invicx/career_path, python3 -m http.server 8080, curl http://localhost:8080, ss -tulpn

Keywords - DNS, resolver, TTL, root, TLD, authoritative, A record, NS record, 5-tuple, TLS handshake, certificate, HTTP methods, status codes, localhost, port 8080

Brief -
Finished DNS end to end: the Root → TLD → Authoritative chain, the resolver's role (local resolver forwards to a recursive resolver, which walks the chain), and TTL as the cache expiry controlling how long an answer is reused before a fresh lookup.

Ran dig live multiple times — google.com (A record, TTL), github.com (A record, then NS records showing GitHub uses BOTH AWS Route 53 and NS1 simultaneously for reliability and availability, not just raw redundancy).

Covered the 5-tuple (source IP/port, dest IP/port, protocol) as what uniquely identifies one connection, explaining how multiple browser tabs to the same site stay distinguishable.

Covered ports in depth: well-known vs registered vs ephemeral ranges, and built a DevOps port cheat sheet (22, 80, 443, 53, 67/68, 3306, 5432, 6379, 27017, 8080, 179, etc.).

Covered HTTP/HTTPS/TLS: the TLS handshake sequence (Client Hello, Server Hello, Certificate, Cert Verify, Finished) matched to real curl -v output, what a certificate actually proves (identity + encryption, via a trusted CA), and the HTTP status code families (2xx/3xx/4xx/5xx).

Proved the full DNS → TCP → TLS → HTTP chain live, three times, on three real targets: example.com, google.com, and my own GitHub Pages site (invicx.github.io/barca-quiz/, got a real 200 OK with my own deployed HTML).

Covered HTTP methods (GET/POST/PUT/DELETE/PATCH) and where they're actually used in DevOps — mainly troubleshooting and automation scripts, since most tools (AWS CLI, Terraform) send these internally without me typing them directly.

Ran a live local server (python3 -m http.server 8080) and hit it with curl http://localhost:8080 — connected a real "connection refused" vs "working" comparison to the concept of a port only responding when something is actively listening on it.

Covered reserved IP ranges as a side topic: private (10/8, 172.16/12, 192.168/16), loopback (127/8), APIPA (169.254/16), and documentation/testing ranges (192.0.2.0/24 etc.), plus CGNAT.

Self-identified real gaps during a mixed quiz: answered the 5-tuple instead of the actual DNS resolution flow when asked, said DNS uses "both" TCP and UDP without the nuance (primarily UDP, TCP only for larger responses) despite it being visible in my own dig output, and skipped two questions (NXDOMAIN meaning, TTL propagation delay) — flagged honestly rather than glossed over.

Dense, long session — DNS fully closed, HTTP/HTTPS/TLS mostly closed (status code drilling and localhost/port concept still settling, to continue tomorrow).

Next: finish settling HTTP status codes + localhost/port concept, then NAT, then Security Groups vs NACLs, then the full VPC build.

-----------------------------------------------------------------

Date - 2026-10-06
Subject - Network + AWS
Topic - HTTP status codes live testing, Flask multi-method API build, GitHub project workflow, AWS Skill Builder progress

Commands - curl -I https://httpbin.org/status/<code>, pip install flask --break-system-packages, python3 app.py, curl -X GET/POST/PUT/DELETE/PATCH, ss -tulpn, multipass transfer, curl ipinfo.io

Keywords - HTTP status codes, flag, framework, port, localhost, HTTP methods, Flask, multipass transfer, NAT (queued for tomorrow)

Brief -
Pushed Oct 5's log entry to GitHub (DNS, HTTP/HTTPS/TLS), confirming the daily add/commit/push flow works cleanly now with no setup friction.

Closed out HTTP status codes live — ran 200, 404, 500, 502 against httpbin.org after httpstat.us unexpectedly failed; confirmed all 4 ranges (success, client error, server error variants) with real responses.

Clarified core terms along the way: flag (a command modifier like -I or -v), framework (pre-built structure handling repetitive work, e.g. Flask), port (arbitrary dev ports like 5000/3000/8080/6503, none reserved, just convention), and localhost (127.0.0.1, your own machine talking to itself).

Built a real Flask API from zero prior Flask knowledge, specifically to understand what each HTTP method does behind the scenes — GET, POST, PUT, DELETE, PATCH all implemented as separate routes, each returning a distinct response.

Ran and tested the app inside Dev (multipass VM) first, confirmed all 5 methods working via curl from Mac, with matching server-side logs (200 OK) visible in Dev's terminal — proof from both the client and server side.

Transferred app.py from Dev to Mac using multipass transfer, wrote a full project README (what it does, how to run/test it, what was learned, plus an honest process note about learning Flask from scratch with AI guidance), committed and pushed the project to GitHub under projects/flask_hello_world.

Also added a root README.md to the career_path repo, giving the repo actual context (background, motivation, file structure) instead of a blank page.

Covered NAT conceptually — private-to-public IP translation, the translation table mechanism, and the AWS NAT Gateway vs Internet Gateway distinction — but did not finish or test hands-on; explicitly deferred to continue tomorrow.

Continued AWS Skill Builder: Networking Core - Knowledge Badge Readiness Path (pre-assessment and AWS Networking Basics both complete, 25 trainings remaining) and AWS Cloud Practitioner Essentials (Module 1 complete, Module 2 - Compute in the Cloud in progress). Clarified that these are free completion courses, not the same as the paid official AWS certifications (CCP, SAA) — the free courses are prep material, not the credential itself.

Next: finish NAT (hands-on proof via curl ipinfo.io vs private IP), then Security Groups vs NACLs, then the full VPC build.

---------------------------------------------------------

Date - 2026-10-07

Subject - Network + AWS

Topic - VPC architecture diagram to static file

Commands - none

Keywords - SVG, static asset, hardcoded colors, widget vs file, portability

Brief -
Converted the single-AZ VPC diagram built earlier (IGW, VPC 10.10.0.0/16, public subnet with bastion + NAT, private subnet with app + DB, NACL/SG placement) from a live in-chat widget into an actual standalone .svg file.

Learned the practical gap between a rendered widget and a real file: the widget leans on the chat environment's CSS variables for color, so it won't display correctly anywhere else — GitHub, a browser, etc. Fixing that meant hardcoding every fill/stroke as explicit hex values so the file renders correctly on its own.

Saved it locally for now — plan is to drop it into an end-to-end project later rather than commit it standalone.

Next: Linux and Quiz.

------------------------------------

Date - 2026-10-08

Subject - Network Review + Linux

Topic - Full networking knowledge check (2 quiz rounds), closing the networking chapter, Linux overview and filesystem hierarchy

Commands - ls -la /var/log, sudo tail /var/log/auth.log

Keywords - quiz, knowledge check, ARP vs DNS, stateful vs stateless, filesystem hierarchy, /etc /var /home /proc, log rotation, auth.log, Linux roadmap

Brief -
Took two 20-question quiz rounds covering everything from the networking chapter — OSI/TCP-IP, ARP, CIDR, routing, TCP/UDP, DNS, HTTP, NAT, bastion, SG vs NACL, plus Flask/HTTP methods and the Git workflow. Scored 17/20 and 16/20. Misses were mostly role confusion between similar mechanisms (ARP vs DNS, route tables vs SG/NACL) rather than not knowing the material — one answer (NACL statelessness) was a known-answer slip from reading the question too fast, not a real gap.

Called networking chapter closed for now — fundamentals are solid enough to build on, deeper clarity will come when actually deploying the VPC later.

Moved into Linux. Covered what Linux actually is, why it matters for DevOps specifically (it's what the infrastructure runs on, scriptable, transparent), and the core pieces (kernel, shell, filesystem, processes, permissions, package manager). Went deep on the filesystem hierarchy — /etc, /var, /home, /proc, /bin, /tmp — then applied it live by running ls -la /var/log on the VM and walking through real output: log rotation pattern (.1, .2.gz...), what each log file is for (syslog, auth.log, kern.log, dpkg.log, cloud-init.log, wtmp/btmp), and why auth.log has restricted permissions.

Built a full Linux Tier 1+2 checklist (14 sections, tagged, filesystem through scripting/cron/storage) as a Word and PDF doc. Actual daily commitment is 3hrs minimum (not 1hr as originally estimated) — at that pace, full checklist clears in ~6-8 days rather than 16-19. Flagged that compressing to 6-8 days covers everything once but scripting/text-processing need repetition to actually stick, not just a single pass.

Next: File Viewing & Editing (cat/less/tail -f, nano/vim basics), then Permissions.

-----------------------------------------------

Date - 2026-10-10

Subject - Linux

Topic - Filesystem & Navigation: paths, directory switching, listing files, and basic file operations

Commands - `pwd`, `cd ~`, `cd ..`, `cd -`, `mkdir -p`, `touch`, `ls`, `ls -l`, `cp`, `mv` (reviewed and discussed)

Keywords - absolute vs relative paths, `$HOME`, `cd -`, parent directory, `mkdir`, `touch`, `ls -l`, file vs directory, `cp`, `mv`, `rm`, `rmdir`, recursive deletion, force flag

Brief -

Continued Linux filesystem and navigation practice inside the Dev Ubuntu Multipass VM. Reviewed nested directory structures, absolute vs relative paths, and the difference between moving to a parent directory with `cd ..` and switching to the previous working directory with `cd -`.

Verified `cd -` by switching between `~/practice/level1/level2` and `~/practice/level1/level2/level3`. Connected the concept to macOS Cmd+Tab as an analogy for switching between previous contexts, while noting that the actual operations are different.

Reviewed `ls` options and identified the leading `d` in `ls -l` output as a directory and `-` as a regular file. Discussed how terminal colours can also distinguish file types, depending on configuration.

Created and inspected `original.txt` inside `~/practice/files`, then confirmed that `copy.txt` existed alongside it. Reviewed `cp` as copying while preserving the original, and `mv` as a command used both for renaming and moving files or directories.

Covered `mkdir` vs `touch`, and the difference between `rm` and `rmdir`. Clarified that `rmdir` removes empty directories, `rm -r` recursively removes a directory and its contents, and `rm -f` forces removal while suppressing many prompts and errors. The combined `rm -rf` example was discussed but deliberately left for the next session; it was not executed.

**Epiphanies / Key Realizations**

- `cd -` switches between the current and previous working directories, whereas `cd ..` follows the directory hierarchy upward.
- `$HOME` refers to the home directory, while `pwd` reports the current working directory; they can match at the home directory but differ after navigating elsewhere.
- `mkdir` creates directories; `touch` creates an empty file if it doesn't exist.
- `cp` preserves the original, whereas `mv` renames or relocates it.
- The `-r` flag means recursive; `-f` means force. They serve different purposes and should not be confused.

Next - Continue filesystem file operations: verify moving files into `archive`, practise `rmdir` with an empty directory, and run the disposable `demo` example to compare `rm -r` and `rm -rf`. Then continue through `find`, hard vs symbolic links, and filesystem hierarchy review.

--------------------------------

Date - 2026-10-11

Subject - Linux

Topic - Filesystem & Navigation: directory listings, paths, copying, moving, and deletion

Commands - `ls -la`, `ls -R`, `pwd`, `cd`, `mkdir -p`, `cp`, `mv`, `rm`, `rmdir`, `rm -r`, `wc -l`

Keywords - filesystem hierarchy, hidden files, long listing, recursive listing, absolute path, relative path, `$HOME`, `pwd`, copy vs move, empty directory, recursive deletion, force deletion

Brief -

Continued Section 1 (Filesystem & Navigation) of the Linux Mastery Checklist, focusing on understanding command behaviour and predicting outcomes rather than repeating commands already understood.

Reviewed directory listings: `ls -la` combines hidden entries (`-a`) with detailed metadata (`-l`), while `ls -R` recursively displays directory contents. Clarified that recursion comes from `-R`, not `-la`.

Revisited absolute vs relative paths, `$HOME` vs `pwd`, and navigation using `cd`. Also discussed counting directory entries with `ls /bin | wc -l` and noted that `/bin` is commonly linked to `/usr/bin` on modern Ubuntu.

Connected the Linux filesystem hierarchy to Tech Support troubleshooting: `/etc/ssh/` contains SSH configuration, `/var/log/` contains logs, and `systemctl status ssh` can help check whether the SSH service is running. Deeper log interpretation and service troubleshooting remain for their relevant checklist sections.

Reviewed file operations: `cp` creates a copy while retaining the original; `mv` moves or renames an entry. Correctly predicted that moving `copy.txt` into `archive/` leaves the original file in place.

Clarified deletion behaviour through a scenario: `rmdir` only removes empty directories; `rm` removes files; `rm -r` removes directories and their contents recursively. Corrected the mistaken command `rmdir -r` — recursive directory deletion uses `rm -r`, not `rmdir -r`. Discussed `rm -rf` and why forceful recursive deletion requires extra caution.

Epiphanies / Key Realizations -

- `-a`, `-l`, and `-R` do different jobs: show hidden entries, show detailed metadata, and traverse nested directories, respectively.
- The choice between `rm` and `rmdir` depends on whether the target is a file or an empty directory. Recursive deletion is a separate operation.
- Linux filesystem knowledge becomes more useful for Tech Support when directory purpose is connected to a troubleshooting question: configuration in `/etc`, logs in `/var/log`, and service state through `systemctl`.

Next -

Continue Section 1 with `find` — locating files by name, type, size, and modification time. Then cover symbolic and hard links and review the remaining filesystem hierarchy items. Resume the pending hands-on deletion exercise only if needed; the core `rm` vs `rmdir` behaviour was already reasoned through. Move to File Viewing & Editing only after completing the current checklist section.

---------------------------------------

Date - 2026-10-12

Subject - Linux

Topic - Filesystem & Navigation: `find`, hard links vs symbolic links, filesystem hierarchy, and introduction to file viewing

Commands - `find` by name/type/size/mtime, `find -newer`, `ln`, `ln -s`, `ls -li`, `cat`, `touch`, `sleep`, `echo`, `printf`, `seq`, `less`, `cd /`

Keywords - `find`, `-name`, `-type`, `-size`, `-mmin`, `-mtime`, `-newer`, inode, hard link, symbolic link, dangling symlink, filesystem hierarchy, `/etc`, `/var/log`, `/home`, `/proc`, `printf`, `less`

Brief -

Continued Linux filesystem practice on the Dev Ubuntu VM. Practised searching files by name, type, size, and modification time. Explored `find -newer` and confirmed that it requires a reference filename; files modified later than the reference are returned. Investigated modification-time search boundaries using `-mmin`.

Created and inspected a hard link with `ln`, confirming that it shared the original file's inode. Created a symbolic link with `ln -s` and confirmed it had a separate inode. Tested deletion behaviour using separate test files: the hard link remained readable after deleting its target filename, while the symbolic link remained present but became dangling because its target path no longer existed.

Discussed practical security and recovery implications of links, including inode searches with `find -inum` and the limitations of relying on logs alone. Explored the Linux filesystem hierarchy and correctly identified `/etc` for configuration, `/var/log` for logs, and `/proc` for live process and kernel information.

Started File Viewing & Editing. Compared `echo` and `printf`, created `notes.txt` using `printf`, and created `longfile.txt` with `seq 1 30`. Opened the file using `less` and reviewed navigation/search keys: Space, `b`, arrow keys, `g`, `G`, `/pattern`, `n`, and `q`.

Epiphanies / Key Realizations -

- A hard link is another directory entry for the same inode; a symbolic link is a separate filesystem object storing a path.
- Deleting a target filename does not necessarily delete its data if another hard link remains. A symbolic link can survive while becoming dangling.
- `find -newer filename` compares modification times against a reference file; it does not search for a file named `filename`.
- Logs can help investigate file operations, but Linux does not automatically audit every deletion or link creation.
- `printf` offers predictable formatting, while `echo` is convenient for simple output.
- `less` is useful for navigating large files and logs without dumping their entire contents.

Next -

Finish File Viewing & Editing: practise `head`, `tail`, and `tail -f`; learn basic `nano`/`vim` editing and saving; compare files using `diff`. Continue through the Linux Tier 1 + Tier 2 checklist, then build at least two practical Linux projects before moving deeper into AWS.

-------------------------------

Date - 2026-10-13

Subject - Linux

Topic - File Viewing & Editing, Permissions & Ownership, introduction to grep

Commands - `diff`, `chmod`, `umask`, `ls -l`, `ls -ld`, `grep`, `echo $?`

Keywords - file comparison, rwx, octal permissions, symbolic permissions, ownership, `sudo`, `umask`, `grep`, regex anchors, exit status

Brief -

Reviewed `diff` by comparing two files and observing how changes affect its output. Covered numeric and symbolic permissions, ownership commands (`chown`, `chgrp`), `sudo` vs root, and `umask`. Verified `umask` was `0002`, producing permissions of `664` for a new file and `775` for a new directory.

Started text processing with `grep`: case sensitivity, line numbers, inverted matches, recursive searching, and the `^` beginning-of-line anchor. Verified `$?` returns `0` for success and `1` when the tested grep search finds no match. A search for errors in `/var/log/syslog` returned no output; the reason was not confirmed.

Reviewed `tail -f`, basic Vim save/quit keys, and `diff`. Deeper grep and regex practice remain unfinished.

Epiphanies / Key Realizations -

- `umask` affects permissions on new files and directories, not existing ones.
- `chmod +x` adds execute permission across all categories by default; `chmod a+x` makes this explicit.
- `grep -v` excludes matching lines; `-i` makes matching case-insensitive.
- `grep -r` searches directory trees, while `^` matches the start of a line.
- A grep exit status of `1` commonly means no match, not necessarily an execution error.

Next -

Continue Section 4 (Text Processing) with a dedicated grep lab. Practise regex anchors, character classes, alternatives, repetition, and word boundaries before moving on to `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, pipes/redirection, and `xargs`. Inspect `archive/` and `demo/` before cleaning up practice files.

----------------------------

Date - 2026-10-14

Subject - Linux Text Processing

Topic - grep, cut, sort, uniq, wc, sed, basic awk, pipes and file management.

Commands -
- `grep`: `-i`, `-n`, `-c`, `-v`, `-E`, `-r`
- `cut -d' ' -f1 users.log`
- `sort -k3,3 -k2,2`
- `uniq`, `uniq -c`, `uniq -d`, `uniq -u`
- `wc -l`, `wc -w`, `wc -c`
- `sed 's/old/new/g' file`
- `awk '{print $1, $4}' users.log`
- `awk -F'[ =]' '{print $2, $8}' users.log`
- Pipes `|`, chaining `&&`, redirection `>` and `>>`
- `find`, `mkdir`, `mv`, `rm`, `rmdir`, `ls -lah`

Keywords - Text processing, field extraction, sorting, deduplication, substitution, awk field separators, pipes, redirection.

Brief - Practised Linux text-processing commands on log and user datasets. Learned to extract fields, sort by multiple keys, count duplicates, count lines/words/bytes, substitute text with sed, and extract usernames and statuses using awk. Reviewed command pipelines and file management.

Epiphanies / Key Realizations -
- `uniq` works on adjacent duplicate lines; combine with `sort`.
- `sed` prints transformed output by default without modifying the original.
- `awk` can extract and rearrange fields using field numbers and custom separators.
- Pipes pass output between commands for successive processing.

Next - Complete awk with practical exercises, cover redirection and xargs, practise find + grep, then take the combined Linux Sections 1–4 test.

---------------------------------

Date - 2026-10-15

Subject - Linux Text Processing

Topic - awk, redirection, pipes, xargs, find + grep, Sections 1–4 practical

Commands -
`grep -i`, `grep -in`, `awk -F'[ =]'`, `wc -l`, `find`, `xargs`, `ls -l`, `cat`, `echo`, `>`, `>>`, `<`, `&&`

Keywords - awk fields, filtering, stdin/stdout, redirection, command-line arguments, process pipelines

Brief - Completed practical awk filtering using multiple conditions, extracted usernames and statuses, and practised output redirection and line counting. Used `find` with `xargs` to pass filenames to commands. Completed 9 combined practical tasks covering grep, awk, redirection, counting, and file discovery. Encountered a grep input/output conflict when searching files while redirecting results into one of the searched files.

Epiphanies / Key Realizations -
- `find` locates files; `xargs` passes their paths as command-line arguments.
- `awk` filters records and extracts fields using separators and conditions.
- `>` overwrites, `>>` appends, and `<` supplies standard input.
- Pipes pass output to stdin; not every command reads stdin.

Next - Complete the remaining Sections 1–4 practicals and cover `sed`, `cut`, `sort`, and `uniq` gaps. Then begin process and system-resource monitoring with `ps`, `top`, `free`, `df`, and related commands.

------------------------------

Date - 2026-10-16

Subject - Linux

Topic - Final Practical Assessment: Linux Fundamentals and Text Processing

Environment - Ubuntu Multipass VM

Sections Covered
1. Filesystem & Navigation
2. File Viewing & Editing
3. Permissions & Ownership
4. Text Processing (Core Tier 2 Differentiator)

Test Format - 8-task integrated practical assessment

Marks - 7.5/8 (approximately 94%, mentor-assessed)

Brief -

Completed an eight-task practical assessment covering log analysis, filtering, field extraction, counting, file discovery, output redirection, report generation, and file permissions. Troubleshot command errors and verified results through terminal output.

Performance Review -

Demonstrated good command composition and persistence. Most tasks were completed successfully, although some required retries and hints. Output ordering, command side effects, and reading every requirement carefully need improvement.

Mentor's Opinion -

Ali is progressing from beginner toward intermediate Linux command-line work. The strongest quality shown was persistence: when commands failed or produced unexpected results, he kept investigating instead of giving up. He is beginning to combine commands logically rather than memorising isolated syntax. The next step is improving accuracy and consistency while revisiting checklist topics not fully tested.

Result - Practical assessment completed. Ready to progress, with some fundamentals still requiring additional practice.

Next - Section 5: Processes & System Resources.

------------------------------------

Date - 2026-10-17

Subject - Linux

Topic - Processes & System Resources: process inspection, signals, job control, and disk usage (Section 5 — in progress)

Commands - `ps aux`, `ps -ef`, `ps -o`, `top`, `htop`, `yes > /dev/null &`, `kill`, `kill -15`, `kill -9`, `sleep`, `jobs`, `jobs -l`, `bg`, `fg`, `nohup`, `df -h`, `multipass info dev-ubuntu`

Keywords - PID vs job ID, process states, CPU usage, memory usage, SIGTERM, SIGKILL, SIGHUP, foreground vs background, job control, `nohup`, filesystem capacity, virtual disk

Brief -

Continued Linux Mastery Checklist Section 5 inside the Ubuntu 24.04.3 LTS Multipass VM. Practised process inspection with `ps aux` and `ps -ef`, customized output with `ps -o`, sorted processes by CPU and memory usage, and compared `ps` snapshots with the continuously updating `top` and `htop` monitors.

Created a CPU-heavy process using `yes > /dev/null &` and terminated it with `kill %1`. Practised terminating `sleep` processes with `kill`, `kill -15`, and `kill -9`. Learned about process states, including running, sleeping, stopped, and zombie processes, and corrected a `ps -o` formatting error caused by using an invalid uppercase field name.

Practised job control using `sleep 300 &`, `jobs`, `Ctrl+Z`, `bg`, `jobs -l`, and process IDs. Explored `nohup sleep 300 &` and inspected the running process. Discussed `killall` and why indiscriminately terminating processes by name can be risky. Actual survival after terminal disconnection was not tested.

Used `df -h` to inspect disk capacity inside the VM. The root filesystem showed approximately 3.9 GB total, 2.7 GB used, 1.2 GB available, and 69% usage. Compared this with `multipass info dev-ubuntu` on macOS, which reported 2.7 GiB disk usage out of 4.8 GiB and approximately 247.5 MiB memory usage out of 951.9 MiB.

Epiphanies / Key Realizations

- `ps` provides a snapshot, while `top` and `htop` continuously update process information.
- A PID identifies a process, while a job ID identifies a job managed by the current shell.
- `kill` sends a signal: SIGTERM requests graceful termination, while SIGKILL forces termination.
- `Ctrl+C` interrupts a foreground process; `Ctrl+Z` suspends it; `bg` resumes it in the background, and `fg` brings it back to the foreground.
- `nohup` ignores SIGHUP but does not guarantee survival through VM shutdown.
- `df -h` reports filesystem capacity, which is different from the virtual disk capacity reported by Multipass.

Next - Continue Section 5 by practising `du -sh`, `free -h`, and `uptime`. Understand load averages and complete the remaining checklist items before moving to Section 6.

-------------------------------------

Date - 2026-10-19

Subject - Linux

Topic - Services & systemd: service management, journalctl, and unit files

Commands - `systemctl status`, `start`, `stop`, `restart`, `enable`, `disable`, `is-active`, `is-enabled`, `systemctl cat`, `journalctl -u`, `-f`, `--since`, `--until`, `--no-pager`, `sudo apt update`, `sudo apt upgrade`

Keywords - systemd, services, units, SSH, socket activation, cron, journal logs, timestamps, `ExecStart`, `EnvironmentFile`, `Restart=on-failure`, boot targets, troubleshooting

Brief -

Practised managing the Cron service: checking status, starting, stopping, restarting, enabling, and disabling it. Restored the service and verified its state.

Investigated SSH socket activation and used `journalctl` to examine service events, follow live logs, and filter by time. Compared journal evidence with shell history to understand how administrators investigate incidents.

Updated Ubuntu packages, rebooted the VM to load the updated kernel, and verified that no packages remained upgradable.

Epiphanies / Key Realizations

- Service state and automatic startup configuration are separate.
- Journal logs and shell history provide evidence, not definitive proof of causation.
- A systemd unit file defines how systemd manages a service.
- Recognising command output is only the first step; deeper understanding requires practice.

Next - Writing a basic .service unit file #systemd, Understanding boot targets at a conceptual level

-----------------------------

Date - 2026-10-20

Subject - Linux

Topic - Users, Groups & Sudo: account management, account files, and privilege escalation

Commands - `whoami`, `id`, `groups`, `getent passwd`, `getent group`, `cat /etc/passwd`, `grep`, `tail`, `sudo -l`, `sudo whoami`, `sudo -i`, `su -`, `useradd`, `usermod`, `userdel`, `groupadd`, `visudo`, `mkdir`, `chown`, `chmod`, `rm -r`

Keywords - users, groups, UID, GID, primary group, supplementary groups, `/etc/passwd`, `/etc/group`, `/etc/shadow`, `/etc/sudoers`, `visudo`, sudo, root, home directories, account deletion, permissions

Brief -

Practised inspecting user accounts, IDs, group memberships, and account records. Examined the roles of `/etc/passwd`, `/etc/group`, and `/etc/shadow`, including where password information is stored.

Compared `sudo` and `su`, checked sudo privileges, and explored how `useradd`, `usermod`, and `userdel` manage accounts. Practised understanding home-directory creation, ownership, permissions, and the difference between deleting an account and removing its home directory.

Discussed the risks of recursive deletion and why destructive commands must be handled carefully.

Epiphanies / Key Realizations

- `/etc/passwd` stores account records; password hashes are generally stored in `/etc/shadow`.
- A user has a primary group and may have supplementary groups.
- `sudo` elevates an individual command, while `sudo -i` opens a root shell.
- `userdel` and `userdel -r` differ in whether removal of the home directory and mail spool is attempted.
- Account configuration, group membership, and filesystem permissions are related but distinct.
- Destructive commands can damage the system; understanding the target path and command options matters.

Next - Networking-as-Troubleshooting: inspect network interfaces with `ip addr` #networking #ts

----------------------------------------------

Date - 2026-10-22

Subject - Linux

Topic - Networking-as-Troubleshooting: interfaces, routing, ICMP, DNS, ARP and Ethernet frames

Commands - `ip addr`, `ip route`, `ping -c 4 192.168.64.1`, `ping -c 4 8.8.8.8`, `ping -c 10 192.168.1.10`, `getent hosts google.com`, `ip route get 192.168.1.10`, `ip route get 192.168.64.1`, `ip neigh`, `ip neigh show 192.168.64.1`

Keywords - Networking, network interface, IPv4, IPv6, subnet, CIDR, default gateway, routing table, packet, Ethernet frame, MAC address, ARP, NDP, ICMP, ping, packet loss, TTL, hop limit, DNS, TLD, neighbour table, next hop

Brief -

- Inspected network interfaces using `ip addr`, identifying loopback (`lo`) and the VM's virtual interface (`enp0s1`).
- Read the routing table using `ip route` and identified the VM's IP (`192.168.64.2`), subnet (`192.168.64.0/24`) and default gateway (`192.168.64.1`).
- Used `ping` to test gateway and external IP connectivity. Investigated 100% packet loss when testing an example address outside the VM's subnet.
- Used `ip route get` to compare direct local-subnet routing with routing through the default gateway.
- Used `getent hosts google.com` to verify hostname resolution through the system's configured name-resolution mechanism.
- Inspected the neighbour table with `ip neigh`, identifying the gateway's MAC address and learning about IPv4 ARP, IPv6 NDP, and `REACHABLE` versus `STALE` neighbour states.
- Connected the concepts of IP packets, Ethernet frames, MAC addresses, network interfaces, routers and next-hop forwarding.

Epiphanies / Key Realizations

- A network interface is the connection point; an IP address is assigned to it.
- Linux uses its routing table to choose a destination route and outgoing interface.
- Local-subnet traffic normally goes directly to the destination, while traffic to other networks uses a router.
- ARP resolves local IPv4 neighbours to link-layer addresses; IPv6 uses NDP.
- IP packets travel across networks, while link-layer frames carry them across individual links. MAC addresses are rewritten at routed hops.
- ICMP supports diagnostics and error messages. TTL limits IPv4 packet forwarding; IPv6 uses a Hop Limit.
- DNS resolution, IP reachability and application connectivity are separate things.

Next - Continue Networking-as-Troubleshooting in a natural learning order: inspect packet paths with `tracepath`, then deepen the understanding of local delivery and neighbour discovery before progressing into DNS configuration, TCP/UDP, ports, listening services and connectivity troubleshooting. Reinforce concepts through hands-on exercises rather than rushing through the checklist.

-------------------------------------------------

Date - 2026-10-29

Subject - Linux

Topic - Networking-as-Troubleshooting: sockets, binding, listening ports, and HTTP diagnostics

Commands - `sudo ss -tulpn`, `python3 -m http.server 8080 --bind 127.0.0.1`, `top`, `ps aux`, `curl -v https://google.com`, `curl -I https://google.com`

Keywords - sockets, endpoints, TCP states, binding, loopback, `0.0.0.0`, ports, listening sockets, DNS resolution, TCP connection, TLS handshake, HTTP/2, response headers, HTTP 301 redirect

Brief -

Reviewed `ss -tulpn` and interpreted live output from the Ubuntu VM. Identified SSH listening on port 22, the local DNS resolver on port 53, and UDP sockets associated with DHCP.

Covered sockets and endpoints, the distinction between TCP connection states and HTTP methods, and how applications bind sockets to IP addresses and ports. Clarified that `127.0.0.1` restricts a service to loopback, while `0.0.0.0` binds it to all local IPv4 interfaces. A listening socket alone does not guarantee external reachability.

Started a Python HTTP server bound to `127.0.0.1:8080`, verified the listening socket with `ss`, and inspected process resource usage. Stopped the server after the experiment.

Used `curl -v https://google.com` to observe DNS resolution, TCP connection establishment, TLS negotiation and certificate verification, the HTTP request, and Google's HTTP/2 301 redirect to `https://www.google.com/`.

Used `curl -I https://google.com` to inspect response headers without displaying the response body. Reviewed the `location` header and the meaning of HTTP status 301.

Epiphanies / Key Realizations -

- `ss -tulpn` shows listening TCP/UDP sockets, their addresses and ports, and associated processes; it does not prove external connectivity.
- Binding associates a socket with a local IP address and port.
- `127.0.0.1` means loopback; `0.0.0.0` means all local IPv4 interfaces when binding.
- A TCP connection's state is different from an HTTP method such as GET or POST.
- `curl -v` exposes connection and protocol details; `curl -I` requests headers only.
- The observed request sequence was DNS resolution, TCP connection, TLS handshake, then HTTP request/response.
- HTTP 301 indicates a permanent redirect, with the destination supplied in the `location` header.

Next -

Continue Section 9 with `dig` and `nslookup`, then cover `nc`, `/etc/hosts`, `/etc/resolv.conf`, and `wget`. Reinforce the networking concepts through hands-on troubleshooting.

---------------------------------------

Date - 2026-10-30

Subject - Linux Networking

Topic - Networking troubleshooting: interfaces, routing, DNS, ports, and connectivity testing.

Commands -
- `ip a`, `ip route`, `ip route get <IP>`, `ip neigh`
- `ping -c <count> <host>`, `tracepath <host>`
- `ss -tulpn`, `sudo ss -tulpn`, `grep`, pipes (`|`)
- `curl`, `curl -v`, `curl -I`, `curl -L`, `curl -IL`
- `dig`, `dig A`, `dig AAAA`, `nslookup`
- `nc -vz <host> <port>`
- `python3 -m http.server <port> --bind <IP>`

Keywords -
- TCP, UDP, ICMP, DNS, IPv4, IPv6, CIDR, subnet, gateway, routing, loopback, MAC address, ARP, sockets, listening ports, TCP handshake, TLS handshake, HTTP, DNS resolver, TTL, redirects, Netcat, port numbers.

Brief -
Practised Linux networking commands and learned how to inspect network interfaces, routing decisions, neighbour tables, listening sockets, and DNS records. Used `ping` and `tracepath` to investigate connectivity, and `curl` to inspect HTTP responses, redirects, TLS details, and headers. Used `nc` to test TCP connectivity to port 443 and reviewed important ports for SSH, DNS, web traffic, databases, and DevOps infrastructure.

Epiphanies / Key Realizations -
- DNS resolution, TCP connectivity, TLS negotiation, and HTTP communication are distinct stages.
- `nc -vz` tests whether a TCP connection can be established; it does not perform a TLS handshake or send an HTTP request.
- A listening port does not automatically mean a service is reachable from outside the machine.
- `127.0.0.1` is loopback; `0.0.0.0` means all local IPv4 interfaces when used as a bind address.
- Failed ping responses do not always mean the destination machine is down.
- `dig` and `nslookup` investigate DNS; `curl` tests application-level web communication.
- Database and infrastructure management ports should not be exposed publicly without deliberate security controls.

Next -
- Learn `/etc/hosts` and how local hostname resolution works.
- Inspect `/etc/resolv.conf` and understand DNS resolver configuration.
- Learn `wget` and compare it with `curl`.
- Continue Section 9 of the Linux networking checklist.

------------------------------------------

Date - 2026-11-01

Subject - Linux Documentation & Organisation

Topic - Organising Linux command reference and networking notes.

Commands -
- No new commands practised.

Keywords -
- Linux documentation, command reference, networking cheat sheet, IPv4 subnetting, troubleshooting.

Brief -
Organised Linux learning notes into a structured reference document. Reviewed the networking section, including troubleshooting commands, IPv4 subnetting, private IP ranges, classful addressing, and important ports. The document is organised into separate tabs: Commands, Network, Exit Status, and Quick TS.

Epiphanies / Key Realizations -
- Having a structured personal reference makes revision and troubleshooting easier.
- Documentation should support practical learning, not replace it.

Next -
- Continue Section 9: inspect `/etc/hosts`.
- Study `/etc/resolv.conf`.
- Learn `wget`.
- Continue updating the Linux reference document.

-----------------------------------------------------------------