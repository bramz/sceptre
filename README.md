# sceptre
A Python discord bot reworked and updated. Derived from [Apophis](https://github.com/packetfire/apophis)

## Dependencies
* Docker along with `docker-compose`
* Python 3.8+

## Installation
Make sure you have dependencies above installed in your system.

Rest of the steps can be summarized as:
```shell
$ git clone https://github.com/bramz/sceptre.git
$ cd sceptre
$ make setup
$ make poetry-install
```

Initialize docker containers which will install SQLite and Alembic
```shell
$ docker-compose up sqlite3
$ docker-compose run alembic-migrate
```

## Running
You need to get token for your Bot. [This](https://discordpy.readthedocs.io/en/rewrite/discord.html) might be useful.

Steps thereafter look similar to this:
```shell
$ docker-compose up sqlite3
$ BOT_TOKEN=<your_bot_token>
$ poetry run python sceptre
```
**NOTE**: Above steps assume that you are inside `sceptre`'s root directory (one that contains `Makefile` and `Dockerfile`)

If everything is alright, your bot should be running. You can invoke the test command `!test` to test it.

**NOTE**: If you are running the bot for the first time, please read instructions below.

When attempting to run commands with esclated privileges, you will be greeted with "Unauthorized".
Access must be granted to utilized higher level commands. To do so you will need your Discord ID which can be found by following [these](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) steps.

Once that is out of the way, you need to connect to SQLite container, and add your Discord ID to `permissions` table. These steps can be summarized (and visualized as)
```shell
$ docker exec -it <your_containers_name> psql -U postgres
postgres=# \c sceptre
postgres=# INSERT INTO permissions (username, level) VALUES (<your_discord_id>, 2);
```

You can find your container name under column named `NAMES` after running `docker ps`.

### Questions, Issues and Contributions

Any questions in regards to this software, feel free to send an email to, [brockramz@gmail.com](mailto:brockramz@gmail.com).

If any issues occur when accessing/using this application, please file a [bug report issue](https://github.com/bramz/sceptre/issues/new).

To contribute, fork this repository, apply changes to a local branch and [create a pull request](https://github.com/bramz/sceptre/compare). All contributions are welcome and will be reviewed accordingly.