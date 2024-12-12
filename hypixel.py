import main
r = main.Request(
    'http://api.hypixel.net/v2/status',
    headers={"Api-Key": open('token.env').read().strip()},
        params={"uuid": "99608a14447946fd96aa44a5d1b89334"}
            )

req = None
while True:
    req = r.wait_for_update(req)
    print(req.json()["session"])
