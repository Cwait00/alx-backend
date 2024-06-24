# Queuing System in JavaScript

This project demonstrates a queuing system implemented in JavaScript using Redis.
The purpose is to showcase how to set up and use Redis to handle basic queuing tasks.

## Installation Instructions

### Prerequisites

- Ubuntu 18.04
- Node.js 12.x
- Redis 6.0.10 or higher

#Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/alx-backend.git
   cd alx-backend/0x03-queuing_system_in_js

2. Install Redis:

- wget http://download.redis.io/releases/redis-6.0.10.tar.gz
- tar xzf redis-6.0.10.tar.gz
- cd redis-6.0.10
- make
- src/redis-server &

3. Verify Redis is working:

- src/redis-cli ping
# Should output: PONG

4. Set and get a value in Redis to verify functionality:

- src/redis-cli
# Inside the Redis CLI:
- 127.0.0.1:6379> set Holberton School
OK
- 127.0.0.1:6379> get Holberton
"School"

5. Copy the dump.rdb file to the project root:

- cp dump.rdb ../

6. Install project dependencies:

- npm install

Project Structure

- package.json: Project metadata and dependencies.
- .babelrc: Babel configuration file.
- dump.rdb: Redis database file.
- src/: Source code directory.
- test/: Test files directory.

Requirements

- Node.js 12.x
- Redis 6.0.10 or higher
- Express
- Kue
- Chai
- Mocha
- Babel

Author:

Full Name: Cwaita Nobongoza
Email: lounobongoza@gmail.com
