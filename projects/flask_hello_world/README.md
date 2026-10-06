# Flask Multi-Method API

A small Flask app built to understand how a web server actually works —
routes, HTTP methods, and how a process listens on a port.

Built this with zero prior Flask knowledge — the goal wasn't to learn
Flask itself, but to actually USE each HTTP method (GET, POST, PUT,
DELETE, PATCH) hands-on and see what happens behind the scenes, instead
of just reading about them.

## What it does
Responds differently depending on the HTTP method used:
- GET → retrieve data
- POST → create/send data
- PUT → update data
- DELETE → remove data
- PATCH → partially update data

## How to run

Runs on port 6503 by default. (why ? just picked a random ahh number as it says 16 bits. checked its availability as well)

## How to test

curl http://localhost:6503
curl -X POST http://localhost:6503 -d "test data"
curl -X PUT http://localhost:6503 -d "updated data"
curl -X DELETE http://localhost:6503
curl -X PATCH http://localhost:6503 -d "patched data"


## What I learned
- Flask handles HTTP parsing/routing — I just define route + method → function
- host='0.0.0.0' vs '127.0.0.1' — accepting connections from any interface vs only localhost
- Port is just a number; confirmed 6503 was free using `ss -tulpn` before using it
- Built and ran this inside a Multipass VM (dev-ubuntu), tested from my Mac over the VM's private IP (192.168.64.x)
- Each HTTP method maps to a real-world action: GET=retrieve, POST=create, PUT=update, DELETE=remove, PATCH=partial update

## Process note
Built this while learning Flask/HTTP from scratch — asked a lot of dumb
questions along the way (what's a flag, what's localhost, why does my
port not work), broke things, got confused, kept going anyway. Learned
with guidance from Claude (Anthropic) as a mentor throughout — explaining
concepts, correcting mistakes, and walking through the debugging.
