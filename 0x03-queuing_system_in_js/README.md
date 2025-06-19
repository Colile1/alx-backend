# 0x03-queuing_system_in_js

This directory contains tasks and projects related to implementing queuing systems using JavaScript and Redis. The tasks demonstrate how to interact with Redis, perform basic and advanced operations, and build job processing systems.

## Contents
- **0-redis_client.js**: Basic Redis client connection and ping.
- **1-redis_op.js**: Basic Redis operations (set, get, del, etc.).
- **2-redis_op_async.js**: Asynchronous Redis operations using Promises.
- **4-redis_advanced_op.js**: Advanced Redis operations (lists, sets, etc.).
- **5-publisher.js / 5-subscriber.js**: Pub/Sub pattern with Redis.
- **6-job_creator.js / 6-job_processor.js**: Simple job queue creation and processing.
- **7-job_creator.js / 7-job_processor.js**: Advanced job queue creation and processing.
- **8-job.js / 8-job.test.js**: Job creation and testing.
- **9-stock.js**: Stock management with Redis.

## Usage
1. Make sure you have Node.js and Redis installed and running.
2. Install dependencies (if any):
   ```bash
   npm install
   ```
3. Run the desired script:
   ```bash
   node 0-redis_client.js
   # or any other script as needed
   ```

## Notes
- Each file is self-contained for its respective task.
- Some scripts require a running Redis server on the default port (6379).
- For job processing, you may need to run both the creator and processor scripts simultaneously.

---

*This directory is part of the ALX Backend specialization.*