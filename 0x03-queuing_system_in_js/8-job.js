#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs from an array of job information.
 * Each job will be of type 'push_notification_code_3' and will emit various events
 * during its lifecycle including enqueue, complete, failed, and progress.
 * 
 * @param {Object[]} jobs - Array of job information objects to create notifications for
 * @param {Queue} queue - Kue queue instance to add the jobs to
 * @throws {Error} If jobs parameter is not an array
 * 
 * Events emitted:
 * - 'enqueue': When job is successfully created and queued
 * - 'complete': When job is completed successfully
 * - 'failed': When job fails with error message
 * - 'progress': When job reports progress percentage
 */
export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
