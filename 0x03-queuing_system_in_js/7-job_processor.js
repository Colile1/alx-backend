#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

/**
 * Array of phone numbers that are blacklisted from receiving notifications
 * @type {string[]}
 */
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * Sends a notification to a phone number with progress tracking and blacklist validation
 * 
 * @param {string} phoneNumber - The phone number to send notification to
 * @param {string} message - The message content to send
 * @param {Job} job - The Kue job instance for progress tracking
 * @param {Function} done - Callback function to signal job completion or error
 * 
 * @description This function simulates sending a notification with the following behavior:
 * - Tracks progress from 0% to 50% during the first half of execution
 * - Checks if phone number is blacklisted and throws error if found
 * - Logs the notification details when starting to send
 * - Uses a 1-second interval to simulate processing time
 * - Calls done() when complete or done(error) if blacklisted
 */

const sendNotification = (phoneNumber, message, job, done) => {
  let total = 2, pending = 2;
  let sendInterval = setInterval(() => {
    if (total - pending <= total / 2) {
      job.progress(total - pending, total);
    }
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (total === pending) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`,
      );
    }
    --pending || done();
    pending || clearInterval(sendInterval);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
